# Round 13 — Study 3 red-team review (dream emotion vs pre-awakening EEG)

Reviewer: adversarial, independent recomputation. Scratch code: `/tmp/s3redteam/` (`cache.py`, `a1.py`–`a5.py`). No repo file modified. All correlations below are within-subject (normal scores, centred), permutation within subject, same design as the pre-registration. Anything marked *post hoc* was not pre-registered.

**Bottom line.** The fourteen nulls reproduce exactly and the window is valid. But the study only had power for strong relations, the "intensity" outcome is mostly positive affect and tracks report length, the subject count is misreported, and no positive control shows the pipeline relating EEG to any report feature. "No measure tracks felt emotion in dreams" is too broad; "no strong relation for these seven measures" is what the data support.

## Findings

| # | Claim / issue | Verdict | Evidence | Severity | Fix |
|---|---|---|---|---|---|
| 1 | Run reproduces; 14 tests null | HOLDS | `--quick` rerun: 113 usable, all r identical to JSON (e.g. valence–eog +0.174, p = 0.063). Independent recompute, 113 awakenings: post_delta max abs diff 0.0008, post_hf 0.0004, faa r = 0.9997, eog r = 0.996 (my filter order differs), intensity and valence exact | – | – |
| 2 | "111 from 17 subjects with ≥3" | BROKEN | 17 subjects contribute a rating; s14 has 2 awakenings and is dropped, so the test uses **16** subjects. `within_corr` returns the count before the ≥3 filter. s13 is lost entirely (7 unrated + 1 white dream) | Low | Report 16; fix the counter |
| 3 | Join Ratings ↔ Records ↔ EDF | WEAKENED | Format `casexx_syy` joins correctly for 120 of 122 rating rows. "No recording" ×2 are different things: `case133_s27` is in Records but its EDF is absent (133 EDFs for 134 records); `case123_s27` is in no Records row, while `case132_s27` (Experience 2, EDF present) has no rating row — probably a typo in Ratings (case123 belongs to s26). One awakening probably recoverable; unconfirmable (Reports folder empty) | Low | Ask the dataset authors; do not silently remap |
| 4 | Rating columns read correctly | HOLDS | Values only 0–4; 140 blanks = 7 rows × 20, all s13 night 2, remark "No self-ratings available" | – | – |
| 5 | Intensity = sum of 20 items is "how strongly felt" | WEAKENED | Positive items are 75% of the total; intensity–positive r = 0.82, –negative 0.57. Negative sum is 0 in 31/113 and ≤2 in 66/113 (floor). Not one-item dominated ("interested" 12.7%, "joyful" 11.8%). Intensity rises with report word count, r = +0.50 (p = 0.0002) | Medium | Say "mostly positive feeling"; report word-count confound |
| 6 | Ratings vary enough within person | HOLDS | Within-subject SD: intensity 5.5 (ICC 0.47), valence 0.65 (ICC 0.24). Within-subject split-half reliability (Spearman–Brown) 0.81 intensity, 0.83 valence; alpha within-centred 0.67 (20 items) | – | – |
| 7 | Files end at the awakening; 2 s skip adequate | HOLDS | All 134 last stage = REM. Chin EMG (>20 Hz, 1 s bins, relative to −100…−25 s): median 1.00–1.04 through −2 s, 1.10 in the final second; bins >2× baseline: 7% at baseline, 11% at −2 s, 19% in the final second. No run-past as in the other dataset. Minor: `extra()` does not trim the ~1 s zero padding in 7 files, so faa/eog windows sit 1 s later than the other measures there | Low | Trim padding in `extra()` |
| 8 | Window is ordinary REM | WEAKENED | Protocol woke people in phasic REM; horizontal EOG SD climbs to 1.3× (−10 s) and 2.0× (−2 s) of its earlier level. The window is selected for eye movements, restricting range | Medium | State it |
| 9 | `eog` measures eye movement | HOLDS (partly) | HL and HR anticorrelate (median r = −0.71), so HL−HR is horizontal EOG; log variance vs saccade count r = +0.80. It misses vertical movement (eog–veog r = +0.50) | Low | Add vertical channel |
| 10 | EEG measures free of eye-movement contamination | WEAKENED | eog vs post_hf −0.42, vs lz −0.43 (both p = 0.0002); vertical EOG vs post_delta +0.44, vs lz −0.42. Frontal delta vs eog +0.47. faa vs eog +0.02 | Medium | Report; see row 11 |
| 11 | Would EOG regression change the result? (*post hoc*) | HOLDS | After regressing H and V EOG from every channel: post_delta −> intensity +0.06, valence +0.03; post_hf −0.05, +0.01; faa +0.03, −0.09. Mastoid reference instead of average: all |r| ≤ 0.08. Still null | – | – |
| 12 | Power | WEAKENED | Simulation with the real structure (16 subjects, n = 3…12, 111 awakenings, 1,500 runs each): 80% power needs true within-subject r ≈ 0.38 at p < 0.0036 and ≈ 0.29 at p < 0.05. At r = 0.20 power is 16% and 48%. False-positive rate 0.3% and 5.7% | High | State sensitivity with the result |
| 13 | Positive controls | WEAKENED | Pipeline detects EEG–EEG (row 10) and report–report relations (word count–intensity +0.50). It shows **no** EEG–report relation: FAA–anger (SR_NA1) −0.09, p = 0.36 (between-subject Spearman +0.26, p = 0.31, n = 17) — published result not recovered, methods differ; time of night vs post_delta +0.09, p = 0.37; word count vs the seven measures, largest eog +0.19, p = 0.06. *Post hoc*: saccade count vs word count +0.26, p = 0.007; vertical EOG vs intensity +0.18, p = 0.04 (uncorrected) | High | Report as a limit on the null |
| 14 | "No measure tracks felt emotion in dreams" | BROKEN as worded | Seven scalp measures, one lab, 16 people, power only for r ≳ 0.38, outcome confounded, no positive control | High | Use the sentences below |

