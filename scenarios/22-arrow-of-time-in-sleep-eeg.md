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
