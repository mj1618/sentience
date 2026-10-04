"""Study 6: slow-wave power 34-14 s before waking versus reported experience.

Plan fixed in scenarios/28-earlier-window.md before this was run on any confirmation recording.
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
import dream_features as df  # noqa: E402
import dream_topo as dt  # noqa: E402

warnings.filterwarnings("ignore")
mne.set_log_level("ERROR")
ROOT = Path(__file__).resolve().parent.parent


def locate_awakening(raw):
    """Seconds before the end of file at which chin EMG first exceeds 3x baseline
    in the last 40 s; 0 if none or no EMG channel."""
    emg = [c for c in raw.ch_names if "EMG" in c.upper()]
    if not emg:
        return 0, "no EMG channel"
    sf = raw.info["sfreq"]
    n = int(min(raw.n_times, 60 * sf))
    if n < 60 * sf:
        return 0, "shorter than 60 s"
    x = raw.get_data(picks=emg[:2], start=raw.n_times - n)
    e = x[0] - x[1] if len(emg) >= 2 else x[0]
    hi = min(100.0, sf / 2 - 1)
    e = signal.sosfiltfilt(signal.butter(4, [20, hi], btype="band", fs=sf, output="sos"), e)
    k = int(sf)
    rms = np.sqrt((e[: 60 * k].reshape(60, k) ** 2).mean(axis=1))
    base = np.median(rms[:20])
    if base <= 0:
        return 0, "flat EMG"
    idx = np.nonzero(rms[20:] > 3 * base)[0]
    if len(idx) == 0:
        return 0, "no rise"
    return int(60 - (20 + idx[0])), "located"


def whole_scalp_delta(path, back_to, back_from, onset):
    """Mean log 1-4 Hz power over good scalp channels for the window
    [onset+back_to, onset+back_from] seconds before the end of file."""
    raw = mne.io.read_raw_edf(path, preload=False)
    pos, picks = [], []
    for ch in raw.ch_names:
        p = dt.position(ch, len(raw.ch_names))
        if p is not None and p[2] > -0.2:
            pos.append(p); picks.append(ch)
    if len(picks) < 19:
        return None, "too few positioned channels"
    sf = raw.info["sfreq"]
    need = int(round((onset + back_to + 6) * sf))
    if raw.n_times < need:
        return None, "recording too short"
    x = raw.get_data(picks=picks, start=raw.n_times - need)
    x = x - x.mean(axis=1, keepdims=True)
    x = signal.sosfiltfilt(signal.butter(4, [0.5, 40], btype="band", fs=sf, output="sos"), x, axis=1)
    isf = int(round(sf))
    if isf != df.FS:
        x = signal.resample_poly(x, df.FS, isf, axis=1)
    end = x.shape[1] - (onset + back_from) * df.FS
    w = x[:, end - (back_to - back_from) * df.FS: end]
    p2p = np.ptp(w, axis=1)
    good = (p2p > 0) & (p2p <= df.MAX_P2P)
    if good.mean() < 0.7:
        return None, "more than 30% of channels bad"
    w = w[good] - w[good].mean(axis=0, keepdims=True)
    return float(df.band_power(w, 1, 4).mean()), None


def run(dataset_dir, out_json):
    root = Path(dataset_dir)
    rec = list(csv.DictReader(open(df.find_records(root), newline="", encoding="utf-8-sig")))
    by_rel, by_base = df.build_index(root)
    rows, log, how = [], [], {}
    for r in rec:
        if str(r["Last sleep stage"]).strip() not in ("2", "3") or str(r["Experience"]).strip() not in ("0", "2"):
            continue
        p = df.resolve(r["Filename"], by_rel, by_base)
        if p is None:
            log.append((r["Filename"], "file not found")); continue
        try:
            onset, note = locate_awakening(mne.io.read_raw_edf(p, preload=False))
            how[note] = how.get(note, 0) + 1
            early, why = whole_scalp_delta(p, 34, 14, onset)
            late, _ = whole_scalp_delta(p, 20, 0, onset)
        except Exception as e:                       # noqa: BLE001
            early, late, why, onset = None, None, f"error: {e}", None
        if early is None:
            log.append((r["Filename"], why)); continue
        rows.append({"file": r["Filename"], "subject": r["Subject ID"], "experience": str(r["Experience"]).strip(),
                     "stage": str(r["Last sleep stage"]).strip(), "onset": onset,
                     "delta_early": early, "delta_late": late})
    Path(out_json).write_text(json.dumps({"rows": rows, "excluded": log, "onset_notes": how}, indent=0))
    reasons = {}
    for _, w in log:
        reasons[w] = reasons.get(w, 0) + 1
    print(f"{dataset_dir}: {len(rows)} NREM awakenings with the measure; awakening {how}; excluded {reasons}")


def analyse(paths, n_perm=10000, seed=0):
    rng = np.random.default_rng(seed)
    out = {}
    for feat in ("delta_early", "delta_late"):
        v, y, cell = [], [], []
        for p in paths:
            name = Path(p).stem
            rows = json.loads(Path(p).read_text())["rows"]
            z = da.normal_scores([np.nan if r[feat] is None else r[feat] for r in rows])
            v.append(z); y.append([r["experience"] == "2" for r in rows])
            cell.append([f"{name}|{r['subject']}|{r['stage']}" for r in rows])
        v, y, cell = np.concatenate(v), np.concatenate(y).astype(bool), np.concatenate(cell)
        e, w, used = da.effect(v, y, cell)
        null = np.array([da.effect(v, da.permute_within(y, cell, rng), cell)[0] for _ in range(n_perm)])
        p = float((np.sum(np.abs(null) >= abs(e)) + 1) / (n_perm + 1))
        per = {}
        for pth in paths:
            name = Path(pth).stem
            m = np.array([c.startswith(name + "|") for c in cell])
            per[name] = (float(da.effect(v[m], y[m], cell[m])[0]), int(da.effect(v[m], y[m], cell[m])[2]))
        out[feat] = {"effect": float(e), "p": p, "null_sd": float(null.std()), "cells": used,
                     "n": int((~np.isnan(v)).sum()), "per_dataset": per}
        print(f"{feat:12s} pooled {e:+.3f} (95% {e-1.96*null.std():+.2f} to {e+1.96*null.std():+.2f})  p={p:.4f}  "
              f"awakenings {out[feat]['n']}  cells {used}   " + "  ".join(f"{k}:{a:+.2f} ({c} cells)" for k, (a, c) in per.items()))
    return out


if __name__ == "__main__":
    if sys.argv[1] == "features":
        run(sys.argv[2], sys.argv[3])
    else:
        res = analyse(sys.argv[2:])
        (ROOT / "sims" / "out" / "dream" / "study6_early.json").write_text(json.dumps(res, indent=1))
