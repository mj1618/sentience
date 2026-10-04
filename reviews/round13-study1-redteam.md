# Round 13 red-team — Study 1 (Scenario 23) confirmation run

Scripts and outputs: `/tmp/s1redteam/`. No repo file was modified. Everything marked
*post hoc* was done after the outcome was known and is exploratory.

**Bottom line.** The numbers reproduce exactly and no re-analysis changes the null. But one
of the three primary datasets ("multi") was analysed in the wrong window: its files run on
past the awakening. With three eligible datasets the plan allows no confirmatory claim in
either direction. Correct label: **inconclusive, not confirmatory**; not "no effect".

## Findings

| # | Claim / issue | Verdict | Evidence | Sev. | Fix |
|---|---|---|---|---|---|
| 1 | Combined effects and p-values | HOLDS | Re-run (seed 0, 10,000 permutations) is identical to `study1_confirmation.json` to every digit (Table A). | – | – |
| 2 | Features computed as defined | HOLDS | Own implementation, 30 random awakenings per dataset: `post_delta` Pearson r 0.993–0.996; `lz` r = 1.0000. Checks arithmetic, not window placement (see 3). | – | – |
| 3 | "Last 20 s before awakening" in multi | **BROKEN** | Multi files do not end at the awakening. Chin EMG (20–100 Hz) rises about ten-fold (median +0.9 log10 in N2, +1.2 in REM) starting a median 16–18 s before file end; onset earlier than −2 s in 341/455 files (75%). No such rise in Noreika or Aamodt (EMG flat ±0.03); Tononi only in the final second, inside the 2 s skip. | critical | End the multi window at EMG onset; label post hoc. |
| 4 | 154/455 multi exclusions | explained | Not units (median-site peak-to-peak 182 µV vs Noreika 174, both mastoid-referenced). 72 of 154 exceed 2,000 µV; 42 are a single site. They are awakening movement artefacts: ending the window at EMG onset cuts NREM exclusions from 86/277 (31%) to 13/277 (5%). Exclusion as executed: no-experience 33/91 (36%) vs experience 53/186 (28%), Fisher p = 0.21. | high | As 3. |
| 5 | Conclusions robust to the amplitude rule | HOLDS | Table B. Smallest p in any variant 0.087 (threshold 0.006). | – | Report Table B as post hoc. |
| 6 | ≥4 within-subject datasets required | **BROKEN** (rule not met) | k = 3 (Tononi 37, multi 15, Noreika 9 subjects with both; Aamodt 6 and 4). The plan permits no confirmatory claim, positive or negative. | high | Say so first. |
| 7 | Hartung–Knapp interval | WEAKENED | With k = 3 the multiplier is t(2) = 4.30; intervals span ±0.35 to ±0.75, so "not supported" was unreachable. | medium | Add the fixed-effect interval (Table A). |
| 8 | Positive control | WEAKENED | Tononi (N2 only) and both Aamodt sets give no control. `irr`: multi −0.36, Noreika −0.91 — wrong sign against development (+0.61). `fp_lag`: −0.24 and +1.22. `post_hf`: −0.32 and +2.31. `post_delta` and `lz` pass (−1.60/−6.85; +0.86/+2.92). The multi control is itself wake-contaminated; no rule for combining datasets. | high | Label `irr`, `irr_adj`, `fp_lag`, `fp_lag_adj` nulls uninformative; `post_hf` doubtful. |
| 9 | Amendment trail | HOLDS (unverifiable) | Analysis code unchanged since 10:11 (Amendment 1). Amendments 2–4 (11:33:16, 11:34:40, 11:41:52) alter label parsing only (diff checked). The outcome file is stamped 11:43:50 and was committed 11:45:36 (362419a). Nothing contradicts the claim; git cannot prove no interactive look. Oddity: the Amendment 3 commit holds a 240-row `tononi.json`; the 271-row file was written 18 s later. | low | – |
| 10 | Other departures | WEAKENED | (a) Reviewer's ≥90% coverage floor silently dropped and not listed under "not done"; multi coverage 66%. (b) Kumral 2023 not added, no note. (c) `fp_lag_orig` computed, never reported. (d) REM secondary has k = 1; "without recall" k = 2. | medium | List in the write-up. |
| 11 | Experience and stage coding | HOLDS, with caveats | All five READMEs: 2 = experience, 1 = without recall, 0 = none; stages 0/1/2/3/5. Negative codes correctly dropped. No missing files. Subject IDs map one-to-one to filename prefixes in every dataset. Caveats: multi is a yes/no report with no content and no "without recall" category; multi pools 2 nights and Noreika 4 per subject; Aamodt files are ICA-cleaned with marked bad segments the pipeline ignores. | low | State caveats. |
| 12 | "The null reflects an insensitive 5-site measure" | not supported | Table C: a 23-channel posterior cluster, full-head average reference, gives dz −0.38 against −0.33. Slightly, not clearly, larger. | medium | Say the Tononi data show a small effect in the published direction that does not reach threshold at the scalp. |
| 13 | Development effects replicated? | No | `lz` +0.53 → +0.05 (upper limit +0.24); `fp_lag` +0.53 → +0.09 (upper limit +0.28). The development–confirmation difference is itself not significant (z = 1.6, 1.3). | – | "Did not replicate", not "refuted". |

