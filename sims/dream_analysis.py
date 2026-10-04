"""Study 1 analysis, version 2 (after the methods review, before unblinding).

Contrast: experience ('2') vs no experience ('0') in N2 and N3, computed WITHIN
subject x stage cells and combined. Features are converted to normal scores
within dataset. Effects are in units of the pooled within-cell, within-label SD.
Primary test: permutation of labels within cells (statistic = cell-weight
weighted mean of dataset effects). Generalisation: Hartung-Knapp interval.
FROZEN by scenarios/23-what-goes-with-experience-in-sleep.md, Amendment 1.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

BASE = ["post_delta", "post_hf", "lz", "irr", "fp_lag"]
TESTS = ["post_delta", "post_hf", "lz", "lz_adj", "irr", "irr_adj", "fp_lag", "fp_lag_adj"]
NREM = {"2", "3"}
MIN_SUBJECTS = 8
N_PERM = 10000


def normal_scores(v):
    v = np.asarray(v, float)
    out = np.full(len(v), np.nan)
    ok = ~np.isnan(v)
    r = stats.rankdata(v[ok])
    out[ok] = stats.norm.ppf((r - 0.5) / ok.sum())
    return out


def residual(y, xs):
    ok = ~np.isnan(y) & np.all([~np.isnan(x) for x in xs], axis=0)
    out = np.full(len(y), np.nan)
    a = np.column_stack([np.ones(ok.sum())] + [x[ok] for x in xs])
    out[ok] = y[ok] - a @ np.linalg.lstsq(a, y[ok], rcond=None)[0]
    return out


def prepare(rows, stages=NREM, labels=("0", "2")):
    rows = [r for r in rows if r["stage"] in stages and r["experience"] in labels]
    f = {k: normal_scores([np.nan if r.get(k) is None else r[k] for r in rows]) for k in BASE}
    f["lz_adj"] = residual(f["lz"], [f["post_delta"], f["post_hf"]])
    f["irr_adj"] = residual(f["irr"], [f["post_delta"]])
    f["fp_lag_adj"] = residual(f["fp_lag"], [f["post_delta"]])
    y = np.array([r["experience"] == labels[1] for r in rows])
    cell = np.array([f"{r['subject']}|{r['stage']}" for r in rows])
    subj = np.array([r["subject"] for r in rows])
    return rows, f, y, cell, subj


def effect(v, y, cell):
    """Weighted mean of within-cell differences, scaled by pooled within-cell,
    within-label SD. Returns (effect, total weight, cells used, subjects used)."""
    num = den = 0.0
    ss = dof = 0.0
    used = 0
    for c in np.unique(cell):
        m = (cell == c) & ~np.isnan(v)
        e, n = v[m & y], v[m & ~y]
        if len(e) == 0 or len(n) == 0:
            continue
        w = len(e) * len(n) / (len(e) + len(n))
        num += w * (e.mean() - n.mean()); den += w; used += 1
        ss += ((e - e.mean()) ** 2).sum() + ((n - n.mean()) ** 2).sum(); dof += len(e) + len(n) - 2
    if den == 0 or dof <= 0:
        return np.nan, 0.0, 0
    return num / den / np.sqrt(ss / dof), den, used


def permute_within(y, cell, rng):
    yp = y.copy()
    for c in np.unique(cell):
        m = np.nonzero(cell == c)[0]
        yp[m] = y[rng.permutation(m)]
    return yp


def hartung_knapp(est, se):
    y, v = np.asarray(est), np.asarray(se) ** 2
    k = len(y)
    w = 1 / v
    fixed = np.sum(w * y) / np.sum(w)
    q = np.sum(w * (y - fixed) ** 2)
    tau2 = max(0.0, (q - (k - 1)) / (np.sum(w) - np.sum(w ** 2) / np.sum(w)))
    wr = 1 / (v + tau2)
    mu = np.sum(wr * y) / np.sum(wr)
    var = max(np.sum(wr * (y - mu) ** 2) / ((k - 1) * np.sum(wr)), 1 / np.sum(wr))   # truncated HK
    half = stats.t.ppf(0.975, k - 1) * np.sqrt(var)
    return float(mu), float(mu - half), float(mu + half), float(tau2)


def analyse(datasets, stages=NREM, labels=("0", "2"), seed=0, n_perm=N_PERM, verbose=True):
    rng = np.random.default_rng(seed)
    prep = {}
    for name, rows in datasets.items():
        rows_, f, y, cell, subj = prepare(rows, stages, labels)
        n_sub = len({s for s, c in zip(subj, cell)
                     if y[cell == c].any() and (~y[cell == c]).any()})
        prep[name] = (f, y, cell, n_sub, len(rows_), int(y.sum()))
    out = {"datasets": {}, "combined": {}}
    eligible = [n for n, p in prep.items() if p[3] >= MIN_SUBJECTS]
    for name, (f, y, cell, n_sub, n_aw, n_exp) in prep.items():
        out["datasets"][name] = {"awakenings": n_aw, "with_experience": n_exp, "subjects_with_both": n_sub,
                                 "in_primary": name in eligible}
    for t in TESTS:
        obs, wts, ses = {}, {}, {}
        for name in eligible:
            f, y, cell, *_ = prep[name]
            e, w, _ = effect(f[t], y, cell)
            if np.isnan(e):
                continue
            obs[name], wts[name] = e, w
            boot = []
            cells = np.unique(cell)
            subs = np.array([c.split("|")[0] for c in cells])
            us = np.unique(subs)
            for _ in range(500):                        # subject bootstrap for the interval only
                pick = rng.choice(us, len(us))
                idx = np.concatenate([np.nonzero(np.isin(cell, cells[subs == s]))[0] for s in pick])
                # relabel cells so a resampled subject counts as distinct
                tag = np.concatenate([[f"{k}:{c}" for c in cell[np.isin(cell, cells[subs == s])]]
                                      for k, s in enumerate(pick)])
                b, _, _ = effect(f[t][idx], y[idx], tag)
                if not np.isnan(b):
                    boot.append(b)
            ses[name] = float(np.std(boot)) if boot else np.nan
        if not obs:
            continue
        names = list(obs)
        w = np.array([wts[n] for n in names]); e = np.array([obs[n] for n in names])
        stat = float(np.sum(w * e) / np.sum(w))
        null = np.empty(n_perm)
        for i in range(n_perm):
            es = []
            for n in names:
                f, y, cell, *_ = prep[n]
                es.append(effect(f[t], permute_within(y, cell, rng), cell)[0])
            null[i] = np.sum(w * np.array(es)) / np.sum(w)
        p = float((np.sum(np.abs(null) >= abs(stat)) + 1) / (n_perm + 1))
        res = {"combined_effect": stat, "p_perm": p, "k": len(names),
               "per_dataset": {n: {"effect": float(obs[n]), "se_boot": ses[n]} for n in names},
               "same_sign_share": float(np.mean(np.sign(e) == np.sign(stat)))}
        if len(names) >= 3:
            mu, lo, hi, tau2 = hartung_knapp(e, [ses[n] for n in names])
            res.update({"hk_mean": mu, "hk_lo": lo, "hk_hi": hi, "tau2": tau2})
        out["combined"][t] = res
        if verbose:
            per = "  ".join(f"{n}:{obs[n]:+.2f}" for n in names)
            hk = f"  HK [{res.get('hk_lo', float('nan')):+.2f}, {res.get('hk_hi', float('nan')):+.2f}]" if len(names) >= 3 else ""
            print(f"{t:11s} combined {stat:+.3f}  p={p:.4f}  k={len(names)}{hk}   {per}")
    return out


def positive_control(datasets):
    """Within-subject difference between lighter states (wake '0', N1 '1', REM '5') and
    deep sleep ('3'), or N2 if a dataset has no N3: does each feature move at all?"""
    out = {}
    for name, rows in datasets.items():
        f = {k: normal_scores([np.nan if r.get(k) is None else r[k] for r in rows]) for k in BASE}
        st = np.array([r["stage"] for r in rows]); su = np.array([r["subject"] for r in rows])
        deep = "3" if (st == "3").sum() >= 10 else "2"
        res = {}
        for k in BASE:
            d = []
            for s in np.unique(su):
                a = f[k][(su == s) & np.isin(st, ["0", "1", "5"])]
                b = f[k][(su == s) & (st == deep)]
                a, b = a[~np.isnan(a)], b[~np.isnan(b)]
                if len(a) and len(b):
                    d.append(a.mean() - b.mean())
            if len(d) >= 5:
                d = np.array(d)
                res[k] = {"dz": float(d.mean() / d.std(ddof=1)), "n": len(d)}
        out[name] = {"reference_stage": deep, **res}
    return out


def load(paths):
    return {Path(p).stem: json.loads(Path(p).read_text())["rows"] for p in paths}


if __name__ == "__main__":
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    data = load(paths)
    n_perm = 2000 if "--quick" in sys.argv else N_PERM
    print("NREM, experience vs no experience")
    res = {"nrem": analyse(data, n_perm=n_perm)}
    for n, d in res["nrem"]["datasets"].items():
        print("  ", n, d)
    if "--all" in sys.argv:
        print("\nREM, experience vs no experience")
        res["rem"] = analyse(data, stages={"5"}, n_perm=n_perm)
        print("\nNREM, experience without recall vs no experience")
        res["white"] = analyse(data, labels=("0", "1"), n_perm=n_perm)
        res["positive_control"] = positive_control(data)
        print("\nPositive control (lighter states minus deep sleep, within subject, dz)")
        for n, d in res["positive_control"].items():
            print("  ", n, {k: (round(v["dz"], 2) if isinstance(v, dict) else v) for k, v in d.items()})
    out = next((a.split("=")[1] for a in sys.argv[1:] if a.startswith("--out=")), None)
    if out:
        Path(out).write_text(json.dumps(res, indent=1))
