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
