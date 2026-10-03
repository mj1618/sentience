"""Scenario 3b: how vivid should imagined feelings be?

A planner that can preview how an outcome would feel (imagination) chooses
better. But a preview that feels as good as the real thing is a free reward:
the animal can daydream instead of act. Evolve preview fidelity f in [0,1].

Each step: O options with true body value val. Planner previews each as
f*val + noise and picks the best. It then either pursues it (feels val - effort,
gains fitness val - effort) or daydreams (feels f*val, gains nothing), choosing
whichever has felt better on average so far.
"""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "out"


def lifetime(rng, f, effort, T=300, O=6, sigma=0.3, eps=0.1, lr=0.1):
    N = f.shape[0]
    idx = np.arange(N)
    r_real = np.zeros(N); r_dream = np.zeros(N)
    fit = np.zeros(N); dreamt = np.zeros(N)
    for t in range(T):
        val = rng.normal(0, 1, (N, O))
        preview = f[:, None] * val + rng.normal(0, sigma, (N, O))
        v = val[idx, preview.argmax(1)]
        dream = np.where(rng.random(N) < eps, rng.random(N) < 0.5, r_dream > r_real)
        felt_real = v - effort
        felt_dream = f * v
        fit += np.where(dream, 0.0, felt_real)
        dreamt += dream
        r_real += lr * (~dream) * (felt_real - r_real)
        r_dream += lr * dream * (felt_dream - r_dream)
    return fit / T, dreamt / T


def evolve(effort, seed, gens=150, N=300):
    rng = np.random.default_rng(seed)
    f = rng.random(N)
    for g in range(gens):
        fit, _ = lifetime(rng, f, effort)
        a, b = rng.integers(0, N, (2, N))
        f = np.clip(f[np.where(fit[a] >= fit[b], a, b)] + rng.normal(0, 0.03, N), 0, 1)
    fit, dreamt = lifetime(rng, f, effort)
    return f.mean(), fit.mean(), dreamt.mean()


def landscape(effort, seed=0):
    """Fitness of fixed-f populations, to see the shape of the trade-off."""
    rng = np.random.default_rng(seed)
    rows = []
    for fv in np.linspace(0, 1, 11):
        fit, dreamt = lifetime(rng, np.full(2000, fv), effort)
        rows.append({"f": float(fv), "fitness": float(fit.mean()), "daydream_share": float(dreamt.mean())})
    return rows


if __name__ == "__main__":
    res = {"evolved": [], "landscape": {}}
    for effort in [0.1, 0.3, 0.6, 0.9]:
        runs = [evolve(effort, s) for s in range(5)]
        f, fit, d = np.mean(runs, axis=0)
        row = {"effort": effort, "evolved_fidelity": float(f), "fitness": float(fit), "daydream_share": float(d)}
        res["evolved"].append(row); print(row)
        res["landscape"][str(effort)] = landscape(effort)
    for r in res["landscape"]["0.3"]:
        print(r)
    (OUT / "imagination.json").write_text(json.dumps(res, indent=1))
