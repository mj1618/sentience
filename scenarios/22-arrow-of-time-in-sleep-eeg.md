# Scenario 22 — A direct test: is brain activity more "one-way in time" when people are experiencing?

Round 12, companion to Scenario 21 (conjecture T2). Our own analysis of public sleep
recordings. **Part 1 written and committed before any data were downloaded.**

## Idea

Conjecture T2 says feeling needs a direction of time: brain activity that looks
different played forwards than backwards. Published work reports that this
"irreversibility" falls in deep sleep and under anaesthesia. The sharper test is
dreaming sleep (REM): the person is unresponsive, as in deep sleep, but on waking usually
reports vivid experience. If irreversibility goes with *experience*, REM should look like
waking. If it goes with something else (being behaviourally awake, or the shape of sleep
waves), REM need not.

## Data

Sleep-EDF Expanded (PhysioNet), "sleep cassette" recordings of healthy adults: whole-night
EEG with sleep stages scored by experts in 30-second epochs. First-night recordings of
the first 20 subjects that download successfully.

## Measures (fixed now)

- **Primary.** Ordinal-pattern irreversibility on the Fpz-Cz EEG channel: for each
  30-second epoch, take the six possible up/down orderings of three samples spaced 40 ms
  apart, and compute the Jensen–Shannon divergence between how often each ordering occurs
  in the signal and in the same signal reversed in time. Zero means the epoch looks the
  same in both directions.
- **Secondary.** (a) The same on the Pz-Oz channel. (b) Absolute skewness of 40 ms
  increments (another standard time-asymmetry statistic) on Fpz-Cz. (c) Primary measure
  at spacings of 20 ms and 100 ms.
- Per subject, the median over epochs of each stage: wake, light sleep (N1, N2), deep
  sleep (N3, including the older "stage 4"), REM. Epochs marked as movement or unscored
  are dropped.

## Predictions, written first

| | T2 (irreversibility goes with experience) | N (it goes with something else) |
|---|---|---|
| Wake vs deep sleep | Wake higher | No commitment; could be either |
| REM vs deep sleep | REM higher | No commitment |
| REM vs wake | Similar: REM closer to wake than to deep sleep | REM differs from wake; may resemble or fall below deep sleep |

**Scoring rule.** T2 is supported only if, on the primary measure, REM exceeds deep sleep
in at least 80% of subjects *and* REM lies closer to wake than to deep sleep in at least
80%, with the same direction on at least two of the three secondary measures. T2 is
strained if REM is at or below deep sleep in most subjects. Anything else is
inconclusive.

## Weaknesses known in advance

- One scalp channel is a crude view of the brain; published claims use many channels or
  brain scans and measure irreversibility between regions, not within one signal.
- Waking recordings contain eye-blink and muscle artefacts, which are strongly
  one-directional; deep-sleep slow waves have an asymmetric shape. Either could drive the
  measure for reasons unrelated to experience. This is why the REM comparison is the one
  that matters: REM has few slow waves and little muscle activity (though it has eye
  movements, which mainly affect the frontal channel; hence the Pz-Oz check).
- Nobody was woken and asked. "REM = experience, deep sleep = none" is a rough
  approximation: dreams are reported from about half of non-REM awakenings.
- A result here would bear on experience in general, not on feeling good or bad.

## Part 2 — Result (pre-registered analysis)

Twenty first-night recordings downloaded; 19 had enough epochs of wake, deep sleep and
REM to enter the comparison.

| Measure | Wake | Light | Deep | REM | Wake > deep | REM > deep | REM closer to wake |
|---|---|---|---|---|---|---|---|
| **Primary: ordinal patterns, 40 ms, Fpz-Cz** | 0.00175 | 0.00069 | 0.00096 | 0.00068 | 89% | **0%** | 11% |
| Same, Pz-Oz | 0.00078 | 0.00076 | 0.00085 | 0.00063 | 37% | 5% | 63% |
| Increment skewness, 40 ms, Fpz-Cz | 0.237 | 0.094 | 0.097 | 0.101 | 100% | 58% | 16% |
| Ordinal patterns, 20 ms | 0.00122 | 0.00048 | 0.00062 | 0.00054 | 100% | 32% | 0% |
| Ordinal patterns, 100 ms | 0.00267 | 0.00124 | 0.00204 | 0.00118 | 63% | 0% | 37% |

(Values are medians across subjects of each subject's median epoch; percentages are the
share of the 19 subjects.)

**By the rule fixed in advance:** REM was at or below deep sleep in every subject on the
primary measure, so T2 is **strained** on this test. The support criterion (REM above
deep sleep and closer to wake in at least 80%) was not met on any measure.

## Part 3 — Exploratory check, not pre-registered

How far above its own noise floor is the measure? For each epoch we compared the primary
measure with the same measure on a scrambled copy that keeps the epoch's frequency
content but is time-reversible by construction.

| Stage | Real | Scrambled | Epochs above their own scrambled copy |
|---|---|---|---|
| Wake | 0.00170 | 0.00053 | 81% |
| Light | 0.00071 | 0.00061 | 53% |
| Deep | 0.00097 | 0.00072 | 62% |
| REM | 0.00071 | 0.00055 | 57% |

During all sleep stages the single-channel measure sits barely above its floor. Only
waking is clearly above it, and waking recordings contain blinks and muscle activity.

## Reading (ours; to be reviewed before use)

On one scalp channel, by these measures, dreaming sleep is not more one-directional in
time than deep sleep, and looks nothing like waking. That is the outcome the conjecture
did not predict. But the measure is close to its noise floor throughout sleep, so this is
a weak test: it shows that this simple measure does not pick out dreaming, not that no
measure would. Published claims use many channels and relations between brain regions.

Code: `sims/sleep_irreversibility.py`. Data: Sleep-EDF Expanded (PhysioNet), not stored
in the repository.
