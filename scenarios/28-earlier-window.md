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
