# Scenario 27 — Study 5: is the experience-related difference at the front or the back of the head?

Round 14. **Plan committed before the whole-scalp features were related to reports in any
dataset.** What we already knew is stated below.

## Why

The sharpest live dispute among theories of consciousness is anatomical. One camp
(integrated information; the "posterior hot zone") says experience depends on the back
of the cortex. Another (global workspace; higher-order theories) says the front is
essential. In sleep, the published claim is that experience goes with *less slow-wave
activity at the back of the head*. The round 13 studies used eleven scalp sites and an
average reference over those sites, which ties front and back together arithmetically and
cannot say where an effect is. This study uses every scalp channel a dataset has.

## Data

- **Estimation sets** (we have already seen eleven-site results from these): Tononi
  serial awakenings (up to 257 channels), Zhang & Wamsley (58), Noreika DATA1 (25).
- **Confirmation set, untouched:** Kumral et al. 2023 (128 channels, 19 people, 66
  awakenings), still downloading at this commit, not opened.
- Not used: "Multiple awakenings" (its recordings run past the awakening); the two Aamodt
  sets (too few people with both kinds of report).

## Measures (fixed; code `sims/dream_topo.py`)

Window −22 s to −2 s. All scalp channels with a known position; channels that are flat
or exceed 500 microvolts are dropped, and the recording is excluded if more than 30% are;
average reference over the remaining channels. Frontal region: channels in the front
third of the head; posterior region: channels in the back third.

`front_delta`, `post_delta`: log slow-wave power (1–4 Hz) in each region.
`grad_delta` = posterior minus frontal. The same three for fast activity (20–30 Hz):
`front_hf`, `post_hf`, `grad_hf`.

## Analysis (fixed)

As in Study 1: N2 and N3 awakenings, "experience" against "no experience", normal scores
within dataset, contrast within subject and stage, permutation within cells, datasets
with at least 8 subjects contributing both kinds.

## What each camp predicts

| | Posterior camp | Frontal camp |
|---|---|---|
| `post_delta` with experience | lower | no commitment |
| `grad_delta` (back minus front) | lower: the reduction is specific to the back | not lower: any reduction is at least as large at the front |
| `post_hf` | higher | no commitment |
| `front_hf` | no commitment | higher |
| `grad_hf` | higher | not higher |

## Decision rules

1. **Estimation** (three sets): effects and intervals are reported for all six measures.
   No confirmatory claim is made from these, because we have seen related results in
   them (eleven-site posterior slow-wave effect in the Tononi set about −0.33; a reviewer's
   dense posterior cluster −0.38; whole-scalp −0.29).
2. **Confirmation** (Kumral): before opening it, we will commit a short amendment naming
   at most two directional predictions taken from the estimation results. Each is
   **supported** at one-sided p < 0.025 in the Kumral data alone, if at least 8 subjects
   there contribute both kinds of report; otherwise the confirmation is reported as
   **not possible**.
3. A result is called a difference between front and back only on `grad_delta` or
   `grad_hf`, never on a comparison of two separate tests.

## Known weaknesses

Scalp position is a poor guide to where in the brain a signal comes from. Fast activity
at the scalp is contaminated by muscle, more so at the front and edges. The estimation
sets come from three laboratories with different equipment. "No experience" may include
forgetting.

## Part 2 — Estimation result (three laboratories; 522 awakenings; 64 people with both kinds of report)

| Measure | Combined effect (95% interval) | p | Tononi / Zhang / Noreika |
|---|---|---|---|
| `front_delta` | −0.18 (−0.38 to +0.02) | 0.08 | −0.17 / −0.51 / −0.05 |
| `post_delta` | −0.17 (−0.37 to +0.03) | 0.10 | −0.23 / −0.39 / +0.01 |
| `grad_delta` (back minus front) | +0.04 (−0.17 to +0.25) | 0.71 | −0.16 / +0.34 / +0.21 |
| `front_hf` | +0.18 (−0.03 to +0.39) | 0.10 | +0.23 / +0.16 / +0.09 |
| `post_hf` | +0.16 (−0.05 to +0.37) | 0.13 | +0.31 / +0.10 / −0.04 |
| `grad_hf` | −0.14 (−0.35 to +0.06) | 0.18 | −0.03 / −0.48 / −0.15 |

Effects are in within-person standard-deviation units; intervals from the permutation
null. Nothing is individually significant. Reading, to be reviewed: slow-wave power tends
to be lower and fast activity higher before reports of experience, by about the same
small amount at the front and at the back; there is no sign that the difference is
specific to the back of the head.

## Amendment 1 — predictions for the untouched confirmation set, committed before it was opened

From the table above, two directional predictions for the Kumral data:

1. `post_delta` is lower before reports of experience.
2. `front_delta` is lower before reports of experience.

Each is supported at one-sided p < 0.025 in that dataset alone, provided at least 8
people there contribute both kinds of report. The download (46 GB) was about 2% complete
at this commit and the archive had not been opened.
