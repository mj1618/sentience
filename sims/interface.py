"""Scenario 3: is feeling the engine, the teacher, or an interface?

Part 1  Four candidate wirings of valence into behaviour, each run through
        the same battery of laboratory findings (research/04). Which wiring
        reproduces all of them?
Part 2  Why would evolution route the body's values to a planner through
        experienced outcomes? Compare learning speed.

Body valuation L(outcome, body state) is the same in every architecture:
what differs is who gets to read it, and when.
"""
import json
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)


def L(outcome, body):
    """How good an outcome is for the body right now (computed on contact)."""
    if outcome == "food":
        return 2.0 * body["hunger"] - 0.3
    if outcome == "salt":            # intensely salty: foul unless sodium-depleted
        return 3.0 * body["sodium_need"] - 1.5
    if outcome == "shock":
        return -2.0
    return 0.0


HUNGRY = {"hunger": 1.0, "sodium_need": 0.0}
SATED = {"hunger": 0.0, "sodium_need": 0.0}
DEPLETED = {"hunger": 0.5, "sodium_need": 1.0}


class Agent:
    """arch: direct | cached | interface | readout
    direct    one system; action = live body valuation of the expected outcome
    cached    one system; action = stored value of the action/cue itself,
              learned from how its outcomes felt
    interface two systems; automatic one re-values cues live (unfelt), planner
              uses stored outcome values that update only when the outcome is
              experienced and its valuation crosses to the planner (felt)
    readout   two systems; planner can read live body valuation of any
              outcome it thinks of, no experience needed
    """

    def __init__(self, arch):
        self.arch = arch
        self.g = 1.0          # automatic "wanting" gain (dopamine-like)
        self.m = 1.0          # planner self-activation
        self.q = {}           # cached values of actions/cues
        self.u = {}           # planner's stored outcome values
        self.model = {}       # action/cue -> outcome

    def experience(self, outcome, body, via=None):
        v = L(outcome, body)
        if via is not None:
            self.model[via] = outcome
            self.q[via] = v
        self.u[outcome] = v           # what crossed to the planner
        return v

    def cue_approach(self, cue, body):
        """Automatic, cue-triggered approach."""
        if self.arch == "cached":
            return self.g * self.q.get(cue, 0.0)
        return self.g * L(self.model[cue], body)

    def press(self, action, body, prompted=False):
        """Self-initiated instrumental action for an outcome."""
        o = self.model[action]
        drive = 1.0 if prompted else self.m
        if self.arch == "direct":
            return drive * self.g * max(0.0, L(o, body))
        if self.arch == "cached":
            return drive * self.g * max(0.0, self.q.get(action, 0.0))
        if self.arch == "interface":
            return drive * max(0.0, self.u.get(o, 0.0))
        return drive * max(0.0, L(o, body))     # readout

    def consume(self, outcome, body, hidden_bias=0.0):
        """Returns (amount consumed, reported feeling). hidden_bias is a valence
        nudge that never reaches report (subliminal)."""
        v = L(outcome, body)
        if self.arch in ("interface", "readout"):
            return v + hidden_bias, v            # automatic system gets the nudge; report does not
        return v + hidden_bias, v + hidden_bias  # one system: behaviour and report move together