## Table A — as executed (reproduced), with fixed-effect interval

Interval = estimate ± 1.96 × SD of the permutation null (SD 0.097–0.101). It assumes one
common effect and takes the multi data at face value.

| Test | Combined | p | 95% fixed-effect | Hartung–Knapp | Tononi / multi / Noreika |
|---|---|---|---|---|---|
| post_delta | −0.066 | 0.495 | −0.26, +0.12 | −0.41, +0.34 | −0.17 / +0.11 / −0.08 |
| post_hf | −0.015 | 0.876 | −0.21, +0.18 | −0.72, +0.70 | +0.24 / −0.37 / −0.06 |
| lz | +0.050 | 0.604 | −0.14, +0.24 | −0.56, +0.59 | +0.20 / −0.22 / +0.08 |
| lz_adj | +0.063 | 0.514 | −0.13, +0.25 | −0.30, +0.43 | +0.04 / +0.08 / +0.08 |
| irr | −0.161 | 0.104 | −0.35, +0.03 | −0.48, +0.19 | −0.24 / −0.17 / −0.03 |
| irr_adj | −0.158 | 0.110 | −0.35, +0.04 | −0.47, +0.20 | −0.23 / −0.18 / −0.02 |
| fp_lag | +0.089 | 0.374 | −0.10, +0.28 | −0.50, +0.79 | −0.03 / +0.38 / −0.01 |
| fp_lag_adj | +0.075 | 0.443 | −0.12, +0.27 | −0.62, +0.88 | −0.08 / +0.40 / −0.01 |

Every interval of either kind includes 0.2 in one direction, so "inconclusive" is the right
pre-registered label for all eight. The fixed-effect intervals exclude magnitudes above
about 0.35. Minimum detectable effect (80% power, α = 0.006): 0.35, as planned.

## Table B — post hoc sensitivity (combined effect, p; 2,000 permutations)

