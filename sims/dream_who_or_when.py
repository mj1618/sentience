"""Study 2: is a 'no experience' report about the moment, or about the person?

Plan fixed in scenarios/24-who-or-when.md before this was run.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
REC = ROOT / "data" / "dream" / "records.csv"
DSETS = ROOT / "data" / "dream" / "datasets.csv"
FEATS = ["post_delta", "post_hf", "lz", "irr", "fp_lag"]
FEATURE_FILES = ["zhang", "tononi", "multi", "noreika", "aamodt_eve", "aamodt_morn"]


def auc(score, y):
    score, y = np.asarray(score, float), np.asarray(y, bool)
    pos, neg = score[y], score[~y]
    if len(pos) == 0 or len(neg) == 0:
        return np.nan
    gt = (pos[:, None] > neg[None, :]).sum() + 0.5 * (pos[:, None] == neg[None, :]).sum()
    return gt / (len(pos) * len(neg))


def icc_oneway(groups):
    """One-way random-effects ICC(1) for unbalanced binary data."""
    groups = [np.asarray(g, float) for g in groups if len(g) >= 2]
    k = len(groups); n = sum(len(g) for g in groups)
    grand = np.concatenate(groups).mean()
    msb = sum(len(g) * (g.mean() - grand) ** 2 for g in groups) / (k - 1)
    msw = sum(((g - g.mean()) ** 2).sum() for g in groups) / (n - k)
    n0 = (n - sum(len(g) ** 2 for g in groups) / n) / (k - 1)
    return (msb - msw) / (msb + (n0 - 1) * msw)


def person_scores(subj, y):
    """Leave-one-out share of the subject's other awakenings with experience."""
    by = defaultdict(list)
    for i, s in enumerate(subj):
        by[s].append(i)
    score = np.full(len(y), np.nan)
    for s, idx in by.items():
        if len(idx) < 3:
            continue
        tot = sum(y[i] for i in idx)
        for i in idx:
            score[i] = (tot - y[i]) / (len(idx) - 1)
    return score


def logistic_fit(x, y, l2=1.0, iters=200):
    x = np.column_stack([np.ones(len(x)), x])
    w = np.zeros(x.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-x @ w))
        g = x.T @ (p - y) + l2 * np.r_[0, w[1:]]
        h = x.T @ (x * (p * (1 - p))[:, None]) + l2 * np.diag(np.r_[0, np.ones(x.shape[1] - 1)])
        w -= np.linalg.solve(h, g)
    return w


def loso_scores(x, y, subj):
    score = np.full(len(y), np.nan)
    for s in np.unique(subj):
        te = subj == s
        mu, sd = x[~te].mean(0), x[~te].std(0)
        w = logistic_fit((x[~te] - mu) / sd, y[~te].astype(float))
        score[te] = np.column_stack([np.ones(te.sum()), (x[te] - mu) / sd]) @ w
    return score


def table_part():
    names = {r["Set ID"]: r["Common name"] for r in csv.DictReader(open(DSETS, newline="", encoding="utf-8-sig"))}
    rows = list(csv.DictReader(open(REC, newline="", encoding="utf-8-sig")))
    latest = defaultdict(int)
    for r in rows:
        latest[r["Set ID"]] = max(latest[r["Set ID"]], int(r["Amendment"]))
    rows = [r for r in rows if int(r["Amendment"]) == latest[r["Set ID"]]
            and r["Last sleep stage"] in ("N2", "N3/NREM3/NREM4") and r["Experience"] in ("Experience", "No experience")]
    out = {}
    for sid in sorted({r["Set ID"] for r in rows}, key=int):
        rr = [r for r in rows if r["Set ID"] == sid]
        subj = np.array([r["Subject ID"] for r in rr]); y = np.array([r["Experience"] == "Experience" for r in rr])
        counts = defaultdict(int)
        for s in subj:
            counts[s] += 1
        if sum(c >= 3 for c in counts.values()) < 8:
            continue
        ps = person_scores(subj, y); ok = ~np.isnan(ps)
        stage = np.array([r["Last sleep stage"] == "N2" for r in rr], float)
        by = defaultdict(list)
        for s, v in zip(subj, y):
            by[s].append(v)
        out[names[sid]] = {"awakenings": len(rr), "subjects": len(counts), "experience_rate": float(y.mean()),
                           "auc_person": float(auc(ps[ok], y[ok])), "n_person": int(ok.sum()),
                           "auc_stage": float(auc(stage, y)) if 0 < stage.mean() < 1 else None,
                           "icc": float(icc_oneway(list(by.values()))),
                           "_subj": subj.tolist(), "_y": y.tolist(), "_ps": ps.tolist()}
    return out


