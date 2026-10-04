# Round 13 red-team — Study 2 (Scenario 24, "who or when")

Scripts: `/tmp/s2redteam/` (`orig.py`, `a1`–`a4.py`). No existing repo file was modified.
*Post hoc* = done after the outcome was known.

**Bottom line.** The run reproduces exactly. The person effect is real but modest and
uneven. The brain arm's 0.43 is the floor of the scoring method; 0.14 and 0.11 are
artefacts. The plan's "person vs moment" verdict cannot be drawn.

## Findings

| # | Claim / issue | Verdict | Evidence | Sev. | Fix |
|---|---|---|---|---|---|
| 1 | Reproduces; stage AUC 0.52 | HOLDS | Re-run JSON identical. Tononi has N2 only. | – | – |
| 2 | Person score leaks | HOLDS (no leak) | Own report excluded. Bias runs the other way: leaving out a "yes" lowers that person's score, so chance is below 0.5. | – | State chance level. |
| 3 | "Person AUC 0.647" read against 0.5 | WEAKENED (understated) | Reports shuffled across subjects within dataset, 5,000 times: null mean 0.471, SD 0.029, 95% 0.416–0.528. Observed is 0.18 above (z = 6.1, p = 0.0002). Seven of eight datasets p ≤ 0.012; Tononi p = 0.70. | medium | Quote against 0.47. |
| 4 | Bootstrap interval 0.553–0.675 | BROKEN | Resampling duplicates subjects; pairs within a duplicated subject are always discordant, so draws are biased down (mean 0.615; 86% below the estimate). Between-subject pairs only: 0.679, interval 0.614–0.733. | medium | Report the latter, or the permutation null. |
| 5 | Pooled AUC is the right metric | WEAKENED | It measures base-rate differences between people by construction — the intended quantity — but within person it is 0 by construction, and it weights datasets by size. Unweighted mean 0.71. | medium | Report ICC and Table 1. |
| 6 | Brain AUC 0.43, 0.14, 0.11 | BROKEN | Leave-one-subject-out artefact. Holding out a subject who holds the rare "no experience" reports raises the training base rate and hence the intercept for exactly those rows; scores from different folds are then pooled. Intercept part alone: AUC 0.06 (both Aamodt), 0.18–0.30 elsewhere. With features scrambled across rows the method gives pooled 0.424 (95% 0.343–0.494); observed 0.426. Aamodt: 14 and 10 "no experience" reports held by 6/24 and 5/16 subjects; 0.14 and 0.11 sit at the 5.5th and 6.5th percentile of their scrambled nulls. Not sign-flipping. | critical | Drop the across-subject brain AUC or show its null. |
| 7 | "Person beats brain" | BROKEN (unfair) | Person predictor uses the same subject's outcomes; brain predictor must generalise to strangers on raw features that are mostly person fingerprints (between-subject share of `post_hf` 0.31–0.82). Chance levels differ (0.47 vs 0.42). The features were already null in Study 1, so this was not an independent test. | high | Compare within person only. |
| 8 | Within-person brain AUC 0.55 | WEAKENED | Zhang (0.72) is the development set and falls to 0.54 with within-subject z-scoring; multi (0.59–0.65, p = 0.014) is the wake-contaminated set. Remaining data: 0.50 as run (Tononi 0.56, Noreika 0.42, Aamodt evening 0.48); z-scored 0.51; no dataset p < 0.13. | high | Report 0.50 for clean data. |
| 9 | Pooling eight datasets | WEAKENED | See Table 2. Tononi subjects were selected for having both report types in one night, which removes person variance (0 subjects all-yes or all-no; ICC −0.04). Aamodt's 0.88 rests on 24 reports; participants sleep-deprived. Without Aamodt 0.605; without Tononi 0.695. | high | Give the range first. |
| 10 | "Person effect ⇒ recall, not experience" | BROKEN as inference | See below. | high | Remove from "Why". |
| 11 | Coding of "without recall" | HOLDS, with caveat | White dreams counted as experience: 0.641; counted as no recall: 0.612. But Zhang, multi and Kumral have no such category: "no experience" there means "nothing recalled" (Kumral says so explicitly). | medium | State it. |

## Table 1 — person score against its null

