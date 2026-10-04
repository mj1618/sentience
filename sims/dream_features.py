"""Study 1: which brain-activity measures go with reported experience in sleep?

Computes five theory-derived features from the last 20 s of EEG before each
awakening in DREAM-format datasets (EDF files + Records.csv). The feature
definitions here are FROZEN by the pre-registration in
scenarios/23-what-goes-with-experience-in-sleep.md; do not change them
without a dated amendment there.
"""
import csv
import json
import sys
import warnings
from pathlib import Path

import mne
import numpy as np
from scipy import signal

warnings.filterwarnings("ignore")
mne.set_log_level("ERROR")

FS = 100                     # analysis sampling rate (Hz)
WIN = 20                     # seconds before awakening
SITES = ["F3", "FZ", "F4", "C3", "CZ", "C4", "P3", "PZ", "P4", "O1", "O2"]
FRONT = ["F3", "FZ", "F4"]
POST = ["P3", "PZ", "P4", "O1", "O2"]
LAGS = [2, 5, 10]            # samples at 100 Hz = 20, 50, 100 ms
MIN_SITES = 8


def norm_name(ch):
    c = ch.upper().replace("EEG", "").strip()
    for sep in ("-", ":", " "):
        c = c.split(sep)[0] if c.split(sep)[0] else c
    return c.strip()


def load_window(path):
    """Return (data [n_sites x n_samples], site names) for the last WIN s, or None."""
    raw = mne.io.read_raw_edf(path, preload=False)
    names = {}
    for ch in raw.ch_names:
        n = norm_name(ch)
        if n in SITES and n not in names:
            names[n] = ch
    if len(names) < MIN_SITES or not any(s in names for s in FRONT) or not any(s in names for s in POST):
        return None
    sf = raw.info["sfreq"]
    n_need = int(round((WIN + 2) * sf))            # 2 s pad for filter edges
    if raw.n_times < n_need:
        return None
    sites = [s for s in SITES if s in names]
    x = raw.get_data(picks=[names[s] for s in sites], start=raw.n_times - n_need)
    x = x - x.mean(axis=1, keepdims=True)
    keep = np.ptp(x, axis=1) > 0                   # drop flat channels (e.g. the recording reference)
    x = x[keep]; sites = [s for s, k in zip(sites, keep) if k]
    if len(sites) < MIN_SITES or not any(s in FRONT for s in sites) or not any(s in POST for s in sites):
        return None
    # zero-phase band-pass 0.5-40 Hz, then resample to FS
    sos = signal.butter(4, [0.5, 40], btype="band", fs=sf, output="sos")
    x = signal.sosfiltfilt(sos, x, axis=1)
    x = signal.resample_poly(x, FS, int(round(sf)), axis=1) if int(round(sf)) != FS else x
    x = x[:, -WIN * FS:]
    x = x - x.mean(axis=0, keepdims=True)          # average reference over the selected sites
    return x, sites


def band_power(x, lo, hi):
    f, p = signal.welch(x, fs=FS, nperseg=2 * FS, noverlap=FS, axis=1)
    k = (f >= lo) & (f <= hi)
    return np.log10(p[:, k].mean(axis=1))


def lz_complexity(b):
    """Lempel-Ziv (1976) phrase count of a binary sequence."""
    s = "".join("1" if v else "0" for v in b)
    i, c, n = 0, 0, len(s)
    while i < n:
        l = 1
        while i + l <= n and s[i:i + l] in s[:i + l - 1]:
            l += 1
        c += 1
        i += l
    return c


def lz_norm(x):
    out = []
    n = x.shape[1]
    for ch in x:
        b = ch > np.median(ch)
        out.append(lz_complexity(b) * np.log2(n) / n)
    return float(np.mean(out))


def lag_asym(a, b, lag):
    """corr(a_t, b_{t+lag}) - corr(b_t, a_{t+lag}); positive = a leads b."""
    def c(u, v):
        u = u[:-lag]; v = v[lag:]
        return np.corrcoef(u, v)[0, 1]
    return c(a, b) - c(b, a)


def irreversibility_cv(x):
    """Cross-validated squared lag-asymmetry over channel pairs: product of the
    asymmetry estimated on the first and second half of the window, averaged over
    pairs and lags. Unbiased around zero for a time-reversible process."""
    h = x.shape[1] // 2
    x1, x2 = x[:, :h], x[:, h:]
    acc = []
    for i in range(x.shape[0]):
        for j in range(i + 1, x.shape[0]):
            for lag in LAGS:
                acc.append(lag_asym(x1[i], x1[j], lag) * lag_asym(x2[i], x2[j], lag))
    return float(np.mean(acc))


def front_leads(x, sites):
    f = x[[k for k, s in enumerate(sites) if s in FRONT]].mean(axis=0)
    p = x[[k for k, s in enumerate(sites) if s in POST]].mean(axis=0)
    return float(np.mean([lag_asym(f, p, lag) for lag in LAGS]))


def features(path):
    w = load_window(path)
    if w is None:
        return None
    x, sites = w
    post = [k for k, s in enumerate(sites) if s in POST]
    return {
        "post_delta": float(band_power(x[post], 1, 4).mean()),
        "post_hf": float(band_power(x[post], 20, 40).mean()),
        "lz": lz_norm(x),
        "irr_cv": irreversibility_cv(x),
        "front_leads": front_leads(x, sites),
        "n_sites": len(sites),
    }


def run(dataset_dir, out_json):
    """dataset_dir must contain Records.csv; EDFs are found by filename anywhere below."""
    root = Path(dataset_dir)
    rec = list(csv.DictReader(open(next(root.rglob("Records.csv")), newline="", encoding="utf-8-sig")))
    index = {p.name: p for p in root.rglob("*.edf")}
    rows = []
    for r in rec:
        p = index.get(Path(r["Filename"]).name)
        if p is None:
            continue
        try:
            f = features(p)
        except Exception as e:                       # noqa: BLE001
            print("skip", r["Filename"], e, file=sys.stderr)
            f = None
        if f is None:
            continue
        rows.append({"file": r["Filename"], "subject": r["Subject ID"], "experience": r["Experience"],
                     "stage": r["Last sleep stage"], **f})
    Path(out_json).write_text(json.dumps(rows, indent=0))
    print(f"{dataset_dir}: {len(rows)} of {len(rec)} awakenings processed")
    return rows


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
