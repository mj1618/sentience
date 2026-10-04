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

---

## Amendment 1 — after the independent methods review, before any confirmation data were opened

The review (`reviews/round13-study1-methods-review.md`) worked only on the development
data and found that the plan above was not ready. Changes, all made and committed before
unblinding:

**Measures**

- `irr_cv` (20 s) had no test–retest reliability in non-dreaming sleep (−0.06). Replaced
  by `irr`: the same idea over a 50 s window (−52 s to −2 s) in five 10 s segments, odd
  segments against even. Test–retest reliability in development data: 0.69. Recordings
  too short for a 50 s window do not contribute to this measure.
- `front_leads` does not measure direction of flow: under the average reference its sign
  flips for a wave travelling front to back. Renamed `fp_lag` (fronto-posterior lag
  asymmetry), computed over the 50 s window, **with no directional interpretation**. Its
  reliability is low (0.30), so a null result would be uninformative. H5 is a
  replication of a sign only.
- `post_hf` band narrowed to 20–30 Hz (some recordings are filtered at 30–35 Hz).
- All measures: the last 2 s before waking are dropped (they can contain waking and
  padding); trailing flat padding is trimmed; the whole end-section is filtered before
  windowing; windows with any site above 500 microvolts peak-to-peak are excluded.
- Channel labels are parsed strictly; two-electrode derivations between scalp sites are
  rejected; high-density (EGI 256) recordings use the published 10–20 equivalents (F3 =
  E36, Fz = E21, F4 = E224, C3 = E59, C4 = E183, P3 = E87, Pz = E101, P4 = E153, O1 =
  E116, O2 = E150). Records are matched to files by path, with an exclusion log.
- **Adjusted versions, co-primary:** `lz_adj` (complexity after removing its relation to
  both power measures; raw complexity is about three-quarters explained by them),
  `irr_adj` and `fp_lag_adj` (after removing the relation to slow-wave power, since both
  lag measures respond to travelling slow waves).

**Analysis**

- Features are converted to normal scores within dataset. The contrast is computed
  **within subject and within sleep stage** (N2 and N3 separately) and combined, because
  stage is related to both the features and the chance of reporting experience.
- Effects are in units of the pooled within-cell standard deviation.
- **Primary test:** permutation of the experience labels within subject-and-stage cells
  (10,000 permutations), statistic = weighted mean of dataset effects. The earlier
  random-effects z-test was shown to give too many false positives with five datasets.
- A dataset enters the primary analysis only with at least 8 subjects contributing both
  kinds of awakening. At least 4 such datasets are required for a confirmatory claim.
- Generalisation across laboratories is described by a Hartung–Knapp interval.

**Decision rules (replace those above)**

Eight tests: `post_delta`, `post_hf`, `lz`, `lz_adj`, `irr`, `irr_adj`, `fp_lag`,
`fp_lag_adj`.

- **Supported:** predicted sign, permutation p < 0.006 (0.05 divided by 8), and at least
  three-quarters of datasets sharing the sign.
- **Contradicted:** p < 0.006 in the opposite direction.
- **Inconclusive:** neither, and the Hartung–Knapp interval includes an effect of ±0.2.
- **Not supported:** neither, and the interval lies within ±0.2.
- The design can reliably detect effects of about 0.35 standard deviations or more.
- **Positive control:** each feature's within-subject difference between lighter states
  (waking, N1, REM) and deep sleep is reported for the confirmation sets. A feature that
  does not move between those states (|dz| < 0.5) has its null result labelled
  uninformative. Development data: `post_delta` −1.29, `lz` +1.08, `irr` +0.61,
  `post_hf` +0.40, `fp_lag` +0.26.

**Recommended by the reviewer and not done** (stated so it is not mistaken for done):
time-of-night as a covariate; muscle-channel power as a covariate; a fixed identical site
set per dataset.

**Permitted before the confirmation run:** reading the *headers* of confirmation
recordings (channel labels, sampling rate, duration) and their record tables' column
names, to confirm the parser handles them. No signal values and no outcome-by-feature
analysis.

**Development-set results under the amended pipeline (exploratory):** Zhang & Wamsley,
102 awakenings, 16 subjects with both kinds: `post_delta` −0.39, `post_hf` −0.11, `lz`
+0.53, `lz_adj` +0.50, `irr` +0.15, `irr_adj` +0.16, `fp_lag` +0.53, `fp_lag_adj` +0.55;
none individually significant by permutation (smallest p ≈ 0.08).

## Amendment 2 — channel-label parsing only, after header inspection, before any confirmation features or outcomes were computed

Header inspection (permitted under Amendment 1) showed that the high-density recordings
label their channels "Chan 36" and not "E36". The parser now accepts both. No other
change. The remaining confirmation headers (Noreika, Aamodt evening and morning) parse
with the frozen rules. The largest archives needed a different unzip tool; the "Multiple
awakenings" archive was still downloading at this commit and will be checked for
integrity before use.

## Amendment 3 — channel-label parsing only, before any outcome analysis

31 high-density recordings (four subjects) label channels with bare numbers ("36") and
have some bad channels already removed (215–256 channels). The parser now accepts bare
numbers for recordings with at least 200 channels. A site whose channel was removed is
simply unavailable; the eight-site minimum still applies. Features had been extracted for
the other recordings at this point, but no outcome had been examined.

## Amendment 4 — channel-label parsing only, before any outcome analysis

In the "Multiple awakenings" recordings the O1 channel is labelled "01" (zero, one). The
parser now reads it as O1. The archive's checksum matched the published one. No outcome
had been examined at this point.
