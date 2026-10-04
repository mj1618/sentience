# Round 14 — Study 5 (front or back) — adversarial review

Scope: `scenarios/27-front-or-back.md` Part 2, Amendment 1; `sims/dream_topo.py`. Scripts in
`/tmp/s5redteam`. No repo file modified; `conf2/` not opened. Units: within-person SD; "se" = SD of
the permutation null.

## Findings

| # | Claim / issue | Verdict | Evidence | Severity | Fix |
|---|---|---|---|---|---|
| 1 | Part 2 table reproduces | HOLDS | Repo code re-run: identical. Own extraction (own Welch) for all 916 files: max log-power difference 0.035 (Tononi), 0.003 (Zhang), 0.001 (Noreika); all six effects within ±0.01. 231+109+182 = 522; 39+16+9 = 64. | – | `analyse ... --quick` crashes (flag read as a path). |
| 2 | Coordinates and template | HOLDS | +y anterior in both montages (Fpz +1.00, Oz −0.99; E31 +0.98, E126 −0.96) and in the `.sfp`. Template vs `.sfp`: median 4.8°, max 16°; 4 frontal, 6 posterior channels change region; effects unchanged to 2 dp. | low | Use the `.sfp`. |
| 3 | Regions comparable across datasets | WEAKENED | Tononi 57 front / 59 post (16 frontal on the forehead rim); Zhang 16 / 24 (front: Fpz, Fp1/2, AF3/4/7/8, F1–F8; post includes TP7/8 and the CP row); Noreika 8 / 12 (5 of 8 frontal are Fp1, Fp2, Fpz, F7, F8; post includes TP7/8, T5/6). Stricter regions (Noreika F3/Fz/F4 vs P/PO/O): front −0.22 (p 0.03), post −0.19 (p 0.06), grad +0.02 (−0.18 to +0.22). | medium | Report core regions as sensitivity. |
| 4 | Zhang duplicate derivations | WEAKENED (minor) | 9 Zhang files also carry F3‑A2, F4‑A1, C3‑A2, C4‑A1, O1‑A2, O2‑A1; the code counts both, mixing references. Only 2 are in the contrast. | low | Drop non‑REF duplicates. |
| 5 | Average reference couples front and back | WEAKENED | Simulation below: `grad_delta` has the right sign and is zero for a global change, but recovers only 32–63% of a posterior-only change; 10–26% leaks to the front. Channel count (25 vs 166) hardly matters. | medium | State attenuation; add Laplacian. |
| 6 | "By about the same small amount at the front and at the back" | WEAKENED | Within-person correlation of front and post delta: 0.97 / 0.90 / 0.95. One whole-scalp measure, not two findings. Whole-scalp delta: −0.19 (p 0.055). | medium | Report one global measure plus the gradient. |
| 7 | "No sign that the difference is specific to the back" | WEAKENED | True of the pooled estimate under every reference (table). But (a) laboratories disagree: I² 48%, random-effects interval −0.59 to +0.74; (b) the original high-density dataset leans posterior: −0.16 (−0.44 to +0.12), core regions −0.23 (p 0.10); (c) 80% power only for a gradient effect ≥0.29; (d) under the Laplacian the delta effect itself disappears (front −0.07, post −0.01): the signal is spatially broad and scalp position cannot place it. | high | Reword (sentences below). |
| 8 | What is excluded | — | A gradient effect beyond −0.17 SD; in raw terms (gradient SD 0.058 / 0.110 / 0.048 log10) posterior power falling about 2–4% further than frontal. Not excluded: a small focal posterior change under global slow waves; any source-level claim. | – | – |
| 9 | Zhang pre-marker waking | HOLDS | Frontal 20–30 Hz in 4‑s bins: no median rise in Zhang (within ±0.03 log10). Files with a >2× burst inside the window: Zhang 20 (11 experience / 9 none), Tononi 26 (18 / 8), Noreika 8 (4 / 4). Excluding them: front −0.17, post −0.16, grad +0.05. | low | – |
| 10 | Window choice | UNCHECKED (post hoc) | Window −34 to −14 s gives front −0.29, post −0.29 (p≈0.007, uncorrected, post hoc); grad +0.03. Not claimable. | medium | Do not report as a finding. |
| 11 | Six measures, anything beyond noise? | BROKEN if read as a finding | Smallest p 0.08; Bonferroni over six ≈ 0.5. The fast-activity effects vanish under the original reference (+0.05, −0.01). | high | Call it "suggestive, not established". |
| 12 | Amendment 1 predictions | WEAKENED | The two predictions correlate ≥0.90: one test at half alpha. se ≈ 1.05/√W (fits all three sets); for ~42 awakenings se ≈ 0.32–0.40; power at one-sided 0.025 is 7–8% for a true −0.18, 11–15% for −0.30. Eight people with both kinds from ~2 awakenings each is doubtful. | high | Keep the amendment; publish the power figure now; report Kumral as a fourth estimate. |
| 13 | Siclari et al. 2017 | UNCHECKED | `ExperimentalDescription.txt` quotes only methods; no results. From memory, not verified: the posterior low-frequency decrease was a source-space result, and NREM high-frequency increases extended to frontal regions. If so, equal scalp effects do not contradict it. | medium | Cite the paper directly before characterising it. |

