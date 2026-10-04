"""Study 4: does how a sleeper wakes up predict whether experience is reported?

Plan fixed in scenarios/26-does-the-waking-up-matter.md.
Data: De Gennaro 'Multiple awakenings' (DREAM), whose files continue past the awakening.
"""
import csv
import json
import sys
from pathlib import Path

import mne
import numpy as np
from scipy import signal

sys.path.insert(0, str(Path(__file__).parent))
import dream_analysis as da  # noqa: E402
import dream_features as df  # noqa: E402

mne.set_log_level("ERROR")
ROOT = Path(__file__).resolve().parent.parent
MULTI = ROOT / "data" / "dream" / "conf" / "multi"
MEASURES = ["emg_jump", "emg_rise", "delta_after", "delta_drop", "delta_before"]


def emg_envelope(raw):
    """1-second RMS of chin EMG (20-100 Hz) over the last 60 s. Returns (rms, n_seconds)."""
    names = {c.upper(): c for c in raw.ch_names}
    if "EMG1" not in names or "EMG2" not in names:
        return None
    sf = raw.info["sfreq"]
    n = int(min(raw.n_times, 60 * sf))
    x = raw.get_data(picks=[names["EMG1"], names["EMG2"]], start=raw.n_times - n)
    e = x[0] - x[1]
    hi = min(100.0, sf / 2 - 1)
    e = signal.sosfiltfilt(signal.butter(4, [20, hi], btype="band", fs=sf, output="sos"), e)
    k = int(sf)
    secs = len(e) // k
    return np.sqrt((e[-secs * k:].reshape(secs, k) ** 2).mean(axis=1))


def find_onset(rms):
    base = np.median(rms[:20])
    if base <= 0:
        return None, base
    above = rms > 3 * base
    for t in range(20, len(rms) - 4):
        if above[t] and above[t + 1:t + 5].sum() >= 3:
            return t, base
    return None, base


def posterior_delta(x, sites, start, stop):
    """log 1-4 Hz power over posterior sites for samples [start, stop) at FS; None if it fails the check."""
    if start < 2 * df.FS or stop > x.shape[1]:
        return None
    w = x[:, start:stop]
    if np.ptp(w, axis=1).max() > df.MAX_P2P:
        return None
    w = w - w.mean(axis=0, keepdims=True)
    post = [k for k, s in enumerate(sites) if s in df.POST]
    return float(df.band_power(w[post], 1, 4).mean())


def features(path):
    raw = mne.io.read_raw_edf(path, preload=False)
    rms = emg_envelope(raw)
    if rms is None or len(rms) < 40:
        return None, "no EMG or recording too short"
    onset, base = find_onset(rms)
    if onset is None:
        return None, "no awakening onset found"
    after = len(rms) - onset                       # seconds of recording after onset
    if after < 4:
        return None, "onset within last 4 s"
    out = {"onset_before_end": int(after),
           "emg_jump": float(np.log10(rms[onset:onset + 3].mean()) - np.log10(base))}
    big = np.nonzero(rms[onset:] >= 10 * base)[0]
    out["emg_rise"] = float(min(big[0], 10)) if len(big) else 10.0
    got, why = df.load(path)
    out.update({"delta_after": None, "delta_drop": None, "delta_before": None})
    if got is not None:
        x, sites = got
        end = x.shape[1]                           # df.load trims trailing padding; align on the file end
        on = end - after * df.FS
        before = posterior_delta(x, sites, on - 22 * df.FS, on - 2 * df.FS)
        aft = posterior_delta(x, sites, on + 1 * df.FS, on + 9 * df.FS) if after >= 9 else None
        out["delta_before"] = before; out["delta_after"] = aft
        if before is not None and aft is not None:
            out["delta_drop"] = aft - before
    return out, None


def build():
    root = MULTI
    rec = list(csv.DictReader(open(df.find_records(root), newline="", encoding="utf-8-sig")))
    by_rel, by_base = df.build_index(root)
    rows, excluded = [], []
    for r in rec:
        p = df.resolve(r["Filename"], by_rel, by_base)
        if p is None:
            excluded.append((r["Filename"], "file not found")); continue
        try:
            f, why = features(p)
        except Exception as e:                       # noqa: BLE001
            f, why = None, f"error: {e}"
        if f is None:
            excluded.append((r["Filename"], why)); continue
        rows.append({"file": r["Filename"], "subject": r["Subject ID"], "experience": str(r["Experience"]).strip(),
                     "stage": str(r["Last sleep stage"]).strip(), **f})
    return rows, excluded


def analyse(rows, n_perm=10000, seed=0):
    rng = np.random.default_rng(seed)
    rows = [r for r in rows if r["stage"] in ("2", "3") and r["experience"] in ("0", "2")]
    y = np.array([r["experience"] == "2" for r in rows])
    cell = np.array([f"{r['subject']}|{r['stage']}" for r in rows])
    res = {"n": len(rows), "n_experience": int(y.sum())}
    for m in MEASURES:
        v = da.normal_scores([np.nan if r.get(m) is None else r[m] for r in rows])
        e, w, used = da.effect(v, y, cell)
        null = np.array([da.effect(v, da.permute_within(y, cell, rng), cell)[0] for _ in range(n_perm)])
        p = float((np.sum(np.abs(null) >= abs(e)) + 1) / (n_perm + 1))
        res[m] = {"effect": float(e), "p": p, "n_used": int((~np.isnan(v)).sum()), "cells": used,
                  "null_sd": float(np.nanstd(null))}
        print(f"{m:13s} effect {e:+.3f}  p={p:.4f}  awakenings with measure {res[m]['n_used']}  cells {used}")
    return res


if __name__ == "__main__":
    rows, excluded = build()
    reasons = {}
    for _, w in excluded:
        reasons[w] = reasons.get(w, 0) + 1
    print(f"{len(rows)} recordings with an awakening onset; excluded {reasons}")
    ob = np.array([r["onset_before_end"] for r in rows])
    print(f"onset before end of file: median {np.median(ob):.0f} s, range {ob.min()}-{ob.max()} s")
    res = analyse(rows, n_perm=2000 if "--quick" in sys.argv else 10000)
    (ROOT / "sims" / "out" / "dream" / "study4_awakening.json").write_text(
        json.dumps({"rows": rows, "excluded": excluded, "results": res}, indent=1))
