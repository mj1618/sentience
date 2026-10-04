# Round 12 red-team — Scenario 22 (arrow of time in sleep EEG)

Reviewer scripts: `/tmp/r12sleep/` (`rt.py`, `an.py`, `an2.py`; own EDF parser and ordinal code,
20 phase-randomised surrogates per epoch).

**Bottom line.** The arithmetic is right and the headline direction (REM not above deep sleep)
survives bias correction. But the measure is at chance in sleep, the "wake" reference is daytime
artefact, and against in-bed wake the measure fails its positive control. The pre-registered label
"strained" applies by the letter; the fair reading is "uninformative test". "REM looks nothing like
waking" must go.

## Findings

| # | Claim | Verdict | Why (my numbers) | Sev. | Fix |
|---|---|---|---|---|---|
| 1 | Part 2 table is computed correctly | HOLDS | Re-run reproduces the JSON exactly. Independent reader + implementation: max abs difference 1.3e-16 over all 20 subjects, epoch counts identical. PSG and hypnogram start times equal in all 20; 100 Hz; stages 3+4 → deep; movement/"?" dropped. | – | – |
| 2 | Ordinal code sound | HOLDS | Codes 1 and 6 are impossible, always zero in both distributions, skipped by the KL mask. Ties (0.8–1.6% of triples; treated as "down" in both directions, so reversal is not an exact permutation) change medians by ≤0.00002. | low | Drop tied triples. |
| 3 | 19 of 20 subjects | HOLDS, undisclosed | SC4101 has 6 deep epochs; the ≥10-epoch threshold was not pre-registered. With ≥5 it enters and is REM > deep (raw 1/20). | low | State the rule and the excluded subject. |
| 4 | Raw stage differences reflect irreversibility | WEAKENED | JSD is biased upward and the bias depends on spectrum: surrogate floor (mean of 20) wake 0.00070, light 0.00085, deep 0.00095, REM 0.00075. Of the raw deep−REM gap (0.00028), 0.00020 is floor. | high | Report a bias-corrected estimate. |
| 5 | REM ≤ deep sleep (primary) | HOLDS, small | Per-epoch z: REM > deep 3/19. Pooled-count estimate (counts summed over equal numbers of epochs; surrogate floor <1e-5): deep 26.7e-5, REM 3.8e-5, light 2.4e-5; REM > deep 0/19. | – | Quote pooled figure. |
| 6 | "Barely above floor in sleep" | HOLDS, understated | Epochs exceeding all 20 surrogates (chance 4.8%): light 6.0%, REM 7.0%, deep 9.1%, wake 40%. Median z: light −0.22, REM −0.11, deep +0.03 (null simulation: −0.25 to −0.30). Light sleep and REM are essentially null per epoch. | high | Say "at chance per epoch". |
| 7 | Wake is clearly irreversible; "REM looks nothing like waking" | BROKEN | Median 1,911 wake epochs per subject, 44 of them between sleep onset and final awakening. In-bed wake (WASO, n=16): raw 0.00070 vs REM 0.00072, deep 0.00094; wake > deep 3/16; REM closer to wake 10/16; median z 0.20 (all wake: 1.91). Pooled: WASO 8.8e-5 vs deep 27.8e-5, wake > deep 4/16. Low-amplitude wake: see table. | critical | Delete the sentence; define wake as WASO. |
| 8 | Test can separate conscious from unconscious states | BROKEN | Positive control fails (finding 7): in-bed wake is not above deep sleep. A measure that cannot tell awake from deep sleep cannot test T2 in REM. | critical | Call the test uninformative. |
| 13 | Other checks | HOLDS | Eye movements: REM z by EOG tercile −0.18 (low) vs −0.05 (high), works against the result. Secondaries on z: 100 ms REM > deep 4/19, 20 ms 4/19, Pz 2/19. | low | – |
| 9 | Deep-sleep excess is a brain-dynamics property | WEAKENED | Stage 4 > stage 3 (z +0.25 vs −0.04); increment skew negative in 89% of subjects in deep sleep (waveform shape). Header: analogue HP 0.5 Hz, LP 100 Hz at 100 Hz sampling. Simulation: time-symmetric pulses + noise, pooled JSD 0.4e-5; after a causal 0.5 Hz high-pass 10.8e-5; zero-phase 0.2e-5. Same order as the observed 26.7e-5. | medium | Attribute to slow-wave shape/filter, not "direction of time". |
| 10 | Bears on published irreversibility findings | UNCHECKED → no | Literature measures are multivariate/between-region. Exploratory two-channel lagged cross-correlation asymmetry (Fpz-Cz vs Pz-Oz, 40–200 ms, RMS of stage-mean asymmetry, equal epochs): wake 0.024, light 0.068, deep 0.088, REM 0.024; all 3–8× noise; REM > deep 4–5/19; REM closer to wake 12/19. Direction is opposite to the literature (wake lowest), so it most likely indexes travelling slow waves/spindles. | medium | Label exploratory; do not cite as support or strain. |
| 11 | Bears on experience | BROKEN as stated | No awakenings, no reports; stage is a proxy; NREM dreams ~half of awakenings (their own caveat). | high | "Test of sleep stage, not of experience." |
| 12 | "T2 strained" | HOLDS by letter, WEAKENED in meaning | Rule met (REM ≤ deep in 19/19 raw, 16/19 z, 19/19 pooled). But T2's other prediction (wake > deep) fails for in-bed wake, and the "closer to wake" criterion flips from 2/19 to 10/16–16/19 with wake definition. | high | Report label plus "uninformative". |

