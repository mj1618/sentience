"""Study 5: is the experience-related difference at the front or the back of the head?

Uses every scalp EEG channel with a known position (not just eleven sites).
Features per awakening, window -22 s .. -2 s, average reference over good channels:
  front_delta, post_delta, grad_delta (= post - front)   log power 1-4 Hz
  front_hf,    post_hf,    grad_hf                        log power 20-30 Hz
Plan: scenarios/27-front-or-back.md.
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

sys.path.insert(0, str(Path(__file__).parent))
import dream_analysis as da  # noqa: E402
import dream_features as df  # noqa: E402

warnings.filterwarnings("ignore")
mne.set_log_level("ERROR")
ROOT = Path(__file__).resolve().parent.parent
FEATS = ["front_delta", "post_delta", "grad_delta", "front_hf", "post_hf", "grad_hf"]
_STD = {k.upper(): v for k, v in mne.channels.make_standard_montage("standard_1005").get_positions()["ch_pos"].items()}
_EGI = {k.upper(): v for k, v in mne.channels.make_standard_montage("GSN-HydroCel-256").get_positions()["ch_pos"].items()}
NOT_SCALP = ("EOG", "EMG", "ECG", "EKG", "LOC", "ROC", "M1", "M2", "A1", "A2", "REF", "VEOG", "HEOG", "CHIN", "RESP")


def position(label, n_channels):
    """Unit-sphere position for a channel label, or None."""
    c = label.upper().strip()
    m = re.fullmatch(r"(?:E|CHAN\s*)?(\d+)", c)
    if m and n_channels >= 200:
        p = _EGI.get("E" + m.group(1))
        return None if p is None else np.asarray(p) / np.linalg.norm(p)
    if c == "01":
        c = "O1"
    c = re.sub(r"^EEG[\s\-_:]*", "", c).strip(" .")
    parts = [x for x in re.split(r"[\s\-_:/]+", c) if x]
    if not parts or parts[0].startswith(NOT_SCALP):
        return None
    if len(parts) > 1 and parts[1] not in df.OK_REFS:
        return None
    p = _STD.get(parts[0])
    return None if p is None else np.asarray(p) / np.linalg.norm(p)


def features(path):
    raw = mne.io.read_raw_edf(path, preload=False)
    pos, picks = [], []
    for ch in raw.ch_names:
        p = position(ch, len(raw.ch_names))
        if p is not None and p[2] > -0.2:               # drop face/neck electrodes of the high-density net
            pos.append(p); picks.append(ch)
    if len(picks) < 19:
        return None, f"only {len(picks)} positioned scalp channels"
    sf = raw.info["sfreq"]
    n_take = int(min(raw.n_times, round(60 * sf)))
    x = raw.get_data(picks=picks, start=raw.n_times - n_take)
    moving = np.any(np.diff(x, axis=1) != 0, axis=0)
    if not moving.any():
        return None, "flat recording"
    x = x[:, : np.max(np.nonzero(moving)[0]) + 2]
    if x.shape[1] < (df.SHORT + df.SKIP_END + 4) * sf:
        return None, "recording too short"
    x = x - x.mean(axis=1, keepdims=True)
    x = signal.sosfiltfilt(signal.butter(4, [0.5, 40], btype="band", fs=sf, output="sos"), x, axis=1)
    isf = int(round(sf))
    if isf != df.FS:
        x = signal.resample_poly(x, df.FS, isf, axis=1)
    w = df.window(x, df.SHORT)
    if w is None:
        return None, "recording too short"
    pos = np.array(pos)
    p2p = np.ptp(w, axis=1)
    good = (p2p > 0) & (p2p <= df.MAX_P2P)
    if good.mean() < 0.7:
        return None, "more than 30% of channels flat or above 500 microvolts"
    w, pos = w[good], pos[good]
    w = w - w.mean(axis=0, keepdims=True)                  # average reference over good scalp channels
    front, post = pos[:, 1] > 0.35, pos[:, 1] < -0.35
    if front.sum() < 3 or post.sum() < 3:
        return None, "too few frontal or posterior channels"
    out = {"n_channels": int(good.sum()), "n_front": int(front.sum()), "n_post": int(post.sum())}
    for name, lo, hi in (("delta", 1, 4), ("hf", 20, 30)):
        bp = df.band_power(w, lo, hi)
        out[f"front_{name}"] = float(bp[front].mean())
        out[f"post_{name}"] = float(bp[post].mean())
        out[f"grad_{name}"] = out[f"post_{name}"] - out[f"front_{name}"]
    return out, None


def run(dataset_dir, out_json):
    root = Path(dataset_dir)
    rec = list(csv.DictReader(open(df.find_records(root), newline="", encoding="utf-8-sig")))
    by_rel, by_base = df.build_index(root)
    rows, log = [], []
    for r in rec:
        p = df.resolve(r["Filename"], by_rel, by_base)
        if p is None:
            log.append((r["Filename"], "file not found")); continue
        try:
            f, why = features(p)
        except Exception as e:                       # noqa: BLE001
            f, why = None, f"error: {e}"
        if f is None:
            log.append((r["Filename"], why)); continue
        rows.append({"file": r["Filename"], "subject": r["Subject ID"], "experience": str(r["Experience"]).strip(),
                     "stage": str(r["Last sleep stage"]).strip(), **f})
    Path(out_json).write_text(json.dumps({"rows": rows, "excluded": log, "n_records": len(rec)}, indent=0))
    reasons = {}
    for _, w in log:
        reasons[w] = reasons.get(w, 0) + 1
    ch = sorted({r["n_channels"] for r in rows})
    print(f"{dataset_dir}: {len(rows)} of {len(rec)} processed; channels {ch[0] if ch else '-'}-{ch[-1] if ch else '-'}; excluded {reasons}")


def analyse(paths, n_perm=10000, seed=0):
    rng = np.random.default_rng(seed)
    data = {Path(p).stem.replace("topo_", ""): json.loads(Path(p).read_text())["rows"] for p in paths}
    prep = {}
    for name, rows in data.items():
        rows = [r for r in rows if r["stage"] in ("2", "3") and r["experience"] in ("0", "2")]
        y = np.array([r["experience"] == "2" for r in rows])
        cell = np.array([f"{r['subject']}|{r['stage']}" for r in rows])
        n_sub = len({c.split("|")[0] for c in np.unique(cell) if y[cell == c].any() and (~y[cell == c]).any()})
        prep[name] = (rows, y, cell, n_sub)
        print(f"{name}: {len(rows)} NREM awakenings, {int(y.sum())} with experience, {n_sub} subjects with both")
    out = {}
    names = [n for n, p in prep.items() if p[3] >= da.MIN_SUBJECTS]
    for f in FEATS:
        vals = {n: da.normal_scores([r[f] for r in prep[n][0]]) for n in names}
        obs = {n: da.effect(vals[n], prep[n][1], prep[n][2]) for n in names}
        w = np.array([obs[n][1] for n in names]); e = np.array([obs[n][0] for n in names])
        stat = float(np.sum(w * e) / np.sum(w))
        null = np.empty(n_perm)
        for i in range(n_perm):
            es = [da.effect(vals[n], da.permute_within(prep[n][1], prep[n][2], rng), prep[n][2])[0] for n in names]
            null[i] = np.sum(w * np.array(es)) / np.sum(w)
        p = float((np.sum(np.abs(null) >= abs(stat)) + 1) / (n_perm + 1))
        out[f] = {"combined": stat, "p": p, "null_sd": float(null.std()),
                  "per_dataset": {n: float(obs[n][0]) for n in names}}
        print(f"{f:12s} combined {stat:+.3f} (95% {stat-1.96*null.std():+.2f} to {stat+1.96*null.std():+.2f})  p={p:.4f}   "
              + "  ".join(f"{n}:{obs[n][0]:+.2f}" for n in names))
    return out


if __name__ == "__main__":
    if sys.argv[1] == "features":
        run(sys.argv[2], sys.argv[3])
    else:
        res = analyse(sys.argv[2:], n_perm=2000 if "--quick" in sys.argv else 10000)
