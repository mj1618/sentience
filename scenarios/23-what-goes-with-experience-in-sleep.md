# Scenario 23 — Study 1: which brain measures go with reported experience in sleep?

Round 13. First original study under the owner's instruction to find something new.
**Part 1 is a pre-registration, committed before any confirmation dataset was opened.**

## Why this study

In sleep, a person woken from the same sleep stage sometimes reports having been
experiencing something and sometimes reports nothing. That is the cleanest contrast
available for "experience present versus absent" with the brain in the same overall
state, and reports are taken within seconds. An open database (DREAM; 20 datasets, about
2,600 awakenings) now pools such recordings from many laboratories.

The database's own paper tested how well experience could be predicted from standard
single-channel features and found weak prediction in non-dreaming-stage sleep (average
AUC 0.586). It did not test measures of how brain regions relate to one another, did not
test time-irreversibility, and did not test theory-derived measures head to head across
laboratories. That is the gap.

## Data

- **Development set** (already opened and used to build the pipeline): Zhang & Wamsley
  2019 (58 channels; 308 awakenings); De Gennaro young adults (21 channels; one awakening
  per person).
- **Confirmation sets** (downloading as zip archives; **not opened** at the time of this
  commit): Tononi serial awakenings (the Siclari 2017 data); De Gennaro multiple
  awakenings; Noreika DATA1; Aamodt evening sleep; Aamodt morning sleep. Kumral 2023 will
  be added if it can be downloaded.

## Measures (frozen; code in `sims/dream_features.py`)

Last 20 seconds before awakening. Up to eleven standard scalp sites (F3, Fz, F4, C3, Cz,
C4, P3, Pz, P4, O1, O2); flat channels dropped; at least eight sites required, including
one frontal and one posterior. Zero-phase band-pass 0.5–40 Hz, resampled to 100 Hz,
re-referenced to the average of the selected sites.

| Feature | Definition | Why |
|---|---|---|
| `post_delta` | log power 1–4 Hz, mean of posterior sites | Published "posterior hot zone" finding: less slow activity when experience is reported |
| `post_hf` | log power 20–40 Hz, posterior sites | Published: more fast activity with experience |
| `lz` | Lempel–Ziv complexity of each median-binarised channel, averaged | Complexity accounts |
| `irr_cv` | cross-validated irreversibility: for every pair of sites and lags of 20, 50, 100 ms, the lagged-correlation asymmetry is estimated on the first and second 10 s separately and the two are multiplied; mean over pairs and lags. Centred on zero for a time-reversible process | Conjecture T2 from round 12; never tested against dream reports |
| `front_leads` | lagged-correlation asymmetry between the mean frontal and mean posterior signal (positive = frontal activity leads), mean over the three lags | Feedback/"top-down" accounts; emerged in the development set |

## Analysis (frozen; code in `sims/dream_analysis.py`)

Awakenings from stages N2 and N3 classified "experience" or "no experience"
("experience without recall" excluded from the primary analysis). Features z-scored
within dataset. For each subject with both kinds of awakening, the difference of means;
dataset effect = weighted mean of those differences with a subject-bootstrap standard
error. Datasets with fewer than five such subjects contribute a between-subject
difference to a secondary analysis only. Combination across datasets by random-effects
meta-analysis.

## Hypotheses and decision rules

| | Hypothesis (direction with experience) | Status |
|---|---|---|
| H1 | `post_delta` lower | benchmark (published) |
| H2 | `post_hf` higher | benchmark (published) |
| H3 | `lz` higher | benchmark |
| H4 | `irr_cv` higher | **new** |
| H5 | `front_leads` higher | **new**; suggested by the development set |

A hypothesis is **supported** if, in the confirmation sets only, the primary
meta-analytic estimate has the predicted sign with |z| ≥ 2.58 (two-sided p < 0.01; five
tests), and at least three-quarters of the contributing datasets share that sign. It is
**contradicted** if z is beyond 2.58 in the opposite direction. Otherwise **not
supported**.

**Secondary, also fixed now:** (a) each of `lz`, `irr_cv`, `front_leads` after removing
its linear relation to `post_delta` within dataset, to ask whether it adds anything
beyond slow-wave power; (b) the same contrasts in REM sleep; (c) "experience without
recall" against "no experience".

## Development-set results (exploratory; shown so the reader can see what was known)

Zhang & Wamsley, 110 NREM awakenings, 16 subjects with both kinds:
`post_delta` −0.24 ± 0.13; `post_hf` −0.03 ± 0.12; `lz` +0.40 ± 0.19; `irr_cv`
−0.18 ± 0.24; `front_leads` +0.45 ± 0.19 (within-subject, in standard-deviation units).
Young adults (between-subject, 33 awakenings): nothing distinguishable from zero.

## Known weaknesses, stated in advance

- Scalp EEG with eleven sites is coarse. Lagged asymmetries between scalp sites can
  reflect travelling slow waves and not information flow.
- "No experience" may include forgotten experience.
- Fast-frequency power on the scalp is contaminated by muscle activity.
- Laboratories differ in equipment, reference, and how awakenings were done.
- Finding a measure that goes with reported experience would not show it *is*
  experience, and none of these measures concerns feeling good or bad.

## Process

1. This file and the code are committed before any confirmation archive is opened.
2. An independent methods review of the plan and code follows; any change it prompts is
   recorded here as a dated amendment, still before opening the confirmation data.
3. Then the confirmation run; then independent reproduction and red-teaming; then a
   pre-publication check of the update.
