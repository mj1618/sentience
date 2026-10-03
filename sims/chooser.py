"""Scenario 4: a field that chooses instead of pushes.

Suppose something biases which way equal-energy quantum events fall, by a
small amount delta (probability 0.5 -> 0.5 + delta). No force, no energy.

  1  How big must delta be to change a decision, if every relevant event is
     nudged the right way?
  2  How many observations would it take to notice delta, and what is the
     thermodynamic cost of the choosing?
  3  The targeting problem: the brain is chaotic. How far ahead of a decision
     can a chooser act and still steer it, and what must it know?
"""
import json
from math import erf, log, sqrt
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "out"
KT = 1.380649e-23 * 310


def phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


def needed_bias():
    """Decision = which of two pools has more of N micro-events 'on'.
    Bias delta on a fraction f of events, toward one option.
    z = 2*sqrt(2)*f*delta*sqrt(N); P(choice) = Phi(z)."""
    rows = []
    for label, N in [("one neuron near threshold", 1e4),
                     ("small circuit, 100 ms", 1e8),
                     ("whole-brain decision, 1 s", 1e15)]:
        for f in [1.0, 1e-3]:
            d75 = 0.674 / (2 * sqrt(2) * f * sqrt(N))
            rows.append({"system": label, "events": N, "fraction_targeted": f,
                         "bias_for_75_percent": min(d75, 0.5)})
    return rows


def detection_and_cost():
    rows = []
    for d in [1e-2, 1e-3, 1e-4, 1e-6, 1e-8]:
        n5 = (5 / (2 * d)) ** 2                    # events to see it at 5 sigma
        bits = 2 * d * d / log(2)                  # information per event (KL, bits)
        watts = 1e18 * 2 * d * d * KT              # 1e18 events/s brain-wide, kT per nat
        rows.append({"bias": d, "events_to_detect_5sigma": n5,
                     "bits_per_event": bits, "entropy_cost_watts_whole_brain": watts})
    return rows


def chaos(trials=3000, N=200, g=2.0, beta=1.5, delta=0.05, seed=0):
    """Random recurrent network of noisy binary units (chaotic for g>1).
    Goal: make readout w.x positive at time T. The chooser nudges every unit's
    coin once, tau steps before the decision.
      naive   nudges toward the readout pattern itself (knows only the goal)
      linear  nudges toward the pattern propagated back through the wiring
              (knows the wiring, linear approximation)
    Returns P(goal) for each; 0.5 = no steering."""
    rng = np.random.default_rng(seed)
    J = rng.normal(0, g / sqrt(N), (N, N))
    w = rng.normal(0, 1, N)
    out = []
    for tau in [0, 1, 2, 3, 5, 8]:
        back = w.copy()
        for _ in range(tau):
            back = J.T @ back
        res = {"lead_steps": tau}
        for mode in ["naive", "linear"]:
            hits = 0
            for tr in range(trials):
                r = np.random.default_rng(10_000 + tr)
                x = np.sign(r.normal(size=N))
                for _ in range(5):                                   # settle
                    x = np.where(r.random(N) < 1 / (1 + np.exp(-2 * beta * (J @ x))), 1.0, -1.0)
                p = 1 / (1 + np.exp(-2 * beta * (J @ x)))
                u = r.random(N)
                noise = r.random((tau, N))

                def run(direction):
                    y = np.where(u < np.clip(p + delta * direction, 0, 1), 1.0, -1.0)
                    for k in range(tau):
                        y = np.where(noise[k] < 1 / (1 + np.exp(-2 * beta * (J @ y))), 1.0, -1.0)
                    return w @ y

                if mode == "naive":
                    val = run(np.sign(w))
                else:
                    val = run(np.sign(back))
                hits += val > 0
            res[mode] = float(hits / trials)
        out.append(res)
        print(res)
    return out


if __name__ == "__main__":
    res = {"needed_bias": needed_bias(), "detection": detection_and_cost()}
    for r in res["needed_bias"]:
        print(r)
    for r in res["detection"]:
        print(r)
    res["chaos"] = chaos()
    (OUT / "chooser.json").write_text(json.dumps(res, indent=1))
