"""Study 1: which brain-activity measures go with reported experience in sleep?

Version 2, after the independent methods review (reviews/round13-study1-methods-review.md)
and BEFORE any confirmation dataset was opened. Definitions are frozen by
scenarios/23-what-goes-with-experience-in-sleep.md (Amendment 1).

Per awakening, from the EEG before waking:
  post_delta, post_hf, lz        from the window -22 s .. -2 s
  irr, fp_lag, fp_lag_orig       from the window -52 s .. -2 s (files long enough only)
"""
import csv
import json
import re
import sys
import warnings
from pathlib import Path

import mne
import numpy as np
from scipy import signal

warnings.filterwarnings("ignore")
mne.set_log_level("ERROR")

FS = 100
SITES = ["F3", "FZ", "F4", "C3", "CZ", "C4", "P3", "PZ", "P4", "O1", "O2"]
FRONT = ["F3", "FZ", "F4"]
POST = ["P3", "PZ", "P4", "O1", "O2"]
LAGS = [2, 5, 10]            # 20, 50, 100 ms
MIN_SITES = 8
SKIP_END = 2                 # seconds dropped before the awakening
SHORT = 20                   # power / complexity window (s)
LONG = 50                    # lag-measure window (s), five 10 s segments
MAX_P2P = 500e-6             # volts; windows with any site above this are excluded
OK_REFS = {"", "REF", "A1", "A2", "M1", "M2", "LE", "AVG", "AV", "CZ", "VREF", "COM", "CLE", "AR"}

# Published 10-20 equivalents for the EGI HydroCel 256/257 net (Cz is the recording reference).
EGI256 = {"F3": "E36", "FZ": "E21", "F4": "E224", "C3": "E59", "C4": "E183",
          "P3": "E87", "PZ": "E101", "P4": "E153", "O1": "E116", "O2": "E150"}


def site_of(label):
    """Map a channel label to a 10-20 site, or None. Rejects bipolar derivations
    whose second electrode is not a reference."""
    c = label.upper().strip()
    c = re.sub(r"^EEG[\s\-_:]*", "", c).strip(" .")
    parts = [p for p in re.split(r"[\s\-_:/]+", c) if p]
    if not parts:
        return None
    first = parts[0]
    m = re.fullmatch(r"(F3|FZ|F4|C3|CZ|C4|P3|PZ|P4|O1|O2)(A1|A2|M1|M2)?", first)
    if not m:
        return None
    second = parts[1] if len(parts) > 1 else ""
    if second not in OK_REFS:
        return None
    return m.group(1)


def channel_map(ch_names):
    labels = {c.upper().strip(): c for c in ch_names}
    # EGI high-density net: channels labelled 'E36', 'Chan 36' or bare '36' (header inspection,
    # Amendments 2 and 3); some recordings have bad channels already removed.
    egi = {re.sub(r"^(E|CHAN\s*)?(\d+)$", r"E\2", k): v for k, v in labels.items()}
    if len(ch_names) >= 200 and "E36" in egi and "E224" in egi:
        return {s: egi[e] for s, e in EGI256.items() if e in egi}
    out = {}
    for ch in ch_names:
        s = site_of(ch)
        if s and s not in out:
            out[s] = ch
    return out


def load(path):
    """Return (x [sites x samples] at FS, original reference; site list) covering the
    end of the file with trailing padding removed, or (None, reason)."""
    raw = mne.io.read_raw_edf(path, preload=False)
    cmap = channel_map(raw.ch_names)
    sites = [s for s in SITES if s in cmap]
    if len(sites) < MIN_SITES:
        return None, f"only {len(sites)} usable sites"
    sf = raw.info["sfreq"]
    n_take = int(min(raw.n_times, round(150 * sf)))
    x = raw.get_data(picks=[cmap[s] for s in sites], start=raw.n_times - n_take)
    # trim trailing constant samples (padding)
    moving = np.any(np.diff(x, axis=1) != 0, axis=0)
    if not moving.any():
        return None, "flat recording"
    x = x[:, : np.max(np.nonzero(moving)[0]) + 2]
    keep = np.ptp(x, axis=1) > 0
    x = x[keep]; sites = [s for s, k in zip(sites, keep) if k]
    if len(sites) < MIN_SITES or not any(s in FRONT for s in sites) or not any(s in POST for s in sites):
        return None, "too few usable sites after dropping flat channels"
    if x.shape[1] < (SHORT + SKIP_END + 4) * sf:
        return None, "recording too short"
    x = x - x.mean(axis=1, keepdims=True)
    sos = signal.butter(4, [0.5, 40], btype="band", fs=sf, output="sos")
    x = signal.sosfiltfilt(sos, x, axis=1)                   # zero-phase, whole chunk
    isf = int(round(sf))
    if isf != FS:
        x = signal.resample_poly(x, FS, isf, axis=1)
    return (x, sites), None


def window(x, seconds):
    end = x.shape[1] - SKIP_END * FS
    start = end - seconds * FS
    return None if start < 2 * FS else x[:, start:end]      # keep 2 s of filter margin


def band_power(x, lo, hi):
    f, p = signal.welch(x, fs=FS, nperseg=2 * FS, noverlap=FS, axis=1)
    k = (f >= lo) & (f <= hi)
    return np.log10(p[:, k].mean(axis=1))