## Recomputed tables (Fpz-Cz, 40 ms)

| Estimate | Wake (all) | Light | Deep | REM | REM > deep |
|---|---|---|---|---|---|
| Raw (authors) | 0.00175 | 0.00069 | 0.00096 | 0.00068 | 0/19 |
| Surrogate floor (mean of 20) | 0.00070 | 0.00085 | 0.00095 | 0.00075 | – |
| Median z vs 20 surrogates | 1.91 | −0.22 | 0.03 | −0.11 | 3/19 |
| Epochs above all 20 surrogates | 40% | 6.0% | 9.1% | 7.0% | 5/19 |
| Pooled counts (×1e-5) | 92.7 | 2.4 | 26.7 | 3.8 | 0/19 |

| Wake definition | n | Wake raw | Wake z | Wake > deep (raw / z) | REM closer to wake (raw / z) |
|---|---|---|---|---|---|
| All (authors) | 19 | 0.00175 | 1.91 | 17/19 / 19/19 | 2/19 / 0/19 |
| WASO | 16 | 0.00070 | 0.20 | 3/16 / 10/16 | 10/16 / 6/16 |
| Low amplitude (≤ REM 75th pct, no clipping) | 19 | 0.00070 | 0.17 | 2/19 / 10/19 | 16/19 / 7/19 |

Exploratory two-channel asymmetry: wake 0.024 (WASO 0.034), light 0.068, deep 0.088, REM 0.024.

Caveats on my own work: phase-randomised surrogates assume stationarity within an epoch; the pooled
estimator only detects asymmetry with a consistent sign across epochs; the filter simulation shows
possibility, not cause.

## Permitted sentences (verbatim)

1. "On our pre-registered single-channel measure, dreaming (REM) sleep was not more time-irreversible
   than deep sleep in any of 19 subjects, and this direction survived a correction for estimator
   bias (0 of 19 on a pooled estimate; 3 of 19 on a per-epoch surrogate-normalised score)."
2. "However, the measure is close to chance during sleep: about 7% of REM epochs, 9% of deep-sleep
   epochs and 6% of light-sleep epochs exceeded all 20 of their own time-reversible surrogates,
   where about 5% is expected by chance."
3. "The high value we first reported for waking came from daytime recording: roughly 98% of wake
   epochs lay outside the sleep period, and wake during the night scored the same as REM (0.00070
   vs 0.00072) and exceeded deep sleep in only 3 of 16 subjects."
4. "Because the measure does not separate being awake in bed from deep sleep, we regard this test
   as uninformative about the conjecture, although the rule we fixed in advance labels the outcome
   'strained'; the small excess in deep sleep is consistent with the asymmetric shape of slow waves
   and possibly the recorder's filter."
5. "Nobody was woken and asked what they were experiencing, so this was a comparison of sleep
   stages, not of experience."

Not permitted: "REM looks nothing like waking"; "irreversibility falls in deep sleep" (on this
data it does not); any use of the two-channel result as evidence for or against T2.
