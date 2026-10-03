"""Scenario 1: does a felt-valence architecture beat an automaton?

These simulations model the FUNCTIONAL role of valence (an internal good/bad
signal). They cannot show whether that signal is felt. What they can do is tell
us what evolution demands of such a signal, which constrains what sentience
would have to be if it is the thing doing this job.

Experiments
  A  reflex automaton vs valence learner across environmental volatility
  J  James alignment: does good-feeling track good-for-you when the feeling
     is causal vs when it is epiphenomenal?
  B  many needs: common-currency valence vs modular/priority automata
  C  firewall: what happens if cognition can write to its own valence?
"""
import json
import sys
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

K = 8  # stimulus types
ANCESTRAL = np.array([1.0] * (K // 2) + [-1.0] * (K // 2))


def lifetime(rng, q0, w, learn, effects, T, eps, lr, access=None, causal=True):
    """Run one lifetime for a whole population. Returns fitness per individual."""
    N = q0.shape[0]
    Q = q0.copy()
    fit = np.zeros(N)
    idx = np.arange(N)
    q_self = np.zeros(N)
    stim = rng.integers(0, K, size=(N, T))
    for t in range(T):
        k = stim[:, t]
        qk = Q[idx, k]
        explore = learn & (rng.random(N) < eps)
        approach = (qk > 0) ^ explore
        e = effects[idx, k]
        if access is not None:
            # self-stimulation: a way to get the feeling without the outcome
            avail = rng.random(N) < access
            try_self = avail & learn & ((q_self > qk) | (rng.random(N) < eps))
            approach &= ~try_self
            q_self += lr * try_self * (np.abs(w) - q_self)
        fit += e * approach
        felt = (w if causal else 1.0) * e
        Q[idx, k] += lr * (learn & approach) * (felt - qk)
    return fit


def evolve(v, mode, seed, gens=150, N=300, T=120, cost=3.0, eps=0.05, lr=0.3,
           with_access=False):
    rng = np.random.default_rng(seed)
    q0 = rng.normal(0, 0.1, (N, K))
    w = rng.normal(0, 0.1, N)
    access = np.full(N, 0.5) if with_access else None
    if mode == "reflex":
        learn = np.zeros(N, bool)
    elif mode == "mixed":
        learn = rng.random(N) < 0.5
    else:  # valence, epi
        learn = np.ones(N, bool)
    hist = []
    for g in range(gens):
        resample = rng.random((N, K)) < v
        effects = np.where(resample, rng.choice([-1.0, 1.0], (N, K)), ANCESTRAL)
        fit = lifetime(rng, q0, w, learn, effects, T, eps, lr, access,
                       causal=(mode != "epi"))
        fit = fit - cost * learn
        hist.append((fit.mean() / T, w.mean(), learn.mean(),
                     access.mean() if with_access else 0.0))
        # tournament selection
        a, b = rng.integers(0, N, (2, N))
        win = np.where(fit[a] >= fit[b], a, b)
        q0 = q0[win] + rng.normal(0, 0.05, (N, K))
        w = w[win] + rng.normal(0, 0.05, N)
        learn = learn[win]
        if mode == "mixed":
            learn = learn ^ (rng.random(N) < 0.01)
        if with_access:
            access = np.clip(access[win] + rng.normal(0, 0.03, N), 0, 1)
    h = np.array(hist)
    return {"fitness": h[-20:, 0].mean(), "w": h[-20:, 1].mean(),
            "learners": h[-20:, 2].mean(), "access": h[-20:, 3].mean(),
            "access_curve": h[:, 3].tolist(), "fit_curve": h[:, 0].tolist()}


def exp_A(reps=6):
    rows = []
    for v in [0.0, 0.05, 0.1, 0.2, 0.4, 0.7, 1.0]:
        r = {"v": v}
        for mode in ["reflex", "valence", "mixed"]:
            runs = [evolve(v, mode, s) for s in range(reps)]
            r[mode] = float(np.mean([x["fitness"] for x in runs]))
            if mode == "mixed":
                r["learner_share"] = float(np.mean([x["learners"] for x in runs]))
        rows.append(r)
        print(r, flush=True)
    return rows


def exp_J(reps=40, v=0.4):
    out = {}
    for mode in ["valence", "epi"]:
        ws = [evolve(v, mode, 1000 + s, gens=100)["w"] for s in range(reps)]
        out[mode] = {"aligned_fraction": float(np.mean(np.array(ws) > 0)),
                     "mean_w": float(np.mean(ws)), "sd_w": float(np.std(ws))}
        print(mode, out[mode], flush=True)
    return out


def exp_C(reps=6, v=0.4):
    runs = [evolve(v, "valence", 2000 + s, gens=200, with_access=True) for s in range(reps)]
    curve = np.mean([r["access_curve"] for r in runs], axis=0)
    fit = np.mean([r["fit_curve"] for r in runs], axis=0)
    out = {"access_start": float(curve[0]), "access_end": float(curve[-20:].mean()),
           "fitness_start": float(fit[:5].mean()), "fitness_end": float(fit[-20:].mean()),
           "access_curve": curve.tolist(), "fit_curve": fit.tolist()}
    print({k: v_ for k, v_ in out.items() if "curve" not in k}, flush=True)
    return out


# ---- Experiment B: many needs ------------------------------------------------

def survive(rng, n, policy, params, T=400, trials=1):
    """Population survival time with n needs; one option per need each step."""
    N = params.shape[0]
    decay = 0.85 * 2.0 / (n + 1)
    x = np.full((N, n), 4.0)
    alive = np.ones(N, bool)
    life = np.zeros(N)
    idx = np.arange(N)
    for t in range(T):
        a = rng.random((N, n)) * 2.0
        if policy == "greedy":            # biggest offer, ignores body state
            c = a.argmax(1)
        elif policy == "state":           # most depleted need, ignores offers
            c = x.argmin(1)
        elif policy == "priority":        # fixed-order alarm thresholds, else greedy
            alarm = x < params[:, :n]
            first = np.where(alarm.any(1), alarm.argmax(1), a.argmax(1))
            c = first
        elif policy == "currency":        # one scalar: offer x urgency(state)
            c = (a * np.exp(-params[:, :n] * x)).argmax(1)
        x -= decay
        x[idx, c] += a[idx, c]
        x = np.minimum(x, 8.0)
        alive &= (x > 0).all(1)
        life += alive
    return life


def exp_B(reps=4, gens=80, N=200):
    rows = []
    for n in [2, 3, 5, 8]:
        r = {"needs": n}
        for policy in ["greedy", "state", "priority", "currency"]:
            scores = []
            for s in range(reps):
                rng = np.random.default_rng(3000 + s)
                p = np.abs(rng.normal(1.0, 0.5, (N, n)))
                for g in range(gens):
                    fit = survive(rng, n, policy, p)
                    a, b = rng.integers(0, N, (2, N))
                    win = np.where(fit[a] >= fit[b], a, b)
                    p = np.abs(p[win] + rng.normal(0, 0.1, (N, n)))
                scores.append(survive(rng, n, policy, p).mean())
            r[policy] = float(np.mean(scores))
        rows.append(r)
        print(r, flush=True)
    return rows


if __name__ == "__main__":
    which = sys.argv[1:] or ["A", "J", "B", "C"]
    res = {}
    f = OUT / "valence_evolution.json"
    if f.exists():
        res = json.loads(f.read_text())
    for w_ in which:
        print(f"--- experiment {w_}", flush=True)
        res[w_] = {"A": exp_A, "J": exp_J, "B": exp_B, "C": exp_C}[w_]()
    f.write_text(json.dumps(res, indent=1))
