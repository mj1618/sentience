"""Study 3: does any EEG measure track the intensity or pleasantness of felt emotion in dreams?

Plan fixed in scenarios/25-does-anything-track-feeling-in-dreams.md.
Data: REM_Turku (DREAM database): 134 REM awakenings, 18 subjects, self-rated emotions.
"""
import csv
import json
import re
import sys
from pathlib import Path

import mne
import numpy as np
from scipy import signal, stats

sys.path.insert(0, str(Path(__file__).parent))
import dream_features as df  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TURKU = ROOT / "data" / "dream" / "emo" / "turku" / "REM_Turku"
MEASURES = ["post_delta", "post_hf", "lz", "irr", "fp_lag", "faa", "eog"]
N_PERM = 10000


def extra(path):
    """faa and eog from the -22..-2 s window."""
    raw = mne.io.read_raw_edf(path, preload=False)
    sf = raw.info["sfreq"]
    names = {c.upper(): c for c in raw.ch_names}
    n_take = int(min(raw.n_times, round(150 * sf)))
    out = {"faa": None, "eog": None}

    def win(x):
        x = x - x.mean()
        end = len(x) - int(df.SKIP_END * sf)
        return x[end - int(df.SHORT * sf): end]
    if "F3" in names and "F4" in names:
        x = raw.get_data(picks=[names["F3"], names["F4"]], start=raw.n_times - n_take)
        sos = signal.butter(4, [0.5, 40], btype="band", fs=sf, output="sos")
        x = signal.sosfiltfilt(sos, x, axis=1)
        p = []
        for ch in x:
            f, pw = signal.welch(win(ch), fs=sf, nperseg=int(2 * sf), noverlap=int(sf))
            p.append(np.log10(pw[(f >= 8) & (f <= 13)].mean()))
        out["faa"] = float(p[1] - p[0])
    if "EOG-HL" in names and "EOG-HR" in names:
        x = raw.get_data(picks=[names["EOG-HL"], names["EOG-HR"]], start=raw.n_times - n_take)
        h = x[0] - x[1]
        sos = signal.butter(4, [0.5, 10], btype="band", fs=sf, output="sos")
        out["eog"] = float(np.log10(np.var(win(signal.sosfiltfilt(sos, h)))))
    return out


def build(max_p2p=None):
    if max_p2p:
        df.MAX_P2P = max_p2p
    rec = {re.sub(r"\.edf$", "", r["Filename"].split("/")[-1]): r
           for r in csv.DictReader(open(TURKU / "Records.csv", newline="", encoding="utf-8-sig"))}
    rows, excluded = [], []
    for r in csv.DictReader(open(TURKU / "Data" / "Ratings.csv", newline="", encoding="utf-8-sig")):
        key = re.sub(r"\.edf$", "", r["Filename"].split("/")[-1])
        path = TURKU / "Data" / "PSG" / f"{key}.edf"
        try:
            pa = [float(r[f"SR_PA{i}"]) for i in range(1, 11)]
            na = [float(r[f"SR_NA{i}"]) for i in range(1, 11)]
        except (ValueError, KeyError):
            excluded.append((key, "no self-ratings")); continue
        if not path.exists() or key not in rec:
            excluded.append((key, "no recording")); continue
        f, why = df.features(path)
        if f is None:
            excluded.append((key, why)); continue
        rows.append({"file": key, "subject": rec[key]["Subject ID"], "stage": rec[key]["Last sleep stage"],
                     "intensity": sum(pa) + sum(na), "valence": float(np.mean(pa) - np.mean(na)),
                     "pos": sum(pa), "neg": sum(na), **f, **extra(path)})
    return rows, excluded


def normal_scores(v):
    v = np.asarray(v, float); out = np.full(len(v), np.nan); ok = ~np.isnan(v)
    out[ok] = stats.norm.ppf((stats.rankdata(v[ok]) - 0.5) / ok.sum())
    return out


def within_corr(x, y, subj):
    ok = ~np.isnan(x) & ~np.isnan(y)
    xs, ys = [], []
    for s in np.unique(subj[ok]):
        m = ok & (subj == s)
        if m.sum() < 3:
            continue
        xs.append(x[m] - x[m].mean()); ys.append(y[m] - y[m].mean())
    if not xs:
        return np.nan, 0, 0
    xs, ys = np.concatenate(xs), np.concatenate(ys)
    return float(np.corrcoef(xs, ys)[0, 1]), len(xs), len(np.unique(subj[ok]))


def analyse(rows, outcomes=("intensity", "valence", "pos", "neg"), seed=0, n_perm=N_PERM):
    rng = np.random.default_rng(seed)
    subj = np.array([r["subject"] for r in rows])
    res = {}
    for o in outcomes:
        y = normal_scores([r[o] for r in rows])
        for m in MEASURES:
            x = normal_scores([np.nan if r.get(m) is None else r[m] for r in rows])
            r_obs, n, k = within_corr(x, y, subj)
            null = np.empty(n_perm)
            for i in range(n_perm):
                yp = y.copy()
                for s in np.unique(subj):
                    idx = np.nonzero(subj == s)[0]
                    yp[idx] = y[rng.permutation(idx)]
                null[i] = within_corr(x, yp, subj)[0]
            p = float((np.sum(np.abs(null) >= abs(r_obs)) + 1) / (n_perm + 1))
            res[f"{o}|{m}"] = {"r": r_obs, "p": p, "n": n, "subjects": k}
            print(f"{o:9s} {m:10s} r={r_obs:+.3f}  p={p:.4f}  n={n}  subjects={k}")
    return res


if __name__ == "__main__":
    limit = 1000e-6 if "--relaxed" in sys.argv else None
    rows, excluded = build(limit)
    reasons = {}
    for _, w in excluded:
        reasons[w] = reasons.get(w, 0) + 1
    print(f"{len(rows)} awakenings usable; excluded {reasons}")
    res = analyse(rows, n_perm=2000 if "--quick" in sys.argv else N_PERM)
    tag = "_relaxed" if limit else ""
    (ROOT / "sims" / "out" / "dream" / f"study3_emotion{tag}.json").write_text(
        json.dumps({"rows": rows, "excluded": excluded, "results": res}, indent=1))
