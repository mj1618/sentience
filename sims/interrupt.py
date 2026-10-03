"""Scenario 6: is feeling an interrupt signal?

A planner that does one thing at a time is working through a chunk of a task
(length Lc steps, paid only on completion, rate rho per step). An event turns
up with stake v, handling time h, and slack s (steps before it is too late to
start). Interrupting mid-chunk throws away the progress g made so far.

What should the "break in now" signal depend on? We compare signals that see
different things, each with its threshold tuned as well as it can be:

  value      sees only the stake v
  urgency    sees only how little slack is left
  value/slack  sees stake divided by slack (a common "urgency" heuristic)
  full       sees stake, slack, progress and time left in the chunk (optimal)

Opponents are tuned by grid search so no rule is handicapped (round 2 lesson).
"""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "out"


def payoff(interrupt_now, v, g, s, Lc, h, rho):
    """Net gain relative to ignoring the event. If the agent does not interrupt
    now it handles the event at the chunk boundary when that comes in time and
    is worth it; otherwise the event is lost."""
    rem = Lc - g
    worth = v - h * rho
    wait_ok = rem <= s
    later = np.where(wait_ok, np.maximum(worth, 0.0), 0.0)
    now = worth - g * rho
    return np.where(interrupt_now, now, later)


def run(Lc=10, h=2, rho=1.0, mean_v=6.0, max_s=15, n=200_000, seed=0):
    rng = np.random.default_rng(seed)
    v = rng.exponential(mean_v, n)
    g = rng.integers(0, Lc, n)
    s = rng.integers(0, max_s + 1, n)
    rem = Lc - g
    res = {}
    # optimal
    opt = (rem > s) & (v - h * rho - g * rho > 0)
    res["full"] = payoff(opt, v, g, s, Lc, h, rho).mean()
    # value-only threshold
    res["value"] = max(payoff(v > th, v, g, s, Lc, h, rho).mean() for th in np.linspace(0, 40, 81))
    # urgency-only
    res["urgency"] = max(payoff(s <= th, v, g, s, Lc, h, rho).mean() for th in range(-1, max_s + 1))
    # value / slack
    res["value/slack"] = max(payoff(v / (s + 1) > th, v, g, s, Lc, h, rho).mean() for th in np.linspace(0, 40, 161))
    # stake and slack but blind to own progress (two thresholds)
    res["value+slack"] = max(payoff((v > a) & (s <= b), v, g, s, Lc, h, rho).mean()
                             for a in np.linspace(0, 30, 31) for b in range(-1, max_s + 1))
    res["never"] = payoff(np.zeros(n, bool), v, g, s, Lc, h, rho).mean()
    return {k: float(x) for k, x in res.items()}


if __name__ == "__main__":
    out = []
    for Lc in [2, 5, 10, 20]:
        for mean_v in [3.0, 6.0, 15.0]:
            r = run(Lc=Lc, mean_v=mean_v)
            row = {"chunk": Lc, "mean_stake": mean_v, **{k: round(x / r["full"], 3) for k, x in r.items()}}
            out.append(row)
            print(row)
    (OUT / "interrupt.json").write_text(json.dumps(out, indent=1))
