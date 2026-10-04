"""Study 1 analysis: within-subject contrast, experience vs no experience, NREM.

For each dataset: awakenings from N2/N3 with Experience ('2') or No experience
('0'). Each feature is z-scored within the dataset. For every subject with at
least one awakening of each kind, d_s = mean(experience) - mean(no experience);
the dataset effect is the weighted mean of d_s (weights n_E*n_NE/(n_E+n_NE)),
with a subject-bootstrap standard error. Datasets are combined by
inverse-variance random-effects meta-analysis (DerSimonian-Laird).
FROZEN by scenarios/23-what-goes-with-experience-in-sleep.md.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

FEATURES = ["post_delta", "post_hf", "lz", "irr_cv", "front_leads"]
NREM = {"2", "3"}


def dataset_effects(rows, stages=NREM, n_boot=4000, seed=0, adjust_for=None):
    rows = [r for r in rows if r["stage"] in stages and r["experience"] in ("0", "2")]
    out = {"n_awakenings": len(rows), "n_experience": sum(r["experience"] == "2" for r in rows)}
    by = defaultdict(list)
    for r in rows:
        by[r["subject"]].append(r)
    subs = [s for s, v in by.items() if {x["experience"] for x in v} == {"0", "2"}]
    out["n_subjects_both"] = len(subs)
    rng = np.random.default_rng(seed)
    for f in FEATURES:
        v = np.array([r[f] for r in rows], float)
        mu, sd = np.nanmean(v), np.nanstd(v)
        z = {id(r): (r[f] - mu) / sd for r in rows}
        if adjust_for:                                # residualise on another feature (within dataset)
            a = np.array([r[adjust_for] for r in rows], float)
            b = np.polyfit(a, v, 1)
            res = v - np.polyval(b, a)
            z = {id(r): (x - res.mean()) / res.std() for r, x in zip(rows, res)}
        d, w = [], []
        for s in subs:
            e = [z[id(r)] for r in by[s] if r["experience"] == "2"]
            n = [z[id(r)] for r in by[s] if r["experience"] == "0"]
            d.append(np.mean(e) - np.mean(n)); w.append(len(e) * len(n) / (len(e) + len(n)))
        d, w = np.array(d), np.array(w)
        if len(d) < 5:
            # too few subjects with both kinds: between-subject standardised difference (secondary)
            e = np.array([z[id(r)] for r in rows if r["experience"] == "2"])
            n = np.array([z[id(r)] for r in rows if r["experience"] == "0"])
            if len(e) < 5 or len(n) < 5:
                out[f] = None
                continue
            sp = np.sqrt(((len(e) - 1) * e.var(ddof=1) + (len(n) - 1) * n.var(ddof=1)) / (len(e) + len(n) - 2))
            g = (e.mean() - n.mean()) / sp
            se = np.sqrt((len(e) + len(n)) / (len(e) * len(n)) + g * g / (2 * (len(e) + len(n))))
            out[f] = {"effect": float(g), "se": float(se), "frac_subjects_positive": None, "between": True}
            continue
        est = float(np.sum(w * d) / np.sum(w))
        idx = rng.integers(0, len(d), (n_boot, len(d)))
        boot = np.sum(w[idx] * d[idx], axis=1) / np.sum(w[idx], axis=1)
        out[f] = {"effect": est, "se": float(boot.std()), "frac_subjects_positive": float(np.mean(d > 0))}
    return out


def meta(effects):
    """Random-effects (DerSimonian-Laird). effects: list of (est, se)."""
    y = np.array([e for e, _ in effects]); v = np.array([s ** 2 for _, s in effects])
    w = 1 / v
    fixed = np.sum(w * y) / np.sum(w)
    q = np.sum(w * (y - fixed) ** 2)
    k = len(y)
    tau2 = max(0.0, (q - (k - 1)) / (np.sum(w) - np.sum(w ** 2) / np.sum(w))) if k > 1 else 0.0
    wr = 1 / (v + tau2)
    est = np.sum(wr * y) / np.sum(wr); se = np.sqrt(1 / np.sum(wr))
    return {"effect": float(est), "se": float(se), "z": float(est / se), "k": int(k),
            "tau2": float(tau2), "Q": float(q)}


def main(paths, adjust_for=None):
    res = {}
    for p in paths:
        rows = json.loads(Path(p).read_text())
        res[Path(p).stem] = dataset_effects(rows, adjust_for=adjust_for)
    for name, r in res.items():
        print(f"\n{name}: {r['n_awakenings']} NREM awakenings ({r['n_experience']} with experience), "
              f"{r['n_subjects_both']} subjects with both kinds")
        for f in FEATURES:
            if r[f]:
                e = r[f]
                kind = "between-subject" if e.get("between") else f"{e['frac_subjects_positive']:.0%} of subjects positive"
                print(f"   {f:12s} {e['effect']:+.3f} ± {e['se']:.3f}  (z={e['effect']/e['se']:+.2f}; {kind})")
    if len(res) > 1:
        print("\nMeta-analysis across datasets (random effects)")
        res["_meta"] = {}
        for f in FEATURES:
            for label, keep in (("within-subject datasets (primary)", lambda e: not e.get("between")),
                                ("all datasets (secondary)", lambda e: True)):
                eff = [(r[f]["effect"], r[f]["se"]) for k_, r in res.items()
                       if k_ != "_meta" and r.get(f) and keep(r[f])]
                if len(eff) >= 2:
                    m = meta(eff); res["_meta"][f + " | " + label] = m
                    print(f"   {f:12s} {m['effect']:+.3f} ± {m['se']:.3f}  z={m['z']:+.2f}  k={m['k']}  "
                          f"tau2={m['tau2']:.3f}  [{label}]")
    return res


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    adj = next((a.split("=")[1] for a in sys.argv[1:] if a.startswith("--adjust=")), None)
    out = main(args, adjust_for=adj)
