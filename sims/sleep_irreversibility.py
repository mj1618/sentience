"""Scenario 22: time-irreversibility of sleep EEG by stage (pre-registered).

Primary: ordinal-pattern irreversibility (patterns of 3 samples, 40 ms apart;
Jensen-Shannon divergence between forward and time-reversed pattern
distributions) on Fpz-Cz, per 30 s epoch; per-subject median by stage.
Secondary: Pz-Oz; |skewness of 40 ms increments|; spacings of 20 and 100 ms.
Data: Sleep-EDF Expanded (PhysioNet), first-night cassette recordings.
"""
import json
import sys
import warnings
from pathlib import Path

import mne
import numpy as np

warnings.filterwarnings("ignore")
mne.set_log_level("ERROR")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "sleep-edf"
FS = 100
EPOCH = 30 * FS
STAGE = {"Sleep stage W": "wake", "Sleep stage 1": "light", "Sleep stage 2": "light",
         "Sleep stage 3": "deep", "Sleep stage 4": "deep", "Sleep stage R": "rem"}

def op_irreversibility(x, lag):
    """JS divergence between ordinal-pattern distribution of x and of reversed x."""
    def dist(y):
        a, b, c = y[:-2 * lag], y[lag:-lag], y[2 * lag:]
        code = (a < b).astype(int) * 4 + (b < c).astype(int) * 2 + (a < c).astype(int)
        h = np.bincount(code, minlength=8).astype(float)
        return h / h.sum()
    p, q = dist(x), dist(x[::-1])
    m = 0.5 * (p + q)

    def kl(u, v):
        k = u > 0
        return float(np.sum(u[k] * np.log2(u[k] / v[k])))
    return 0.5 * kl(p, m) + 0.5 * kl(q, m)


def inc_skew(x, lag):
    d = x[lag:] - x[:-lag]
    s = d.std()
    return float(abs(np.mean((d - d.mean()) ** 3)) / s ** 3) if s > 0 else np.nan