def feature_part():
    out = {}
    for name in FEATURE_FILES:
        rows = json.loads((ROOT / "sims" / "out" / "dream" / f"{name}.json").read_text())["rows"]
        rows = [r for r in rows if r["stage"] in ("2", "3") and r["experience"] in ("0", "2")
                and all(r.get(f) is not None for f in FEATS)]
        subj = np.array([r["subject"] for r in rows]); y = np.array([r["experience"] == "2" for r in rows])
        x = np.array([[r[f] for f in FEATS] for r in rows], float)
        if len(np.unique(subj)) < 8 or y.sum() < 10 or (~y).sum() < 10:
            continue
        res = {"awakenings": len(rows), "auc_brain": float(auc(loso_scores(x, y, subj), y))}
        ps = person_scores(subj, y); ok = ~np.isnan(ps)
        res["auc_person_same_rows"] = float(auc(ps[ok], y[ok]))
        # within person: subtract subject means; keep subjects with both kinds
        both = np.array([y[subj == s].any() and (~y[subj == s]).any() for s in subj])
        xw = x.copy()
        for s in np.unique(subj):
            xw[subj == s] -= x[subj == s].mean(0)
        if both.sum() >= 30:
            sc = loso_scores(xw[both], y[both], subj[both])
            # score within person: rank within subject so between-person rate differences cannot help
            aucs, wts = [], []
            for s in np.unique(subj[both]):
                m = subj[both] == s
                a = auc(sc[m], y[both][m])
                if not np.isnan(a):
                    aucs.append(a); wts.append(y[both][m].sum() * (~y[both][m]).sum())
            res["auc_brain_within_person"] = float(np.average(aucs, weights=wts))
            res["n_within"] = int(both.sum())
        out[name] = res
    return out


def pooled(table, key, wkey="awakenings"):
    v = [(d[key], d[wkey]) for d in table.values() if d.get(key) is not None]
    return float(np.average([a for a, _ in v], weights=[w for _, w in v])), len(v)


if __name__ == "__main__":
    t = table_part()
    print(f"{'dataset':30s} {'awak':>5} {'subj':>5} {'rate':>5} {'AUC person':>10} {'AUC stage':>9} {'ICC':>6}")
    for n, d in t.items():
        st = f"{d['auc_stage']:.2f}" if d["auc_stage"] is not None else "  -"
        print(f"{n[:30]:30s} {d['awakenings']:5d} {d['subjects']:5d} {d['experience_rate']:5.2f} {d['auc_person']:10.2f} {st:>9} {d['icc']:6.2f}")
    # bootstrap over subjects for the pooled person AUC
    rng = np.random.default_rng(0)
    boot = []
    for _ in range(2000):
        vals, wts = [], []
        for d in t.values():
            subj = np.array(d["_subj"]); y = np.array(d["_y"]); ps = np.array(d["_ps"])
            us = np.unique(subj); pick = rng.choice(us, len(us))
            idx = np.concatenate([np.nonzero(subj == s)[0] for s in pick])
            ok = ~np.isnan(ps[idx]); a = auc(ps[idx][ok], y[idx][ok])
            if not np.isnan(a):
                vals.append(a); wts.append(len(idx))
        boot.append(np.average(vals, weights=wts))
    pa, k = pooled(t, "auc_person"); icc, _ = pooled(t, "icc")
    print(f"\nPooled person AUC {pa:.3f} (95% interval {np.percentile(boot, 2.5):.3f} to {np.percentile(boot, 97.5):.3f}), "
          f"k={k}; pooled ICC {icc:.2f}; stage AUC {pooled(t, 'auc_stage')[0]:.3f}")
    f = feature_part()
    print("\nBrain measures (Study 1 features), same contrast")
    for n, d in f.items():
        print(f"  {n:12s} n={d['awakenings']:4d}  AUC brain {d['auc_brain']:.2f}   AUC person (same rows) {d['auc_person_same_rows']:.2f}   "
              f"AUC brain within person {d.get('auc_brain_within_person', float('nan')):.2f}")
    print("  pooled: brain %.3f, person %.3f, brain within person %.3f" % (
        pooled(f, "auc_brain")[0], pooled(f, "auc_person_same_rows")[0],
        np.average([d["auc_brain_within_person"] for d in f.values() if "auc_brain_within_person" in d],
                   weights=[d["n_within"] for d in f.values() if "auc_brain_within_person" in d])))
    for d in t.values():
        for k_ in ("_subj", "_y", "_ps"):
            d.pop(k_)
    (ROOT / "sims" / "out" / "dream" / "study2_who_or_when.json").write_text(json.dumps({"table": t, "features": f}, indent=1))