## Recomputed tables

**grad_delta (posterior minus frontal), pooled and per dataset**

| Variant | Pooled (95%) | Tononi | Zhang | Noreika |
|---|---|---|---|---|
| As run (average reference) | +0.04 (−0.17, +0.25) | −0.16 | +0.34 | +0.21 |
| Original recording reference | +0.12 (−0.09, +0.32) | −0.08 | +0.23 | +0.38 |
| Surface Laplacian, scalp channels | +0.09 (−0.12, +0.29) | −0.03 | +0.27 | +0.20 |
| Surface Laplacian, all good channels | +0.06 (−0.15, +0.26) | −0.09 | +0.27 | +0.20 |
| Core regions | +0.02 (−0.18, +0.22) | −0.23 | +0.26 | +0.31 |
| Earlier window (−34 to −14 s) | +0.03 (−0.17, +0.24) | −0.17 | +0.22 | +0.27 |

Per-dataset se: Tononi 0.14, Zhang 0.28, Noreika 0.18.

**Delta effects by reference (pooled)**

| | front_delta | post_delta |
|---|---|---|
| Average (as run) | −0.18 (p 0.08) | −0.17 (p 0.10) |
| Original reference | −0.23 (p 0.02) | −0.10 (p 0.32) |
| Laplacian | −0.07 (p 0.45) | −0.01 (p 0.91) |


**Reference-coupling simulation** (three-shell sphere, radial dipoles, each dataset's electrode
positions; 30% power cut in posterior sources only = −0.155 log10; range over source spread and montages)

| Reference | front change | post change | grad |
|---|---|---|---|
| Average (code) | −0.016 to −0.040 | −0.080 to −0.120 | −0.049 to −0.097 |
| Linked mastoids | −0.006 to −0.016 | −0.115 to −0.131 | −0.105 to −0.117 |
| Cz | −0.013 to −0.032 | −0.043 to −0.065 | −0.011 to −0.052 |
| Laplacian | 0.000 to −0.004 | −0.127 to −0.147 | −0.125 to −0.147 |

A uniform cut gives grad 0.000 under every reference. `grad_delta` is a valid but attenuated
test of scalp-level specificity. Idealised model.

## Sentences the authors may quote

1. "Using every scalp channel in three sleep datasets (522 awakenings; 64 people who gave both kinds of report), slow-wave power before reports of experience was lower by about 0.18 within-person standard deviations at the front and 0.17 at the back; neither difference was statistically significant (p = 0.08 and 0.10), and none of our six measures would survive correction for multiple testing."
2. "Front and back slow-wave power rose and fell together almost perfectly from one awakening to the next (correlations of 0.90 to 0.97), so these are better read as one whole-scalp measure than as two separate findings."
3. "The back-minus-front difference was +0.04 (95% interval −0.17 to +0.25): we found no evidence that the reduction is larger at the back, but the three laboratories pointed in different directions (−0.16, +0.34, +0.21)."
4. "In the original high-density dataset the difference leaned towards the back (−0.16, 95% interval −0.44 to +0.12), which is compatible both with no front–back difference and with a modest posterior one."
5. "This is a test at the scalp, not of the 'posterior hot zone' claim itself, which concerns sources inside the brain; in a simulation of our method only about a third to two-thirds of a back-only change showed up in the back-minus-front measure."
6. "The planned confirmation set has only about 42 NREM awakenings from 19 people; by our estimate it has roughly a one-in-ten chance of detecting an effect of the size seen here, so a null result there will not count against it."
