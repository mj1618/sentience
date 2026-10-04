# Round 13 methods review — Study 1 (Scenario 23), before confirmation data are opened

Reviewer scripts: `/tmp/s1review/`. Development data only; nothing under `data/dream/conf/` was
opened or listed.

**Bottom line.** The two new measures are not ready. `irr_cv` is unbiased under reversible nulls
but has zero test–retest reliability in NREM, so H4 cannot return an informative result.
`front_leads` does not measure what its name says: under the average reference its sign inverts
for a front-to-back travelling wave and it reduces algebraically to a frontal–central asymmetry.
The benchmarks need fixes to file matching, window end, stage confounding and the
meta-analytic test, which is anti-conservative as coded.

## Findings

| # | Issue | Sev. | Evidence | Amendment |
|---|---|---|---|---|
| 1 | `irr_cv` is noise in NREM | critical | Test–retest (window −22..−2 s vs −42..−22 s), Zhang N2/N3 n=110: Spearman −0.06 (post_delta 0.83, post_hf 0.96, lz 0.88); Young −0.08. Shifting the window 2 s: r=0.63 with itself. N2 median 0.00001, 51% positive (wake 69%, REM 81%). | Declare H4 "not testable in NREM at 20 s" unless a longer window (see A6) reaches reliability ≥0.4 in development data. A null must be reported as uninformative. |
| 2 | `front_leads` sign is not interpretable | critical | Frontal and posterior means correlate −0.95 at zero lag (99% of Zhang windows negative): with 10 sites, p = −(3f+2c)/5, so the f–f terms cancel and the measure equals −(frontal leads central). Empirical r with lagasym(front, central): −0.86 (Zhang), −0.98 (Young). Simulation, front→back travelling delta wave, no interaction: **−0.025** with average reference, **+0.273** without; back→front wave: +0.025. Delayed coupling front→post (30 ms, c=0.7): +0.022 with average reference vs +0.147 without. Test–retest in NREM 0.18. | Rename to "fronto-posterior lag asymmetry (sign reference-dependent)"; drop "top-down/frontal leads" wording. Report alongside a version on the original reference. H5 is a replication of a sign only. |
| 3 | Both lag measures track travelling slow waves and scale with delta | high | Travelling wave, delta gain 1/3/10: irr_cv +0.00006/+0.0012/+0.0034; front_leads −0.005/−0.025/−0.044. Null SD of irr_cv rises 10× with delta (0.0006 → 0.0064); front_leads SD 0.007 → 0.025. Wave direction flipping between halves: irr_cv −0.0011 (96% negative). | Make the delta-adjusted contrast (secondary a) co-primary for H4/H5. State that a negative irr_cv mean signals non-stationarity. |
| 4 | `irr_cv` null behaviour | holds | Mean (SE) over 1,500 runs: mixed AR sources +0.00008 (0.00010); symmetric pulses −0.00008 (0.00014); delta ×3 in second half −0.00007 (0.00006); extra frontal sensor noise 0.00000. Sensitive to delayed coupling c=0.7: +0.0015, 96% positive; c=0.3: 65% positive. Real N2 SD 0.0044, kurtosis 7. | Use a rank-based (within-dataset) transform before z-scoring. |
| 5 | Stage and time-of-night confounding | critical | N2 and N3 pooled; experience odds differ by stage in the expected confirmation counts (N3 70/10 vs N2 177/85). In Zhang, sleep-onset awakenings are 75% experience, later N2 27%; post_delta −0.24 falls to −0.01 when the contrast is taken within subject × (sleep-onset / later); lz +0.39 and front_leads +0.43 persist (13 cells). | Compute differences within subject × stage (N2, N3 separately) and combine. Add time of awakening (hours from each subject's first awakening) as a within-dataset covariate. |
| 6 | File matching can silently drop or mis-assign files | critical | Index is by basename with `.edf`. The DREAM Records README says `Filename` has **no extension** and includes a path; identical basenames in different subject folders overwrite each other; failures only print to stderr. | Match on relative path, try with/without extension, case-insensitive; abort if any two EDFs share a key; write an exclusion log with reasons; require ≥90% of eligible records processed. |
| 7 | Channel names | high | `norm_name` handles 'EEG F3-A2', 'F3:M2', 'F3-M2', 'Fz'. Fails: 'E36' (whole EGI dataset dropped), 'EEG-F3', 'F3A2', 'C3_A2', 'P3.'. Accepts bipolar 'F3-C3' and 'O1-O2' as F3/O1. Mixed contralateral-mastoid references are not removed by the average reference. | Add a per-dataset channel map committed before opening (EGI HydroCel-256 candidates F3=E36, Fz=E21, F4=E224, C3=E59, C4=E183, P3=E87, Pz=E101, P4=E153, O1=E116, O2=E150, Cz=reference; verify against the montage file). Reject derivations whose second electrode is not a mastoid/REF. |
| 8 | Window end | high | No awakening annotation in either development set. 15% of Zhang EDFs end in 1.07 s of flat padding; final-second 20–35 Hz power is −0.24 (N2) to −0.76 (wake) log10 units below the preceding 19 s. The Zhang README states a few seconds of wake can precede the marker. Only 2 s of leading pad for a 0.5 Hz filter and none at the end (head discrepancy 0.07 SD; tail up to 2.3 SD in padded files). | Trim trailing constant samples; filter the whole file, then take −22 s to −2 s. Report −20..0 as sensitivity. |
| 9 | Meta-analysis is anti-conservative | high | Simulated null, 5 datasets: P(\|z\|≥2.58) = 0.019–0.030 (nominal 0.01) with no heterogeneity; 0.045–0.077 with τ = 0.15–0.3. The three-quarters sign rule removes almost nothing (0.019 → 0.019). Truncated Hartung–Knapp: 0.000–0.013, but power 30% at 0.35 SD. | Primary test: permutation of experience labels within subject × stage (10,000), statistic = inverse-variance fixed-effect combined estimate, p < 0.01. Report Hartung–Knapp interval for generalisation. Require k ≥ 4 within-subject datasets. |
| 10 | Power | high | Median meta SE 0.074 (τ=0) to 0.10; 80% power at about 0.35 SD under the current rule (0.25 SD: 54%). The database's own multi-feature AUC of 0.586 corresponds to d≈0.31. Unreliable measures attenuate further. | State the minimum detectable effect (0.35 SD) in the plan; a non-significant result with a confidence interval including ±0.2 SD is "inconclusive", not "not supported". |
| 11 | Positive controls are weak | high | Zhang, within-subject wake minus N2 (n=22), dz: post_delta −0.48 (p=0.035), lz +0.55 (0.017), irr_cv +0.39 (0.083), post_hf +0.03 (0.88), front_leads +0.12 (0.59). Between-awakening d: −0.21, +0.43, +0.40, +0.20, +0.01. REM minus N2 (n=17): lz +0.36, front_leads +0.39, irr_cv +0.23, post_hf +0.14, post_delta −0.13; none p<0.1. "Wake" here is drowsy sleep-onset wake. | Pre-specify: each feature must separate N1/wake/REM from N3 within the confirmation sets (dz ≥ 0.5) or its hypothesis is labelled uninformative. |
| 12 | `post_hf` band and muscle | medium | Zhang files are pre-filtered 0.3–35 Hz, Young at 30 Hz: 30–40 Hz is filter skirt. Fails wake control. | Band 20–30 Hz; add chin-EMG log power (same window) and `Proportion artifacts` as covariates; exclude windows with any site >250 µV peak-to-peak. |
| 13 | `lz` is largely spectral | medium | Implementation matches Kaspar–Schuster on 200 random strings. R² of lz on post_delta + post_hf: 0.76 in NREM. | Co-primary: lz residualised on both power features. A raw H3 result is not independent of H1/H2. |
| 14 | Small-subject rule and scale | medium | Bootstrap SD with 5–8 subjects understates SE; fallback treats repeated awakenings as independent and uses a different metric. z-scoring uses total SD, so units vary with between-subject spread (no label leak). | Threshold ≥8 subjects; standardise by pooled within-subject SD; drop the between-subject fallback from any meta-analysis. |
| 15 | Site count | low | Zhang always 10 sites (Cz flat), Young 11; the reference algebra differs. Resampling is correct for 128, 256, 2000 Hz. | Fix a common site set per dataset; record `n_sites`; sensitivity on the ten-site set. |

## Amendments in priority order

1. Path-safe file matching, exclusion log, coverage floor (6).
2. Per-dataset channel map and derivation check (7).
3. Trim padding; window −22 s to −2 s; whole-file filtering (8).
4. Contrast within subject × stage; time-of-night covariate (5).
5. Within-subject permutation test as the primary test; Hartung–Knapp interval; k ≥ 4 (9).
6. `irr_cv`: test reliability in development data at 60 s and with pooled-over-window estimates; if still <0.4, declare H4 untestable (1).
7. `front_leads`: rename, remove directional interpretation, add original-reference version (2).
8. Delta-adjusted contrasts co-primary for H4, H5; lz adjusted for both power features (3, 13).
9. Within-confirmation positive controls with a stated threshold (11).
10. `post_hf` 20–30 Hz, EMG and artefact covariates, amplitude rejection (12).
11. State minimum detectable effect and the "inconclusive" category (10).
12. Rank transform; ≥8 subjects; within-subject SD scaling (4, 14).

## Which hypotheses are testable as planned

- **H1 (`post_delta`)**: testable after amendments 1–5. Reliable (0.83), passes the wake control weakly.
- **H3 (`lz`)**: testable, but only the spectrum-adjusted version says anything beyond H1/H2.
- **H2 (`post_hf`)**: testable only with the band and muscle amendments; currently fails its control.
- **H4 (`irr_cv`)**: not testable as planned. The estimator is unbiased, but carries no stable signal in NREM.
- **H5 (`front_leads`)**: testable only as a replication of an uninterpreted sign; no claim about direction of flow or "feedback" is licensed. Low reliability (0.18) makes a null uninformative.

Caveats on my own work: simulations use ten sites with Gaussian-falloff mixing, not a head model;
the null-calibration designs assume subject counts I could not check; the EGI site numbers are
from memory and must be verified.
