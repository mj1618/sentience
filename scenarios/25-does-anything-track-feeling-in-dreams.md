# Scenario 25 — Study 3: does any brain measure track how strongly, or how pleasantly, a dreamer felt?

Round 13. **Pre-registration, committed before any rating was related to any brain
measure.** (Looked at so far: the dataset's description, the names of the rating
columns, and the channel labels.)

## Why

Round 7 found that, in the evidence we gathered, no proposed marker of experience had
been tested against *feeling*. An open dataset allows a direct test. In the Turku
serial-awakening study (Sikka, Revonsuo, Noreika, Valli), 18 people were woken 134
times from dreaming (REM) sleep and immediately rated how much they had felt each of ten
positive and ten negative emotions in the dream (0 = not at all, 4 = extremely). The two
minutes of EEG before each awakening are included (24 channels). The original authors
reported that a frontal alpha asymmetry went with dream anger. We ask a different
question: does anything in the recording go with the *amount* of feeling, or with its
*pleasantness*?

## Outcomes (fixed)

- **Intensity:** the sum of all twenty self-rated items.
- **Valence:** mean of the ten positive items minus mean of the ten negative items.
- Secondary: positive sum and negative sum separately.

## Brain measures (fixed)

The five Study 1 measures, computed exactly as in `sims/dream_features.py` (power and
complexity over −22 to −2 s; lag measures over −52 to −2 s), plus two:

- `faa`: frontal alpha asymmetry, log 8–13 Hz power at F4 minus F3 (−22 to −2 s).
- `eog`: log variance of the horizontal eye-movement signal (0.5–10 Hz, −22 to −2 s), a
  rough index of how much rapid eye movement there was.

## Analysis (fixed)

Awakenings with a rating and usable EEG, from subjects with at least three such
awakenings. Each measure and each outcome is converted to normal scores, then centred
within subject, so only differences between one person's awakenings count. Statistic:
the correlation of the centred values. Test: 10,000 permutations of the outcome within
subject.

Fourteen primary tests (7 measures × 2 outcomes). **Supported** at p < 0.0036 (0.05/14).
p < 0.05 is reported as a lead only.

Directional expectations, for the record: intensity with higher `lz`, higher `post_hf`,
lower `post_delta`, higher `eog`; valence lower with higher `faa` (from the original
authors' anger finding). No expectation for the others.

**If more than a quarter of recordings fail the 500-microvolt check** (eye movements are
large in REM sleep), the analysis is also reported with the limit at 1,000 microvolts,
and that is stated.

**Replication, fixed now:** any test with p < 0.05 here is repeated in the Zhang & Wamsley
recordings, using two blind raters' coding of the written dream reports (emotion present
or not; rated pleasantness), agreement between raters 0.93.

## Known weaknesses

One laboratory, 18 people. Ratings are given after waking and after telling the dream.
Frontal measures in REM sleep are contaminated by eye movements. A relation would show
that a measure goes with reported feeling, not that it is the feeling.
