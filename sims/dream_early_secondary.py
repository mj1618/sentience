"""Study 6, Amendment 1: secondary analyses on one dataset (written for Kumral).

S1 rel_delta = log 1-4 Hz minus log 4-40 Hz;  S2 broad = log 4-40 Hz;
S3 delta_early with its within-cell straight-line relation to clock time removed;
plus delta_early with the file end used as the awakening for every recording.
Plan: scenarios/28-earlier-window.md.
"""
import csv
import json
import sys
import warnings
from pathlib import Path

import mne
import numpy as np
from scipy import signal

sys.path.insert(0, str(Path(__file__).parent))
import dream_analysis as da  # noqa: E402
import dream_early as de  # noqa: E402
import dream_features as df  # noqa: E402
import dream_topo as dt  # noqa: E402

warnings.filterwarnings("ignore")
mne.set_log_level("ERROR")
FEATS = ["delta_early", "rel_delta", "broad", "delta_fileend", "delta_time_adjusted"]


def bands(path, onset):
    """(log 1-4 Hz, log 4-40 Hz) mean over good scalp channels, 34-14 s before onset."""
    raw = mne.io.read_raw_edf(path, preload=False)
    picks = [ch for ch in raw.ch_names
             if (p := dt.position(ch, len(raw.ch_names))) is not None and p[2] > -0.2]
    if len(picks) < 19:
        return None
    sf = raw.info["sfreq"]
    need = int(round((onset + 40) * sf))
    if raw.n_times < need:
        return None
    x = raw.get_data(picks=picks, start=raw.n_times - need)
    x = x - x.mean(axis=1, keepdims=True)
    x = signal.sosfiltfilt(signal.butter(4, [0.5, 40], btype="band", fs=sf, output="sos"), x, axis=1)
    if int(round(sf)) != df.FS:
        x = signal.resample_poly(x, df.FS, int(round(sf)), axis=1)
    end = x.shape[1] - (onset + 14) * df.FS
    w = x[:, end - 20 * df.FS: end]
    p2p = np.ptp(w, axis=1)
    good = (p2p > 0) & (p2p <= df.MAX_P2P)
    if good.mean() < 0.7:
        return None
    w = w[good] - w[good].mean(axis=0, keepdims=True)
    return float(df.band_power(w, 1, 4).mean()), float(df.band_power(w, 4, 40).mean())


def clock(t):
    """Hours on a scale that does not wrap at midnight (noon = 12, 1 am = 25)."""
    try:
        t = str(t).strip().upper()
        h, m = t.split(":")[:2]
        v = int(h) % 12 + (12 if "PM" in t else 0) + int(m[:2]) / 60 if ("AM" in t or "PM" in t) else int(h) + int(m[:2]) / 60
        return v + 24 if v < 12 else v
    except (ValueError, AttributeError):
        return np.nan


def run(dataset_dir, out_json):
    root = Path(dataset_dir)
    rec = list(csv.DictReader(open(df.find_records(root), newline="", encoding="utf-8-sig")))
    by_rel, by_base = df.build_index(root)
    rows = []
    for i, r in enumerate(rec):
        if str(r["Last sleep stage"]).strip() not in ("2", "3") or str(r["Experience"]).strip() not in ("0", "2"):
            continue
        p = df.resolve(r["Filename"], by_rel, by_base)
        if p is None:
            continue
        try:
            onset, _ = de.locate_awakening(mne.io.read_raw_edf(p, preload=False))
            a, b = bands(p, onset), bands(p, 0)
        except Exception:                            # noqa: BLE001
            continue
        if a is None:
            continue
        rows.append({"file": r["Filename"], "subject": r["Subject ID"], "stage": str(r["Last sleep stage"]).strip(),
                     "experience": str(r["Experience"]).strip(), "order": i, "time": clock(r.get("Time of awakening")),
                     "delta_early": a[0], "broad": a[1], "rel_delta": a[0] - a[1],
                     "delta_fileend": None if b is None else b[0]})
    Path(out_json).write_text(json.dumps(rows, indent=0))
    print(f"{dataset_dir}: {len(rows)} NREM awakenings")


def analyse(path, n_perm=10000, seed=0):
    rng = np.random.default_rng(seed)
    rows = json.loads(Path(path).read_text())
    y = np.array([r["experience"] == "2" for r in rows])
    cell = np.array([f"{r['subject']}|{r['stage']}" for r in rows])
    both = {c.split("|")[0] for c in np.unique(cell) if y[cell == c].any() and (~y[cell == c]).any()}
    t = np.array([r["time"] for r in rows], float)
    used_time = "clock time"
    if np.isnan(t).mean() > 0.2:
        t, used_time = np.array([r["order"] for r in rows], float), "awakening order"
    print(f"{len(rows)} awakenings, {int(y.sum())} with experience, {len(both)} subjects with both; S3 uses {used_time}")
    out = {"n": len(rows), "subjects_with_both": len(both), "s3_uses": used_time}
    for f in FEATS:
        if f == "delta_time_adjusted":
            v = da.normal_scores([r["delta_early"] for r in rows])
            for c in np.unique(cell):
                m = (cell == c) & ~np.isnan(t) & ~np.isnan(v)
                if m.sum() >= 3 and np.ptp(t[m]) > 0:
                    v[m] = v[m] - np.polyval(np.polyfit(t[m], v[m], 1), t[m])
        else:
            v = da.normal_scores([np.nan if r[f] is None else r[f] for r in rows])
        e, _, used = da.effect(v, y, cell)
        null = np.array([da.effect(v, da.permute_within(y, cell, rng), cell)[0] for _ in range(n_perm)])
        p = float((np.sum(np.abs(null) >= abs(e)) + 1) / (n_perm + 1))
        out[f] = {"effect": float(e), "p": p, "null_sd": float(null.std()), "cells": used}
        print(f"{f:20s} {e:+.3f}  p={p:.4f}  cells {used}")
    return out


if __name__ == "__main__":
    if sys.argv[1] == "features":
        run(sys.argv[2], sys.argv[3])
    else:
        res = analyse(sys.argv[2])
        Path(sys.argv[2]).with_name("study6_secondary.json").write_text(json.dumps(res, indent=1))