## Recomputed table: fourteen primary tests

95% interval = Fisher z with df reduced for 16 subject means; cluster bootstrap over subjects in brackets.

| Measure | Intensity r (p) | 95% CI [bootstrap] | Valence r (p) | 95% CI [bootstrap] |
|---|---|---|---|---|
| post_delta | +0.14 (0.16) | −0.07, +0.33 [0.00, +0.29] | +0.09 (0.37) | −0.11, +0.29 [−0.10, +0.34] |
| post_hf | −0.05 (0.58) | −0.25, +0.15 [−0.22, +0.13] | −0.00 (1.00) | −0.20, +0.20 [−0.18, +0.16] |
| lz | −0.14 (0.19) | −0.33, +0.07 [−0.34, +0.06] | −0.03 (0.77) | −0.23, +0.17 [−0.28, +0.17] |
| irr (n = 110) | −0.05 (0.54) | −0.25, +0.15 [−0.23, +0.14] | +0.14 (0.12) | −0.06, +0.34 [−0.04, +0.32] |
| fp_lag (n = 110) | +0.03 (0.78) | −0.17, +0.23 [−0.18, +0.28] | −0.01 (0.94) | −0.21, +0.20 [−0.21, +0.17] |
| faa | −0.01 (0.93) | −0.21, +0.19 [−0.20, +0.18] | −0.12 (0.19) | −0.31, +0.08 [−0.24, +0.02] |
| eog | +0.14 (0.14) | −0.06, +0.34 [−0.13, +0.41] | +0.17 (0.06) | −0.03, +0.36 [0.00, +0.34] |

Every interval includes zero. No interval extends beyond ±0.41. **Ruled out:** within-person correlations of about 0.4 or more. **Not ruled out:** anything up to roughly 0.3–0.4, which covers most plausible EEG–self-report effects. Ratings are imperfect (within-person reliability ≈ 0.8), so the underlying relation could be somewhat larger than the observed one.

Directions against the stated expectations: eog–intensity (+) and faa–valence (−) are in the predicted direction; lz–intensity (−) and post_delta–intensity (+) are opposite. None is evidence.

The valence–eog lead (p = 0.06) is stable under leave-one-subject-out (r = 0.12 to 0.23). It does not qualify for the pre-registered replication (needs p < 0.05). *Post hoc*, dropping 44 awakenings with any EMG burst >3× baseline in the window gives r = +0.29, p = 0.009, n = 69 — still above 0.0036 and one of many post hoc looks.

## Outcome distributions (113 awakenings)

| Outcome | Mean | SD | Range | Zeros | Within-subject SD | ICC |
|---|---|---|---|---|---|---|
| Intensity (0–80) | 12.9 | 7.4 | 1–37 | 0 | 5.5 | 0.47 |
| Valence (−4…+4) | +0.65 | 0.74 | −1.1…+2.5 | 2 | 0.65 | 0.24 |
| Positive sum | 9.7 | 6.1 | 0–27 | 1 | 4.7 | 0.44 |
| Negative sum | 3.2 | 4.2 | 0–24 | 31 | 3.8 | 0.19 |

60% of all item responses are 0; anger (NA1) is 0 in 68 of 113.

## Sentences the authors may quote verbatim

1. "In 111 awakenings from dreaming sleep in 16 people, none of seven EEG measures taken from the last minute before waking was reliably related to how strongly or how pleasantly people said they had felt in the dream; the largest correlation was 0.17 (eye-movement activity with pleasantness, p = 0.06), which did not meet our pre-set threshold."
2. "This test could only be expected to find strong relations: it had an 80% chance of detecting a within-person correlation of about 0.38 at our threshold, and the 95% intervals leave room for correlations of up to about 0.4 in either direction."
3. "So the result argues against a strong link between these seven measures and reported feeling; it does not show there is no link."
4. "Our 'intensity' score was mostly positive feeling (three quarters of the total), 31 of 113 reports contained no negative feeling at all, and the score rose with the length of the dream report (within-person correlation 0.50), so it is not a clean measure of how strongly someone felt."
5. "With our methods we did not recover the original authors' link between frontal alpha asymmetry and dream anger (correlation −0.09, p = 0.36), and none of our pre-specified measures was clearly related to any feature of the dream report in these data, which makes the null result less informative."
6. "People were woken during bursts of eye movement and rated their feelings after waking and after telling the dream, in one laboratory; the finding applies to these measures and this set-up, not to brain activity in general."