def analyse(psg, hyp):
    raw = mne.io.read_raw_edf(psg, preload=False, include=["EEG Fpz-Cz", "EEG Pz-Oz"])
    assert int(raw.info["sfreq"]) == FS
    ann = mne.read_annotations(hyp)
    data = raw.get_data()                       # 2 x n
    out = {m: {s: [] for s in ("wake", "light", "deep", "rem")}
           for m in ("op40_fpz", "op40_pz", "skew40_fpz", "op20_fpz", "op100_fpz")}
    for onset, dur, desc in zip(ann.onset, ann.duration, ann.description):
        st = STAGE.get(desc)
        if st is None:
            continue
        start = int(round(onset * FS))
        for k in range(int(dur // 30)):
            seg = data[:, start + k * EPOCH: start + (k + 1) * EPOCH]
            if seg.shape[1] < EPOCH or np.ptp(seg[0]) == 0:
                continue
            out["op40_fpz"][st].append(op_irreversibility(seg[0], 4))
            out["op40_pz"][st].append(op_irreversibility(seg[1], 4))
            out["skew40_fpz"][st].append(inc_skew(seg[0], 4))
            out["op20_fpz"][st].append(op_irreversibility(seg[0], 2))
            out["op100_fpz"][st].append(op_irreversibility(seg[0], 10))
    return {m: {s: (float(np.nanmedian(v)) if len(v) >= 10 else None, len(v)) for s, v in d.items()}
            for m, d in out.items()}


def main():
    subs = {}
    for hyp in sorted(DATA.glob("SC4*-Hypnogram.edf")):
        psg = DATA / (hyp.name[:6] + "E0-PSG.edf")
        if not psg.exists():
            continue
        try:
            subs[hyp.name[:6]] = analyse(psg, hyp)
        except Exception as e:                   # noqa: BLE001
            print("skip", hyp.name, e, file=sys.stderr)
    measures = list(next(iter(subs.values())).keys())
    summary = {}
    for m in measures:
        rows = [(s, {k: v[0] for k, v in d[m].items()}) for s, d in subs.items()
                if all(d[m][k][0] is not None for k in ("wake", "deep", "rem"))]
        w = np.array([r[1]["wake"] for r in rows]); d = np.array([r[1]["deep"] for r in rows])
        r_ = np.array([r[1]["rem"] for r in rows]); l = np.array([r[1]["light"] or np.nan for r in rows])
        summary[m] = {
            "subjects": len(rows),
            "median_wake": float(np.median(w)), "median_light": float(np.nanmedian(l)),
            "median_deep": float(np.median(d)), "median_rem": float(np.median(r_)),
            "frac_wake_gt_deep": float(np.mean(w > d)),
            "frac_rem_gt_deep": float(np.mean(r_ > d)),
            "frac_rem_closer_to_wake": float(np.mean(np.abs(r_ - w) < np.abs(r_ - d))),
            "frac_rem_lt_wake": float(np.mean(r_ < w)),
        }
        s = summary[m]
        print(f"{m:11s} n={s['subjects']:2d}  wake {s['median_wake']:.5f}  light {s['median_light']:.5f}  "
              f"deep {s['median_deep']:.5f}  rem {s['median_rem']:.5f} | wake>deep {s['frac_wake_gt_deep']:.2f}  "
              f"rem>deep {s['frac_rem_gt_deep']:.2f}  rem closer to wake {s['frac_rem_closer_to_wake']:.2f}")
    (ROOT / "sims" / "out" / "sleep_irreversibility.json").write_text(
        json.dumps({"summary": summary, "subjects": subs}, indent=1))


if __name__ == "__main__":
    main()


# ---- Exploratory, NOT pre-registered: how far above the noise floor is each stage? ----
def surrogate_floor(seed=0):
    """For each epoch, compare the primary measure with the same measure on a
    phase-randomised copy (same power spectrum, time-reversible by construction)."""
    rng = np.random.default_rng(seed)
    res = {}
    for hyp in sorted(DATA.glob("SC4*-Hypnogram.edf")):
        psg = DATA / (hyp.name[:6] + "E0-PSG.edf")
        raw = mne.io.read_raw_edf(psg, preload=False, include=["EEG Fpz-Cz"])
        x = raw.get_data()[0]
        ann = mne.read_annotations(hyp)
        acc = {s: [] for s in ("wake", "light", "deep", "rem")}
        for onset, dur, desc in zip(ann.onset, ann.duration, ann.description):
            st = STAGE.get(desc)
            if st is None:
                continue
            start = int(round(onset * FS))
            for k in range(0, int(dur // 30), 3):          # every third epoch, for speed
                seg = x[start + k * EPOCH: start + (k + 1) * EPOCH]
                if len(seg) < EPOCH or np.ptp(seg) == 0:
                    continue
                f = np.fft.rfft(seg)
                ph = rng.uniform(0, 2 * np.pi, len(f)); ph[0] = 0
                sur = np.fft.irfft(np.abs(f) * np.exp(1j * ph), n=len(seg))
                acc[st].append((op_irreversibility(seg, 4), op_irreversibility(sur, 4)))
        res[hyp.name[:6]] = {s: (float(np.median([a for a, _ in v])), float(np.median([b for _, b in v])),
                                 float(np.mean([a > b for a, b in v])))
                             for s, v in acc.items() if len(v) >= 10}
    print("\nExploratory: primary measure vs phase-randomised surrogate (median across subjects)")
    for st in ("wake", "light", "deep", "rem"):
        rows = [r[st] for r in res.values() if st in r]
        print(f"{st:6s} real {np.median([r[0] for r in rows]):.5f}  surrogate {np.median([r[1] for r in rows]):.5f}  "
              f"share of epochs above own surrogate {np.median([r[2] for r in rows]):.2f}  (n={len(rows)})")
    return res


if __name__ == "__main__" and "--floor" in sys.argv:
    out = surrogate_floor()
    p = ROOT / "sims" / "out" / "sleep_irreversibility.json"
    d = json.loads(p.read_text()); d["exploratory_surrogate_floor"] = out
    p.write_text(json.dumps(d, indent=1))