# Each test returns (model value, did it match the laboratory finding?)
def battery(arch):
    r = {}

    a = Agent(arch); a.experience("food", HUNGRY, via="lever")
    trained = a.press("lever", HUNGRY)
    shifted = a.press("lever", SATED)
    r["1a state shift alone leaves lever-pressing unchanged"] = (shifted / trained, shifted / trained > 0.8)
    a.experience("food", SATED)                      # eats it once while sated, away from the lever
    after = a.press("lever", SATED)
    r["1b one taste in the new state then cuts pressing"] = (after / trained, after / trained < 0.3)

    a = Agent(arch); a.experience("salt", HUNGRY, via="salt_cue")
    before = a.cue_approach("salt_cue", HUNGRY)
    flipped = a.cue_approach("salt_cue", DEPLETED)   # never tasted while depleted
    r["2 hated salt cue becomes wanted at once when salt-starved"] = (flipped, before < 0 < flipped)

    a = Agent(arch); a.experience("food", HUNGRY, via="food_cue"); a.g = 0.0
    r["3 dopamine loss: no approach, pleasure reaction intact"] = (
        a.cue_approach("food_cue", HUNGRY), a.cue_approach("food_cue", HUNGRY) == 0 and a.consume("food", HUNGRY)[1] > 0)

    a = Agent(arch); a.experience("food", HUNGRY, via="food_cue"); base = a.cue_approach("food_cue", HUNGRY); a.g = 3.0
    r["4 sensitisation: wanting up, liking unchanged"] = (
        a.cue_approach("food_cue", HUNGRY) / base, a.cue_approach("food_cue", HUNGRY) > 2 * base
        and a.consume("food", HUNGRY)[1] == L("food", HUNGRY))

    a = Agent(arch)
    eat0, rep0 = a.consume("food", HUNGRY); eat1, rep1 = a.consume("food", HUNGRY, hidden_bias=0.5)
    r["5 hidden mood nudge changes consumption, not reported feeling"] = (eat1 - eat0, eat1 > eat0 and rep1 == rep0)

    a = Agent(arch); a.experience("food", HUNGRY, via="lever"); a.experience("food", HUNGRY, via="food_cue"); a.m = 0.0
    r["6 lost self-activation: no spontaneous action, normal when prompted, automatic reactions intact"] = (
        a.press("lever", HUNGRY), a.press("lever", HUNGRY) == 0 and a.press("lever", HUNGRY, prompted=True) > 0
        and a.cue_approach("food_cue", HUNGRY) > 0)
    return r


def part1():
    out = {}
    for arch in ["direct", "cached", "interface", "readout"]:
        res = battery(arch)
        out[arch] = {k: {"value": float(v), "match": bool(ok)} for k, (v, ok) in res.items()}
        print(f"{arch:10s} matches {sum(ok for _, ok in res.values())}/{len(res)}: "
              + " ".join("Y" if ok else "-" for _, ok in res.values()))
    return out


# ---- Part 2: learning speed -------------------------------------------------

def part2(reps=200, T=600, O=6, S=3, tau=60):
    """O outcomes whose value depends on body state (S states, switching every tau
    steps). Each outcome is reachable by M different actions. Reward per step,
    as a fraction of what a perfect chooser gets."""
    rows = []
    for M in [1, 2, 5, 10, 20]:
        acc = {"cached": [], "interface": [], "readout": []}
        for rep in range(reps):
            rng = np.random.default_rng(rep)
            val = rng.normal(0, 1, (S, O))
            a2o = np.repeat(np.arange(O), M)
            for arch in acc:
                Q = np.zeros((S, O * M)); U = np.zeros((S, O)); tot = 0.0; best = 0.0
                for t in range(T):
                    s = (t // tau) % S
                    if arch == "readout":
                        a = int(val[s].argmax()) * M
                    elif rng.random() < 0.1:
                        a = int(rng.integers(O * M))
                    elif arch == "cached":
                        a = int(Q[s].argmax())
                    else:
                        a = int(U[s].argmax()) * M
                    r = val[s, a2o[a]] + rng.normal(0, 0.3)
                    Q[s, a] += 0.5 * (r - Q[s, a])
                    U[s, a2o[a]] += 0.5 * (r - U[s, a2o[a]])
                    tot += val[s, a2o[a]]; best += val[s].max()
                acc[arch].append(tot / best)
        row = {"routes_per_outcome": M, **{k: float(np.mean(v)) for k, v in acc.items()}}
        rows.append(row); print(row)
    return rows


if __name__ == "__main__":
    res = {"battery": part1(), "speed": part2()}
    (OUT / "interface.json").write_text(json.dumps(res, indent=1))