| Variant | multi NREM n | post_delta | post_hf | lz | irr | fp_lag |
|---|---|---|---|---|---|---|
| As executed | 191 | −0.07, .51 | −0.02, .87 | +0.05, .60 | −0.16, .11 | +0.09, .37 |
| 1,000 µV | 219 | −0.05, .57 | −0.08, .39 | −0.00, .97 | −0.11, .24 | +0.13, .17 |
| 500 µV after re-referencing | 197 | −0.07, .49 | −0.04, .69 | +0.03, .76 | −0.14, .14 | +0.11, .26 |
| No amplitude rule | 277 | −0.06, .51 | −0.06, .48 | +0.01, .89 | −0.05, .60 | +0.08, .37 |
| Drop sites above 500 µV | 241 | −0.01, .88 | −0.04, .71 | −0.03, .74 | −0.11, .20 | +0.06, .49 |
| **Multi window ended at EMG onset** | 264 | −0.11, .20 | +0.10, .27 | +0.11, .22 | −0.09, .30 | +0.09, .35 |
| Multi window 40 s earlier | 275 | −0.15, .09 | −0.03, .75 | +0.06, .50 | −0.13, .16 | +0.05, .60 |
| Multi removed (k = 2) | – | −0.13, .24 | +0.12, .32 | +0.15, .17 | −0.16, .17 | −0.02, .83 |

Adjusted measures: no p below 0.10 in any variant. With the multi window corrected,
`post_delta` is −0.17 / −0.08 / −0.08 (interval −0.29 to +0.06) and multi's `post_hf` and
`lz` change sign (−0.37 → +0.06; −0.22 → +0.04).

## Table C — Tononi dense posterior check (post hoc, exploratory)

Channels within 4 cm of Pz, POz or Oz (23 channels); reference = mean of all good channels
(median 250); window −22 to −2 s; log10 power 1–4 Hz; subject-level experience minus
no-experience; 10,000 within-subject permutations.

| Measure | Subjects | Awakenings | Difference | dz | p |
|---|---|---|---|---|---|
| Stored 5-site | 37 | 215 | −0.071 | −0.33 | 0.074 |
| 5-site, full-head reference | 37 | 215 | −0.073 | −0.36 | 0.042 |
| Dense cluster, same awakenings | 37 | 215 | −0.078 | −0.38 | 0.032 |
| Dense cluster, all usable | 39 | 231 | −0.076 | −0.38 | 0.031 |
| Whole-scalp mean | 39 | 231 | −0.061 | −0.29 | 0.096 |
| Dense cluster, 20–30 Hz | 39 | 231 | +0.043 | +0.40 | 0.028 |

Published direction, small size, uncorrected. Correlation of dense with stored: 0.96.

## What cannot be claimed

That the measures are unrelated to experience; anything about generalisation across
laboratories; anything from the `irr` or `fp_lag` nulls; that the posterior slow-wave
finding failed to replicate.

## Sentences the authors may quote

1. "None of our eight pre-registered tests found a reliable link between an EEG measure and reported experience in non-REM sleep: the smallest p-value was 0.10 against a threshold of 0.006."
2. "Only three of the five confirmation datasets had enough participants (585 awakenings from 61 people), fewer than the four our plan required, so by our own rules this is not a confirmatory result in either direction."
3. "The result is inconclusive, not evidence of no effect: assuming one common effect, differences larger than about 0.35 standard deviations are unlikely, but a difference of 0.2 cannot be ruled out for any measure, and across laboratories the uncertainty is far wider."
4. "The two effects seen in our development data (complexity +0.53, fronto-posterior lag asymmetry +0.53) did not replicate: the confirmation estimates were +0.05 and +0.09, with upper limits near +0.24 and +0.28."
5. "After the result, a reviewer found that in one of the three datasets the recordings continue past the awakening — chin-muscle activity rises about ten-fold, typically 16 to 18 seconds before the end of the file, in three-quarters of recordings — so our window there mostly captured waking, which also explains why 34% of its recordings failed our amplitude check."
6. "Correcting that window after the fact, relaxing the amplitude rule, or removing that dataset did not change the outcome: no test in any re-analysis had a p-value below 0.08."
7. "In the original 'posterior hot zone' recordings, slow-wave power at the back of the head was slightly lower before reports of experience, as published, but the difference was small (about a third of a standard deviation; p = 0.07 with five sites and 0.03 with 23, uncorrected) and would not have met our threshold."
