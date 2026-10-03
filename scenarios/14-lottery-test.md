# Scenario 14 — Does wanting tilt chance? A test on real lottery draws

Round 6. **Part 1 written and committed before the data were downloaded.**

## Conjecture

> Something tilts genuinely random physical events toward outcomes that are wanted
> (the "valence-aimed chooser" acting on events outside the brain).

Earlier tests used trivial stakes or computer pseudo-randomness. Lottery draws with
physical ball machines are chaotic physical events (so, by the argument of Scenario 4,
quantum-random at root), with real money wanted by millions of people.

## Part 1 — Prediction, written first

People do not pick lottery numbers evenly. Numbers that can be birthdays (1–31, and
especially 1–12) are chosen far more often. So at every draw, more people are hoping for
low numbers than for high ones.

- **Chooser prediction.** Drawn numbers ≤ 31 occur more often than chance. If the tilt
  is ε per ball, the share of drawn balls ≤ 31 exceeds its chance value by about ε.
- **Null prediction.** The share equals the chance value (31/N for a game with N balls),
  within sampling error.

Data: New York State open data, draw histories for games that use numbers above 31.
Analysis fixed in advance: for each game, the fraction of main-draw balls ≤ 31, compared
with 31/N by a normal approximation (balls within a draw are drawn without replacement,
which makes the true variance slightly smaller, so this is conservative); then a pooled
estimate across games weighted by number of balls. Secondary: the same for ≤ 12.

**Known weaknesses, stated in advance.** Wanting is spread across millions of people
with conflicting numbers, so only the *imbalance* in popularity is tested. Some games
or periods may use computer draws, not balls; those test something weaker. A null
limits only a chooser that acts on external events and adds up across people.

## Part 2 — First result (New York data)

116,394 drawn balls across nine game-periods (Powerball, Mega Millions, NY Lotto,
Take 5, Cash4Life).

| Measure | Excess over chance | z |
|---|---|---|
| Balls ≤ 31 (primary) | +0.26% ± 0.13% | +1.97 |
| Balls ≤ 12 (secondary) | 0.00% ± 0.13% | 0.00 |

The primary measure is borderline in the predicted direction (about a 1-in-20 result by
chance). The secondary measure, where the chooser idea predicts a *larger* effect, shows
nothing. Most of the primary excess comes from two Mega Millions periods.

## Part 1b — Replication, pre-specified before downloading new data

A borderline result calls for an independent sample, not interpretation. Committed
before fetching: the same statistic (share of main balls ≤ 31 vs 31/N, pooled) on
lottery draw histories from **other** operators (Texas Lottery games with numbers above
31, and any other national or state draw history we can download), excluding games
already in the New York files (Powerball, Mega Millions).

- Chooser prediction: excess of about +0.26% again (same sign, similar size).
- Null prediction: excess consistent with zero; combined with New York, z falls.
- We will report the replication sample alone and the combined figure, whatever they are.
