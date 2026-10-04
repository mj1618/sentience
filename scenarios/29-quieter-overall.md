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
