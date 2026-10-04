# Round 14 — Study 6 registered result: independent adjudication (four-dataset pool)

## Reproduces: yes (run)
- Own statistics from rows: −0.268, 502 awakenings, 36 cells. p = 0.0288 at the registered
  seed; converged p = 0.033 (200,000 permutations; ten seeds 0.030–0.035). Last-20-s
  comparison −0.035, p 0.78.
- Kumral features recomputed from raw files with an independent pipeline: all 50 match to
  4 decimals. 110 of 128 channels kept. The one excluded recording has 57% bad channels and
  sits in an all-experience cell. 7 cells, 6 subjects.

## Errors and deviations
1. **Kumral's file end is not the awakening.** Its own description says "up to one minute of
   data before the actual point of waking up may thus have been cut". The plan's rule was
   followed, but Kumral's window is really somewhere between 34–14 s and about 94–74 s
   before waking.
2. Kumral's "no experience" means no recall; the authors did not separate the two.
3. p of 0.029 is a slightly lucky seed; 0.03 is fairer.
4. Only 319 awakenings (205 experience, 114 none) sit in informative cells. Weights:
   Multiple awakenings 79%, Aamodt evening 9%, Kumral 6.5%, Aamodt morning 5.5%.
5. "Supported" is correct under the literal rule; Kumral's inclusion was as registered.
   Under the Study 1/5 eligibility rule only Multiple awakenings qualifies: −0.23, p 0.10.

## Fragility, four-dataset pool (all post hoc)
| Check | Effect | p |
|---|---|---|
| Registered | −0.27 | 0.033 |
| File end for all Aamodt | −0.26 | 0.038 |
| Without Multiple awakenings | −0.50 | 0.11 |
| Without Aamodt evening | −0.24 | 0.076 |
| Without Aamodt morning | −0.27 | 0.033 |
| Without Kumral | −0.26 | 0.045 |
| Leave one subject out (34) | −0.33 to −0.22 | 0.011 to 0.085; 4–5 of 34 above 0.05 |
| N2 only (33 cells) | −0.28 | 0.029 |
| Broadband 4–40 Hz | −0.41 | 0.001 |
| Relative delta | −0.09 | 0.47 |
| Delta adjusted for broadband | +0.04 | 0.74 |
| Broadband adjusted for delta | −0.36 | 0.008 |
| Time-adjusted delta | −0.20 | 0.11 |
| Time-adjusted broadband | −0.30 | 0.018 |
| Time/order vs experience | +0.12 | 0.31 |

No dataset significant alone: 0.10, 0.08, 0.80, 0.50.

Accounts (post hoc): leans clearly against a slow-wave-specific account; time of night
explains about a quarter; best reading is a whole-state difference with lower power at all
frequencies. Moderate strength, one dominant dataset.

Study 5 confirmation "could not be run as registered": correct (6 subjects with both
within a stage; 8 required).

## Permitted
1. "We wrote down one prediction in advance and tested it once on four sets of sleep recordings that had not been used to find it: 502 awakenings."
2. "Brain-wave power in the slow range, measured roughly half a minute before waking, was lower before people reported an experience than before they reported none; by the rule fixed in advance, the prediction counts as supported (effect −0.27, p about 0.03)."
3. "The result is modest and fragile: no single dataset shows it alone, most of the weight comes from one dataset, and removing either of two datasets pushes it past the conventional threshold."
4. "Checks made afterwards show the difference is not specific to slow waves: power was lower at all frequencies, more so at faster ones, and the slow-wave difference disappears once overall power is accounted for."
5. "Time of night explains only part of it, about a quarter."
6. "So the result fits 'lighter overall sleep goes with reported experience' better than 'slow waves switch experience off'; this reading is after the fact."
7. "In the fourth dataset the recordings stop up to a minute before waking, so its timing is imprecise; it is too small to matter either way."
8. "A planned confirmation of the front-versus-back study could not be run: only 6 people gave both kinds of report, and 8 were required."

## Forbidden
"Replicated", "confirmed in four datasets", "Kumral confirmed it"; "slow waves predict or
suppress dreaming" or any causal wording; "p = 0.029" without "about"; the
early-versus-late contrast as a finding; "strongest in Aamodt evening"; "Kumral
supports/contradicts either account"; the Study 5 direction presented as evidence; "just a
time-of-night effect".
