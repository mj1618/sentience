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

## Part 3 — Replication result (Texas data)

72,851 drawn balls (Lotto Texas, Cash Five, Texas Two Step; years in which a game's
number range changed were dropped).

| Sample | Balls | Excess of ≤ 31 over chance | z | Excess of ≤ 12 | z |
|---|---|---|---|---|---|
| New York (first) | 116,394 | +0.26% ± 0.13% | +1.97 | 0.00% ± 0.13% | 0.00 |
| Texas (replication) | 72,851 | +0.04% ± 0.15% | +0.30 | +0.04% ± 0.17% | +0.24 |
| Combined | 189,245 | +0.18% ± 0.10% | +1.79 | +0.02% ± 0.10% | +0.15 |

**Reading (ours; to be reviewed).** The borderline New York result did not replicate.
Combined, the excess is not statistically significant and the secondary measure is flat.
The data are compatible with no tilt and rule out a tilt larger than about 0.4% toward
popular numbers. A tilt of the size first seen (0.26%) is not excluded.

**What this does and does not test.** It tests a chooser that acts on physical events
outside the body and adds up across many people's wants. It does not test a chooser
confined to events inside one brain. Whether every game used mechanical ball machines
throughout has not been verified.

Code: `sims/lottery.py`; data: `data/`.

## Part 4 — Review, and a third sample pre-specified before analysis

Reviewer (`reviews/round6-lottery-redteam.md`) recomputed with the exact variance:
New York +0.26% (z = +2.06), Texas +0.04% (z = +0.32), combined +0.18% ± 0.09%
(z = +1.87). Corrections accepted: "did not replicate" is too strong, since Texas was
too small to confirm or exclude the New York figure; the excess is uneven across games;
and it has the wrong shape for a wanting-driven tilt (nothing for 1–12, nothing for 7,
no rise on higher-sales days). The reviewer's own after-the-fact split found the excess
concentrated in games with 44 or more numbers (+0.47% ± 0.18%, z = +2.71) and absent in
smaller games. That split was not planned, so it is a lead, not evidence.

**Third sample, committed before any statistic was computed:** the complete archive of
the German national lottery "6 aus 49" (49 numbers, six main balls per draw, from 1955;
file `data/de_lotto.json`, of which we have looked only at the first few rows to learn
the format). Same statistic: share of main balls ≤ 31 against 31/49, exact
(without-replacement) variance. Secondary: ≤ 12.

- If the large-drum lead is real: excess near +0.47%.
- If it was a fluke of slicing: excess consistent with zero.
- Power is limited (we expect a standard error near 0.25%), so a result between the two
  will be reported as undecided.

## Part 5 — Third sample result (German 6 aus 49)

5,050 draws, 30,300 balls, 1955–2026.

| Measure | Excess over chance | z |
|---|---|---|
| Balls ≤ 31 | −0.04% ± 0.26% | −0.17 |
| Balls ≤ 12 | +0.35% ± 0.23% | +1.48 |

No excess of numbers ≤ 31. The result sits about 1.6 standard errors below the
"large-drum" lead of +0.47%, and is fully consistent with zero. By the rule set in
advance this counts as **not supporting the lead, without excluding it**.

All three samples combined (inverse-variance): ≤ 31 excess +0.15% ± 0.09% (z ≈ +1.7).
Large-drum games only, all samples: +0.31% ± 0.15% (z ≈ +2.1); this subset was chosen
after seeing data, so its z overstates the evidence.

## Where this stands

- Three samples, about 220,000 balls. The first was borderline; the two that followed
  showed nothing.
- The pattern has the wrong shape for a tilt driven by what people want: no excess for
  the most-chosen numbers (1–12, or 7), no increase on bigger-sales days.
- **Verdict (reviewer's wording, adapted): suggestive at most, not established, and
  weakening with each new sample.** A tilt smaller than roughly 0.4% of balls is not
  excluded.
- What would settle it: a large fresh sample with per-draw ticket sales, testing whether
  any excess grows with the number of people wanting it.
