# Round 14 — Study 6 interim result: independent reproduction and red-team

Reviewer: independent agent, own code, raw recordings. Kumral archive not touched.
Everything in the robustness and confound sections is post hoc.

## Reproduces: yes
- Own statistics from the rows: −0.2607, 29 cells, 452 awakenings. Own pipeline from raw
  files: features match to 1e-5, located awakenings match 452 of 452.
- Permutation p 0.043–0.048 over ten seeds; 0.0454 at 200,000 permutations.
- Only 301 awakenings (195 experience, 106 none) sit in informative cells. Weight:
  Multiple awakenings 85%, Aamodt evening 9%, Aamodt morning 6%.

## Deviations and ambiguities (most important first)
1. The muscle rule mislocates waking in the Aamodt data: of 15 "located", the four with a
   wake annotation all put waking ~2 s before file end. File end for all Aamodt: −0.253,
   p 0.052. Rule was followed as written; the verdict flips on it.
2. Pooling is not the one Studies 1 and 5 used (weighted mean of per-dataset effects, at
   least 8 subjects with both report types). Under that eligibility rule only Multiple
   awakenings counts: −0.23, p 0.11. The code matches the plan's literal wording.
3. Trailing padding not trimmed: negligible (−0.266, p 0.041 when trimmed).
4. Muscle threshold fragile: 2× baseline p 0.077; 5× p 0.058.
5. The "95% range" is estimate ± 1.96 null SD, not a confidence interval.
6. Clean: window arithmetic, channels, bad-channel rule, average reference, normal scores,
   cells, permutation, two-sided p.

## Robustness (post hoc)
| Check | Effect | p |
|---|---|---|
| Without Multiple awakenings | −0.58 | 0.13 |
| Without Aamodt evening | −0.23 | 0.10 |
| Without Aamodt morning | −0.27 | 0.048 |
| N2 only (27 cells) | −0.29 | 0.028 |
| Leave one subject out (28) | −0.33 to −0.20 | 0.013 to 0.13; 14 of 28 above 0.05 |
| File end for all | −0.09 | 0.48 |
| Window 24–4 / 29–9 s | −0.10 / −0.11 | 0.42 / 0.40 |
| Window 39–19 / 44–24 s | −0.30 / −0.32 | 0.02 / 0.013 |
| Window 60–40 s | −0.05 | 0.69 |
| Early minus late (20–0) | −0.27 | 0.014 |
| Early minus clean late (24–4) | −0.16 | 0.07 |
| Subject level: 19 of 28 negative | | Wilcoxon 0.06 |
| No average reference | −0.23 | 0.08 |
| 20–30 Hz power, same window | −0.34 | 0.007 |
| 4–40 Hz power, same window | −0.41 | 0.002 |
| Delta relative to 4–40 Hz | −0.08 | 0.56 |
| Adjusted for clock time | −0.20 | 0.12 |
| Multiple awakenings, adjusted for time, order, duration | −0.13 | 0.35 |

- Within cells slow-wave power falls with clock time (r = −0.35); in Multiple awakenings
  experience reports come later in the night (order +0.30, p 0.03).
- Not specific to slow waves: every band is lower before experience, fast more than slow.
- In Multiple awakenings, 20–40 Hz EEG starts rising ~4 s before the located muscle onset,
  so the last-20-s window contains arousal.
- Aamodt evening −0.87 comes from 24 awakenings in 6 cells; p 0.08 alone.

## Permitted
- "On three datasets, the pre-specified measure came out in the predicted direction
  (−0.26) with p about 0.045; this is interim, and the registered test awaits the fourth
  dataset."
- "The result is borderline: reasonable alternative choices (how waking is located in the
  Aamodt data, the earlier studies' inclusion rule, dropping any of several subjects) move
  p to between 0.05 and 0.13."
- "No single dataset shows it on its own."
- "Checks made after the fact suggest the difference is not specific to slow waves and
  shrinks by a quarter to a half once time of night is accounted for."

## Forbidden
"Confirmed"/"replicated"; "slow waves half a minute before waking predict dreaming"; the
early-versus-late contrast as a finding; "strongest in Aamodt evening"; any causal reading;
citing the 44–24 s window's p.

Reviewer's inference (not verified): broadband, larger further from waking, tracking time
of night — looks more like a slow state or time-of-night difference than a slow-wave
correlate of experience.
