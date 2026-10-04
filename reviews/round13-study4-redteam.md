# Round 13 red-team — Study 4 (Scenario 26): does the waking-up matter?

Scripts: `/tmp/s4redteam/`. No existing repo file was modified. *Post hoc* = done after
the outcome was known.

**Bottom line.** The run reproduces to every digit and the code does what the plan says.
But (a) the positive control fails: slow-wave power does not clearly fall after the detected
onset, so the two EEG tests (H3, H4) measured movement artefact, not waking; (b) the +0.31
for `emg_jump` is an artefact of who the detector lets in: it changes sign under every
more inclusive rule. Correct label: **uninformative**, not "all null".

## Findings

| # | Claim / issue | Verdict | Evidence | Sev. | Fix |
|---|---|---|---|---|---|
| 1 | Numbers as reported | HOLDS | Re-run from a copy: rows, exclusions and results identical to `study4_awakening.json` (270 onsets; +0.309 / −0.138 / +0.109 / +0.004 / +0.193). | – | – |
| 2 | Detector follows the plan | HOLDS | Baseline = median of first 20 of last 60 s; 3×; 3 of next 4 s; onset must leave ≥5 s. All 455 files have EMG1/EMG2 at 250 Hz; shortest is 81 s. Minor: 46 files whose only crossing is in the last 4 s are logged as "no onset found". | low | Relabel. |
| 3 | "No onset" in 185 files means no awakening | **BROKEN** | 422/455 (93%) have at least one second above 3× baseline in the last 40 s (403 before −2 s). Of the 185, 106 fail only the persistence rule (brief bursts: median 3 s above threshold, peak 10× baseline) and 46 cross only in the last 4 s (Table A). The earlier reviewer's 75% used no persistence rule. Awakenings are present and mostly missed. | high | Report the breakdown; do not describe 185 as "no awakening". |
| 4 | File end is tied to the awakening | **BROKEN** (unstated) | 450/455 durations are 20 n + 1 s: files are cut on 20-s epoch boundaries, so the amount of post-awakening recording is arbitrary (onset 5–38 s before end; quartiles 11/16/21 s). No stimulus marker (19 files sampled). | medium | State it. |
| 5 | Inclusion unrelated to the report | WEAKENED | NREM onset found: no-experience 58/91 (64%), experience 108/186 (58%); Fisher p = 0.43. But the weak-or-absent-rise group (flat or 2–3×) is 1/91 no-experience vs 18/186 experience (Fisher p = 0.009, post hoc): the exclusions remove low-EMG experience awakenings, which biases `emg_jump` upward. In REM, inclusion differs: 12/29 (41%) vs 80/125 (64%), p = 0.035. | high | See 8. |
| 6 | EEG and EMG time axes agree | HOLDS | Trailing trim is 0 samples in all 455 files; both axes count whole seconds from file end. Per-second EEG amplitude rises at the onset (median largest-site peak-to-peak 67 µV at −10 s, 116 at 0, 177 at +5 s). It starts about 3 s *before* EMG onset (81 µV at −3 s), slightly contaminating `delta_before`. | low | – |
| 7 | **Positive control: slow waves fall on waking** | **BROKEN** | `delta_drop` over all stages: mean −0.035 log10 (n = 137 of 270; 55% negative; t-test p = 0.48); subject means +0.017 (9 of 18 negative). NREM analysis set: −0.136 (n = 92; 60% negative; p = 0.02). REM: +0.190. Second by second, unscreened posterior 1–4 Hz power *rises* after onset (median +0.22 log10 at 0 s, +0.37 at +5 s); 13–22% of post-onset seconds exceed 500 µV. `delta_after` indexes movement artefact. | critical | Declare H3 and H4 untestable, not null. |
| 8 | `emg_jump` +0.31 is a lead | **BROKEN** | *Post hoc.* Permutation-null 95% interval −0.07 to +0.69 (subject bootstrap −0.03 to +0.73); positive in 8 of 17 cells. Under more inclusive rules the sign reverses (Table B): 2× threshold −0.18 (n = 200); no persistence −0.10 (n = 225); onset-free peak amplitude on all 277 NREM awakenings −0.27 (p = 0.05, wrong direction for H1). The measure is truncated at +0.48 by the 3× rule. | high | Report Table B; no directional statement. |
| 9 | Design could detect a real effect | WEAKENED | 80% power at p < 0.0125 needs a true effect of about 0.64 SD for the EMG measures (simulated on the actual cells) and about 0.88 SD for the EEG measures (n = 92–93, 11 cells). Study 1 effects were ≤ 0.2. | high | State it. |
| 10 | `emg_rise` | WEAKENED | Heavily tied: 37 of 166 at the cap of 10 (never reaches 10×), 18 at 0. Sign flips to +0.10 … +0.21 under inclusive rules. | medium | – |
| 11 | Procedure; speech vs arousal | UNCHECKED (not checkable) | `ExperimentalDescription.txt`: woken by calling the first name over an interphone, after ≥5 min of stable stage; asked whether they had been dreaming; content not collected. It does not say when the question was put, whether the answer was spoken, or when the recording stopped. It says twenty subjects; the data have 19. The 1–2 s bursts in 106 files are compatible with a one-word spoken answer or a twitch; these cannot be separated. | high | Say EMG rise = arousal and/or speech. |

