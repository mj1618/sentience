# Scenario 24 — Study 2: is a report of "no experience" about the sleeper's brain in that moment, or about who is asked?

Round 13. **Plan written and committed before the calculation was run.**

## Why

Study 1 looked for a brain signature, in the seconds before waking, of whether a sleeper
will report experience. The whole "within-state" approach to consciousness research
assumes the report reflects what the brain was doing in those seconds. An alternative:
whether someone reports experience is mostly a stable property of the person (some
people rarely report dreams, perhaps because they forget them), plus sleep stage.
If the alternative is right, the paradigm is measuring recall, not experience.

## Data

The DREAM database's table of awakenings (all 20 datasets; latest version of each): for
every awakening, the subject, the sleep stage and the report category. No brain
recordings are needed. For the brain-measure comparison, the Study 1 feature files.

## Measures (fixed now)

Awakenings from N2 and N3 classified "experience" or "no experience", in datasets where
at least 8 subjects have 3 or more such awakenings. For each dataset:

1. **Person.** Predict each awakening's report from the same subject's *other*
   awakenings (the share of them with experience; subjects with fewer than 3 are left
   out). Score: area under the ROC curve (AUC; 0.5 = no information).
2. **Stage and order.** Predict from sleep stage alone (N2 vs N3) where both occur.
3. **Brain measures.** Predict from the five Study 1 features together (logistic
   regression, leave-one-subject-out), for the datasets with features.
4. **Brain measures within person.** As 3, after subtracting each subject's own mean
   from every feature and using only subjects with both kinds of report: can the brain
   measures tell a given person's experience awakenings from the same person's
   no-experience awakenings?
5. The **intraclass correlation** of the report across awakenings of the same subject
   (one-way, on the binary outcome).

AUCs are pooled across datasets by a weighted mean (weights = number of awakenings), with
a bootstrap over subjects for the interval.

## Predictions

- If reports reflect the momentary state of the brain: person AUC near 0.5–0.6, brain
  measures clearly above that.
- If reports are mostly about the person: person AUC well above 0.6 and above the
  brain-measure AUC; within-person brain-measure AUC near 0.5.

**Known limits.** A stable person effect does not show that "no experience" reports are
forgetting: some people may really have less experience in sleep. It would show only
that the contrast used to find signatures of consciousness is largely a contrast between
people. Datasets differ in how awakenings were sampled.

## Review outcome — sentences permitted by the independent reviewer (verbatim)

1. "Across eight sleep datasets (1,136 awakenings), how often a person reported experience on their other awakenings predicted their report on a given awakening modestly: a score of 0.65, where chance on this scoring is about 0.47 and perfect is 1."
2. "The effect was uneven: absent (0.46) in the one dataset whose participants had been selected for giving both kinds of report, and largest (0.88) in two datasets where only 24 'no experience' reports came from 6 of 24 and 5 of 16 participants."
3. "In a check we added afterwards, the person accounted for about 15% of the variation in reports, sleep stage and time of night about 2%, and our five brain measures under 2% more; about four-fifths was explained by nothing we measured."
4. "Our five brain measures did not predict the report: the across-people score of 0.43 is what the method returns when the brain data are scrambled (0.42), and the very low values of 0.14 and 0.11 are an artefact of that method, not a reversed signal."
5. "Within a person the measures scored 0.55 overall, but 0.50 once we set aside the dataset used to build them and the one with a known recording-window problem."
6. "A stable difference between people does not tell us whether 'no experience' reports reflect forgetting or a real absence; it is equally expected from differences in how people judge what counts as an experience, and it does not show that the state of the brain in the moment is irrelevant."

Full review: `reviews/round13-study2-redteam.md`.
