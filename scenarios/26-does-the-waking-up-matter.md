# Scenario 26 — Study 4: does *how a sleeper wakes up* predict whether experience is reported?

Round 13. **Pre-registration, committed before any post-awakening measure was computed
or related to reports.**

## Why

Study 1 found no reliable link between brain activity *before* waking and whether
experience is reported. An old idea in dream research (the "arousal–retrieval" account)
says a dream is only reported if the sleeper wakes fully and quickly enough to store it
before it fades. On that view a "no experience" report can be a failure of memory, and
what should predict the report is the awakening itself, not the seconds before it.

A reviewer of Study 1 found that in one open dataset (De Gennaro "Multiple awakenings":
19 people, 455 awakenings, a yes/no answer to whether they had been dreaming) the
recordings continue for a median of 16–18 seconds past the awakening. That was a flaw for
Study 1. For this question it is an opportunity: the awakening is on the record.

## Measures (fixed now)

- **Awakening onset.** From the chin-muscle channel (difference of the two EMG leads,
  20–100 Hz): root-mean-square amplitude in 1-second steps over the last 60 s; baseline =
  median of the first 20 of those seconds; onset = the first second at which amplitude
  exceeds three times baseline and stays above it for at least three of the next four
  seconds. Recordings with no onset, or an onset within the last 4 s, are excluded.
- `emg_jump`: log10 of mean muscle amplitude in the 3 s after onset minus log10 baseline
  (how forceful the awakening is).
- `emg_rise`: seconds from onset until amplitude first reaches ten times baseline,
  capped at 10 (how abrupt it is; smaller = more abrupt).
- `delta_after`: log posterior slow-wave power (1–4 Hz, the Study 1 sites and reference)
  in the window from 1 s to 9 s after onset, computed only if that window passes the
  500-microvolt check.
- `delta_drop`: `delta_after` minus the same measure in the window from 22 s to 2 s
  before onset (how completely slow waves give way).
- For comparison, `delta_before`: the pre-onset slow-wave power alone (the Study 1
  measure with the window placed correctly).

## Analysis (fixed)

As in Study 1: awakenings from N2 and N3 answered "experience" or "no experience";
normal scores; contrast within subject and sleep stage; 10,000 within-cell permutations.

## Hypotheses

The arousal–retrieval account predicts that reports of experience go with:
H1 larger `emg_jump`; H2 smaller `emg_rise`; H3 lower `delta_after`; H4 more negative
`delta_drop`. Four tests; **supported** at p < 0.0125 with the predicted sign.
`delta_before` is reported for comparison only.

## Known weaknesses, stated in advance

- One laboratory, 19 people. No second dataset with post-awakening recording is known
  to us, so anything found here is a lead needing replication.
- **Direction of cause.** A sleeper with something to report may rouse more vigorously,
  or start speaking sooner (speech moves the chin). The abruptness of the first seconds
  is less exposed to that than the size of the jump.
- **Depth of sleep** affects both how one wakes and whether dreams are reported; the
  within-stage contrast only partly controls for it.
- Brain measures after waking are badly contaminated by movement; many windows will fail
  the amplitude check, and the share that pass will be reported.
- The answer here is a bare yes/no.
