# Scenario 29 — Study 7: is the brain quieter at all speeds before reports of experience?

Round 14. **Pre-registration, committed before the measure was computed on the test
recordings.**

## Where the idea came from

Study 6's registered slow-wave test passed narrowly, but reviewers found afterwards that
the difference was not specific to slow waves: power at 4–40 Hz, 34 to 14 s before
waking, was lower before reports of experience (−0.41, p 0.001, four datasets), and the
slow-wave difference vanished once that was accounted for. Found after the fact; a lead.

## Data

Tononi/Siclari (high-density), Zhang & Wamsley, Noreika: the three Study 5 datasets, not
used in Study 6.

What has already been seen of them, stated so the reader can discount accordingly:
- slow-wave (1–4 Hz) power in this same window: about −0.29 (the lead for Study 6);
- 20–30 Hz power in the *last 20 s*: **higher** with experience (+0.18 front, +0.16 back,
  not significant) — the opposite direction to this study's prediction;
- 4–40 Hz power in the 34–14 s window has not been computed on them.

## Measure and analysis (fixed)

Exactly the code already committed in `sims/dream_early_secondary.py` (`broad`: mean log
4–40 Hz power over good scalp channels, average reference, window 34–14 s before the
awakening located by Study 6's rule). N2/N3, experience versus no experience; normal
scores within dataset; within subject-by-stage cells; all cells pooled; 10,000 within-cell
permutations (as Study 6). Run once.

**Primary prediction:** `broad` is lower before reports of experience. **Supported** if
negative with two-sided p < 0.05; **contradicted** if positive with p < 0.05; otherwise
not confirmed.

**Secondary, each reported with its p, none changing the verdict:**
- `rel_delta` (1–4 minus 4–40 Hz): the whole-state reading predicts near zero.
- `delta_early`: expected negative (already seen; a check that the code agrees with the
  reviewer's figure, not a test).
- the primary under the Study 1/5 pooling rule (weighted mean of per-dataset effects,
  datasets with at least 8 people giving both kinds of report).
- per-dataset effects.

## Known weaknesses

The same datasets produced the slow-wave lead, and slow-wave and faster power are
correlated, so this is less independent than fresh data would be. Against that, the one
fast-activity result already seen in these datasets points the other way. No fresh open
dataset remains.

## Result (2026-10-04, run once)

515 N2/N3 awakenings (Tononi 231, Zhang 102, Noreika 182); 69 subject-by-stage cells with
both kinds of report; people with both: 39, 16, 9.

| measure | pooled effect | ± 1.96 null SD | p | Study 1/5 rule | Tononi | Zhang | Noreika |
|---|---|---|---|---|---|---|---|
| `broad` (primary) | −0.38 | −0.58 to −0.18 | 0.0003 | −0.38, p 0.0003 | −0.46 | −0.52 | −0.20 |
| `rel_delta` | −0.12 | −0.32 to +0.08 | 0.24 | −0.13, p 0.22 | −0.11 | −0.54 | +0.03 |
| `delta_early` (check) | −0.27 | −0.47 to −0.07 | 0.008 | −0.28, p 0.007 | −0.26 | −0.72 | −0.10 |

By the rule fixed in advance the primary prediction is **supported**. Awaiting independent
reproduction and red-team; not to be relied on before that.
(The pooling script is inline in the session; outputs in `sims/out/dream/sec_*.json`,
`study7_broad.json`.)

## Review outcome (2026-10-04)

Reproduced from raw recordings by an independent reviewer; full report and permitted
sentences in `reviews/round14-study7-redteam.md`. Main corrections: the measure is
dominated by 4–8 Hz and is not "all speeds" (equal weighting per frequency: −0.06, p 0.60);
band by band, power below ~16 Hz is lower before experience reports and power above is
not; no awakening was located in Tononi or Noreika (no channel labelled EMG) but the files
do end at the awakening; part of the difference in Zhang and Noreika tracks how awakenings
were scheduled; Tononi is the dataset from which a similar finding was already published.
`clock()` misread AM/PM times (did not affect the registered result; fixed afterwards).