| Dataset | AUC | Null mean ± SD | p | Between-subject pairs only |
|---|---|---|---|---|
| Zhang | 0.664 | 0.474 ± 0.090 | 0.012 | 0.694 |
| LODE | 0.756 | 0.475 ± 0.086 | 0.0002 | 0.779 |
| Multi | 0.588 | 0.472 ± 0.055 | 0.009 | 0.620 |
| Tononi | 0.460 | 0.488 ± 0.055 | 0.70 | 0.472 |
| Noreika DATA1 | 0.623 | 0.450 ± 0.069 | 0.002 | 0.683 |
| Aamodt evening | 0.877 | 0.477 ± 0.113 | 0.0002 | 0.907 |
| Aamodt morning | 0.879 | 0.457 ± 0.142 | 0.0002 | 0.922 |
| Kumral | 0.837 | 0.463 ± 0.139 | 0.001 | 0.871 |
| **Pooled** | **0.647** | 0.471 ± 0.029 | 0.0002 | 0.679 |

## Table 2 — design features that create or remove person effects

| Dataset | Feature |
|---|---|
| Tononi | 32 of 69 chosen from those with both an experience and a no-experience NREM report in one night. |
| Noreika | 5 of 15 dropped after an adaptation night, partly for "unclear dream reports". |
| Aamodt | Sleep-deprived (evening partly; morning a full night awake). Rates 0.88 / 0.84. |
| LODE | Home, spontaneous morning awakenings, self-recorded; person confounded with habits and diligence. |
| Multi | Yes/no answer, no content. |
| Zhang, Kumral | Free report; no "without recall" category. |

## Table 3 — post hoc variance partition (six feature datasets, 840 awakenings)

Linear probability model, adjusted R², n-weighted.

| Predictors | Share explained |
|---|---|
| Stage + time of night | 0.020 |
| Subject | 0.148 |
| Subject + stage + time | 0.161 |
| + five brain measures | 0.177 |
| Brain + stage + time, no subject | 0.019 |

About 82% is unexplained. Subject-mean brain measures do not track subject report rate
(30 Spearman correlations, smallest p = 0.11).

## The dichotomy (item 4)

An intraclass correlation of 0.17 arises equally from fixed personal propensities plus
coin flips and from a strong momentary cause plus small person differences; the plan's
0.6 threshold was calibrated against neither. A person effect is silent on forgetting
versus absence: reporting criterion, sleep depth, age (Tononi rho −0.27, p = 0.10; LODE
+0.42, p = 0.07) and motivation all yield one. *Post hoc* pointer to criterion: among
content-free answers, "something, but I can't recall it" versus "nothing" is itself
person-stable (pooled 0.689 vs null 0.459, p = 0.0005; Tononi 0.654, p = 0.005).

## What can be concluded

People differ modestly and stably in how often they report experience from NREM sleep
(seven of eight datasets). Five scalp measures carry no detectable information about the
report. Most variation is unexplained. Nothing here bears on recall versus experience.

## Sentences the authors may quote

1. "Across eight sleep datasets (1,136 awakenings), how often a person reported experience
   on their other awakenings predicted their report on a given awakening modestly: a score
   of 0.65, where chance on this scoring is about 0.47 and perfect is 1."
2. "The effect was uneven: absent (0.46) in the one dataset whose participants had been
   selected for giving both kinds of report, and largest (0.88) in two datasets where only
   24 'no experience' reports came from 6 of 24 and 5 of 16 participants."
3. "In a check we added afterwards, the person accounted for about 15% of the variation in
   reports, sleep stage and time of night about 2%, and our five brain measures under 2%
   more; about four-fifths was explained by nothing we measured."
4. "Our five brain measures did not predict the report: the across-people score of 0.43 is
   what the method returns when the brain data are scrambled (0.42), and the very low
   values of 0.14 and 0.11 are an artefact of that method, not a reversed signal."
5. "Within a person the measures scored 0.55 overall, but 0.50 once we set aside the
   dataset used to build them and the one with a known recording-window problem."
6. "A stable difference between people does not tell us whether 'no experience' reports
   reflect forgetting or a real absence; it is equally expected from differences in how
   people judge what counts as an experience, and it does not show that the state of the
   brain in the moment is irrelevant."
