# Scenario 28 — Study 6: does slow-wave activity half a minute before waking go with reported experience?

Round 14. **Pre-registration, committed before the measure was computed on any of the
confirmation recordings.**

## Where the idea came from

In reviewing Study 5, an independent reviewer found, after the fact, that whole-scalp
slow-wave power was lower before reports of experience by about 0.29 within-person
standard deviations when measured 34 to 14 seconds before waking, against about 0.18 in
the last 20 seconds (three datasets: Tononi, Zhang & Wamsley, Noreika; p near 0.007,
uncorrected, one of several things tried). A result found that way is a lead. This study
tests it once, on recordings that played no part in finding it.

## Data (none used in Study 5)

- De Gennaro "Multiple awakenings" (19 people, yes/no report; recordings run past the
  awakening, so the awakening has to be located).
- Aamodt evening sleep and Aamodt morning sleep.
- Kumral et al. 2023, if the download completes and verifies (unopened at this commit).

What we had already seen of these: eleven-site results for the first three in Study 1
(nothing notable); and, from the Study 1 reviewer, that shifting the window 40 seconds
earlier in the Multiple-awakenings set moved the eleven-site posterior slow-wave estimate
from −0.07 to −0.15 in a three-dataset pool (p = 0.09).

## Measure (fixed)

- **Locating the awakening.** Where a chin-muscle channel exists: amplitude (20–100 Hz)
  in 1-second steps over the last 60 s; baseline = median of the first 20 of those
  seconds; awakening = the first second in the last 40 s exceeding three times baseline.
  If there is none, or no muscle channel, the end of the file is used.
- **`delta_early`:** mean log power at 1–4 Hz over all good scalp channels (average
  reference; channels flat or above 500 microvolts dropped; recording excluded if more
  than 30% are), in the window from 34 s to 14 s before the located awakening.

## Analysis (fixed)

N2 and N3 awakenings answered "experience" or "no experience"; normal scores within
dataset; differences within subject and sleep stage; all such cells from all datasets
pooled with the usual weights; 10,000 permutations within cells.

**Prediction:** `delta_early` is lower before reports of experience.
**Supported** if the pooled effect is negative with two-sided p < 0.05.
**Contradicted** if positive with p < 0.05. Otherwise **not confirmed**, and the interval
is reported.

For comparison only (not a test): the same measure in the last 20 s before the located
awakening.

## Known weaknesses

The largest dataset has a bare yes/no answer and its awakening has to be estimated. Few
"no experience" reports in the Aamodt sets. If the Kumral data cannot be included, that
will be said. The reviewer's estimate suggests modest power: this could fail to confirm a
real effect.

## Interim record (2026-10-04, before the Kumral archive was opened)

Run once, as written above, on the three datasets already on disk
(`sims/dream_early.py`; 452 N2/N3 awakenings; 29 subject-by-stage cells with both kinds
of report):

| | pooled effect | 95% range | p | Multiple awakenings | Aamodt evening | Aamodt morning |
|---|---|---|---|---|---|---|
| `delta_early` (34–14 s before) | −0.26 | −0.52 to −0.00 | 0.046 | −0.23 (19 cells) | −0.87 (6) | −0.17 (4) |
| last 20 s (comparison only) | −0.01 | −0.26 to +0.24 | 0.95 | +0.07 | −0.27 | −1.11 |

Awakening located by the muscle rule in 257 of 277 Multiple-awakenings recordings, and in
15 of 175 Aamodt recordings (the rest use the end of the file, as the plan says).

**This is not yet the registered result.** The plan includes the Kumral data if it
verifies; it is still downloading and has not been opened. The registered test is the
pooled one including Kumral, run once with this same code. The three-dataset figure is
recorded here so that it cannot quietly be preferred later if the two differ.

## Review of the interim result (2026-10-04)

Reproduced independently (`reviews/round14-study6-interim-redteam.md`). Borderline and
fragile; after-the-fact checks suggest the difference is in all frequency bands, not slow
waves in particular, and shrinks once time of night is accounted for.

## Amendment 1 (2026-10-04, before the Kumral archive is opened)

The registered primary test is unchanged. Three secondary analyses are added, to be run
on the Kumral data alone (the only recordings not yet seen), same window, same
within-cell statistics, each two-sided:

- **S1 `rel_delta`:** log 1–4 Hz power minus log 4–40 Hz power.
- **S2 `broad`:** log 4–40 Hz power.
- **S3:** `delta_early` after removing, within cell, its straight-line relation to clock
  time of awakening (or awakening order if no clock time is given; skipped and said so if
  neither exists).

Two accounts, written before looking:

- *Slow-wave account* (local slow waves switch experience off): `rel_delta` lower with
  experience; `delta_early` survives S3 with at least half its unadjusted size.
- *Whole-state / time-of-night account* (experience reports are simply commoner in
  lighter, later sleep): `broad` lower with experience, `rel_delta` near zero, and
  `delta_early` loses more than half its size in S3.

Also reported for Kumral, because the reviewer showed the awakening-location rule matters:
`delta_early` with the file end used for every recording. Kumral's own eligibility under
the Study 1 rule (at least 8 subjects with both kinds of report) will be stated.