## Table A — why 185 were excluded

| Category | n | NREM no-exp / exp |
|---|---|---|
| Onset found | 270 | 58 / 108 |
| Crossings, persistence rule failed | 106 | 24 / 35 |
| Crossing only in last 4 s | 46 | 8 / 24 |
| Rise 2–3× only | 14 | 0 / 9 |
| Flat (< 2×) | 18 | 1 / 9 |
| Baseline already elevated | 1 | 0 / 1 |

## Table B — robustness (post hoc; NREM; effect, permutation p)

| Onset rule | n | `emg_jump` | `emg_rise` |
|---|---|---|---|
| **As run** (3×, 3 of 4) | 166 | +0.31, .11 | −0.14, .46 |
| 3×, 2 of 4 | 196 | +0.09, .59 | +0.10, .55 |
| 3×, no persistence | 225 | −0.10, .54 | +0.16, .29 |
| 2×, 3 of 4 | 200 | −0.18, .29 | +0.16, .34 |
| 2×, 2 of 4 | 223 | −0.27, .09 | +0.21, .19 |
| 3×, baseline = quietest 10 s | 181 | +0.14, .45 | +0.06, .73 |
| Onset-free: peak 3-s amplitude ÷ baseline | 277 | −0.27, .05 | – |

No variant reaches p < 0.0125.

## Reading

"All null; neither supported nor contradicted" is right for H1 and H2 only with the power
figure attached. For H3 and H4 it under-describes the problem: the measure failed its
positive control, so those tests are void. Over-claiming would be: "how one wakes does not
matter"; "a trend towards more forceful awakenings" (the sign is rule-dependent); or
"awakening could be identified in 59%" as if the rest did not wake. Under-claiming would be
omitting that the detector missed most of the 185.

## Sentences the authors may quote

1. "In the one open dataset whose recordings continue past the awakening (19 people, 455 awakenings), none of our four pre-registered measures of how a sleeper wakes was related to whether experience was reported; the smallest p-value was 0.11 against a threshold of 0.0125."
2. "This test was weak: our onset rule found an awakening in only 270 of 455 recordings, leaving 166 non-REM awakenings for the muscle measures, enough to detect only a large difference (about 0.64 standard deviations) with 80% power."
3. "A reviewer found that 422 of the 455 recordings do show a rise in chin-muscle activity near the end, so most of the 185 exclusions were awakenings our rule missed, not awakenings that did not happen; and when the rule was loosened after the fact, the largest effect we saw (+0.31) shrank or reversed sign."
4. "The two brain-wave measures failed their own sanity check: slow-wave power did not clearly fall after the detected awakening (average change −0.04 log units, not distinguishable from zero), because movement contaminates the signal, so those two tests tell us nothing either way."
5. "The dataset does not record when the question was asked or whether the answer was spoken, so a rise in chin-muscle activity may reflect speaking as much as waking; the arousal account is neither supported nor contradicted by this study."
