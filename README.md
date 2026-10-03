# Sentience

Where does sentience (raw feeling: pain, pleasure, hunger — that something feels like
anything at all) come from? Working hypothesis from the owner: **consciousness =
sentience + thought**, sentience being the motivator and thought working out how to
satisfy it. If so, the hard question is sentience alone.

## Method

1. **Compile** what is known → `research/` (every claim tagged verified / recalled).
2. **Conjecture and test**: propose an answer, then stress-test it → `scenarios/` (argument + simulation or calculation) to find
   constraints that make theories more or less likely.
3. **Red-team**: a fresh reviewer tries to break each conclusion → `reviews/`. Nothing is
   treated as reliable until it has survived this.
4. **Record** what moved → `LEDGER.md` (constraints, credences, open questions).
5. **Report** in plain language → `updates/` (HTML pages, no background assumed).

## Layout

| Path | What |
|---|---|
| `LEDGER.md` | Running list of constraints, theory scores, next scenarios |
| `research/` | Literature briefs with sources |
| `scenarios/` | One file per stress test |
| `sims/` | Code; results in `sims/out/` |
| `updates/` | Plain-language progress pages |

Run: `.venv/bin/python sims/valence_evolution.py` and `.venv/bin/python sims/field_constraints.py`.

## Standing caveat

Simulations here model what a feeling-like signal *does*. None can show that anything is
felt. Their use is to pin down what sentience would have to be like, and to rule out
stories that don't fit.