def lz_complexity(b):
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
    n = x.shape[1]
    return float(np.mean([lz_complexity(ch > np.median(ch)) * np.log2(n) / n for ch in x]))


def lag_asym(a, b, lag):
    """corr(a_t, b_{t+lag}) - corr(b_t, a_{t+lag})."""
    return np.corrcoef(a[:-lag], b[lag:])[0, 1] - np.corrcoef(b[:-lag], a[lag:])[0, 1]


def irr(x):
    """Cross-validated irreversibility over five 10 s segments: the pairwise lag
    asymmetry averaged over odd segments times that averaged over even segments,
    mean over site pairs and lags. Centred on zero for a time-reversible process."""
    seg = [x[:, i:i + 10 * FS] for i in range(0, x.shape[1] - 10 * FS + 1, 10 * FS)]

    def a(group):
        return np.array([np.mean([lag_asym(s[i], s[j], lag) for s in group])
                         for i in range(x.shape[0]) for j in range(i + 1, x.shape[0]) for lag in LAGS])
    return float(np.mean(a(seg[0::2]) * a(seg[1::2])))


def fp_lag(x, sites):
    """Fronto-posterior lag asymmetry. Its sign depends on the reference and is not
    interpreted as a direction of flow."""
    f = x[[k for k, s in enumerate(sites) if s in FRONT]].mean(axis=0)
    p = x[[k for k, s in enumerate(sites) if s in POST]].mean(axis=0)
    return float(np.mean([lag_asym(f, p, lag) for lag in LAGS]))


def features(path):
    got, why = load(path)
    if got is None:
        return None, why
    x, sites = got
    short = window(x, SHORT)
    if short is None:
        return None, "recording too short"
    if np.ptp(short, axis=1).max() > MAX_P2P:
        return None, "amplitude above 500 microvolts"
    avg = short - short.mean(axis=0, keepdims=True)
    post = [k for k, s in enumerate(sites) if s in POST]
    out = {"post_delta": float(band_power(avg[post], 1, 4).mean()),
           "post_hf": float(band_power(avg[post], 20, 30).mean()),
           "lz": lz_norm(avg), "n_sites": len(sites),
           "irr": None, "fp_lag": None, "fp_lag_orig": None}
    long_ = window(x, LONG)
    if long_ is not None and np.ptp(long_, axis=1).max() <= MAX_P2P:
        lavg = long_ - long_.mean(axis=0, keepdims=True)
        out["irr"] = irr(lavg)
        out["fp_lag"] = fp_lag(lavg, sites)
        out["fp_lag_orig"] = fp_lag(long_, sites)
    return out, None


def find_records(root):
    cands = sorted(root.rglob("Records.csv"), key=lambda p: len(p.parts))
    if not cands:
        raise SystemExit(f"no Records.csv under {root}")
    return cands[0]


def build_index(root):
    """Map normalised relative path (no extension) and basename to EDF files.
    Aborts on ambiguous basenames only when a record needs them."""
    edfs = [p for p in root.rglob("*") if p.suffix.lower() == ".edf"]
    by_rel, by_base = {}, {}
    for p in edfs:
        rel = str(p.relative_to(root).with_suffix("")).lower().replace("\\", "/")
        by_rel[rel] = p
        by_base.setdefault(p.stem.lower(), []).append(p)
    return by_rel, by_base


def resolve(name, by_rel, by_base):
    key = re.sub(r"\.edf$", "", name.strip().lower().replace("\\", "/"))
    hits = [p for rel, p in by_rel.items() if rel == key or rel.endswith("/" + key)]
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        raise SystemExit(f"ambiguous record filename {name!r}: {hits[:3]}")
    base = by_base.get(key.split("/")[-1], [])
    if len(base) == 1:
        return base[0]
    if len(base) > 1:
        raise SystemExit(f"ambiguous basename {name!r}: {base[:3]}")
    return None


def run(dataset_dir, out_json):
    root = Path(dataset_dir)
    rec = list(csv.DictReader(open(find_records(root), newline="", encoding="utf-8-sig")))
    by_rel, by_base = build_index(root)
    rows, log = [], []
    for r in rec:
        p = resolve(r["Filename"], by_rel, by_base)
        if p is None:
            log.append((r["Filename"], "file not found")); continue
        try:
            f, why = features(p)
        except Exception as e:                       # noqa: BLE001
            f, why = None, f"error: {e}"
        if f is None:
            log.append((r["Filename"], why)); continue
        rows.append({"file": r["Filename"], "subject": r["Subject ID"], "experience": str(r["Experience"]).strip(),
                     "stage": str(r["Last sleep stage"]).strip(), "time": r.get("Time of awakening", ""),
                     "artifacts": r.get("Proportion artifacts", ""), **f})
    Path(out_json).write_text(json.dumps({"rows": rows, "excluded": log, "n_records": len(rec)}, indent=0))
    reasons = {}
    for _, w in log:
        reasons[w] = reasons.get(w, 0) + 1
    print(f"{dataset_dir}: {len(rows)} of {len(rec)} records processed; excluded: {reasons}")
    return rows


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
