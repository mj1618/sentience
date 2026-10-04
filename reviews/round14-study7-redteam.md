# Round 14 — Study 7 red-team (independent methods review)

Scratch code and per-recording features: session scratchpad `s7/` (feat.py, st.py, a1–a3.py, tc.py).
[C] = verified by code; [I] = inferred; [M] = from memory, unverified.

## (a) Reproduces: yes [C]
- From JSON rows, own statistics: −0.382, 515 awakenings, 69 cells; p 0.00025 (200,000 permutations; five 10k seeds 0.0001–0.0005). Per dataset −0.46 (p 0.001), −0.52 (p 0.05), −0.20 (p 0.26).
- `broad` recomputed from raw EDF for all 515 recordings: identical (max difference 0.0). A separate pipeline (native rate, no band-pass, 4 s Welch, MAD channel rejection): −0.38, p 0.0003; r 0.88–0.99 with the original.

## (b) Errors and deviations
1. **The measure is not "all speeds".** `broad` is the log of arithmetic-mean power over 4–40 Hz; 52–70% of that power is 4–8 Hz, and `broad` correlates 0.88–0.95 with 4–8 Hz power. Weighting each frequency equally, the test-set effect is −0.06, p 0.60 [C]. The scenario title is wrong for these data.
2. **No awakening was "located" in Tononi or Noreika** (no channel labelled EMG; Noreika's is "SM-M2"). The window is 34–14 s before file end. In Zhang 29/107 were "located", scattered 2–40 s: implausible as awakenings. Power time-courses are flat until the last 1–2 s, so files do end at the awakening; file-end window for everyone gives −0.38 [C].
3. Zhang: the onset rule dropped 8 recordings (7 experience). Including them: −0.35, p 0.0007 [C].
4. Flat tails ≤1 s (Tononi 178 files, Zhang 11): immaterial [C].
5. `clock()` misreads AM/PM (Zhang "12:16 AM" → noon). Does not touch the registered result [C].
6. Tononi is the Siclari 2017 dataset; a low-frequency decrease with dreaming was already published from it [M]. Not a blind test there.

## (c) Checks (test set; all post hoc)
| Check | Effect | p |
|---|---|---|
| Registered | −0.38 | 0.0003 |
| Good-channel count by report | −0.12 | 0.25 |
| No rejection / strict 150 µV / median over 2 s segments | −0.33 / −0.48 / −0.37 | ≤0.0014 |
| Adjusted for peak amplitude + channel count | −0.37 | 0.0005 |
| Adjusted for chin EMG (Zhang, Noreika) | −0.32 (from −0.33) | 0.035 |
| 1–4 Hz | −0.27 | 0.009 |
| 4–8 / 8–12 / 12–16 Hz | −0.39 / −0.36 / −0.36 | ≤0.001 |
| 16–25 / 25–40 Hz | +0.03 / +0.14 | 0.79 / 0.20 |
| Time-adjusted (clock; Noreika time since lights-off) / order-adjusted | −0.37 / −0.37 | 0.0004 |
| Adjusted for delta; delta adjusted for broad | −0.28; −0.04 | 0.007; 0.72 |
| N2 only; N3 only (Noreika) | −0.41; −0.29 | 0.0004; 0.15 |
| No re-reference; median over channels | −0.27; −0.38 | 0.009; 0.0002 |
| Windows 20–0 / 24–4 / 44–24 / 54–34 s | −0.27 / −0.30 / −0.25 / −0.22 | 0.008–0.03 |
| Without Tononi / Zhang / Noreika | −0.33 / −0.35 / −0.46 | 0.033 / 0.002 / 0.0004 |
| Leave one subject out (64) | −0.42 to −0.35 | 0.0002–0.0018 |
| Subjects negative | 46 of 64 | sign 0.0006 |
| **Protocol cells** (Zhang sleep-onset vs later; Noreika by night) | −0.33 | 0.004 |

(h) Zhang mixes awakenings after ≤90 s of sleep (75% experience) with awakenings after ≥10 min of N2 (27%) in one cell; split, Zhang is −0.65 but p 0.09 on 13 cells. Noreika's −0.20 is between nights; within night +0.11. Tononi (pseudorandom alarms) carries the result.
(i) Reconciled: 20–30 Hz leans higher with experience in both windows (+0.17 last 20 s, +0.10 at 34–14 s), while 4–16 Hz is lower in both. No conflict; opposite signs by frequency.

## Seven datasets (descriptive; mixes the post hoc discovery set with the registered test set)
4–40 Hz: −0.39, p < 0.0001, 1,017 awakenings, 105 cells, 71 of 98 subjects negative; negative in all seven. Bands: 1–4 −0.27; 4–8 −0.35 (all seven negative); 8–12 −0.31; 12–16 −0.26; 16–25 −0.19; 25–40 −0.10 (p 0.25). Above 16 Hz the datasets disagree: Multiple awakenings and Kumral strongly negative; Tononi, Zhang, both Aamodt positive. Only 4–8 Hz survives adjustment for the other bands (−0.25, p 0.002).

## Literature [M]
Siclari 2017: dreaming goes with lower low-frequency and higher high-frequency power posteriorly. Our low-frequency direction agrees; "quieter at all speeds" conflicts, and our test set leans their way above 16 Hz (not significant). Our difference is not posterior-specific (front −0.35, back −0.36). Wong 2020 found no spectral marker in the Noreika data; consistent with Noreika's weakness here.

## (d) Judgement
Real, not artefact: robust to rejection rule, reference, EMG, time of night, any one subject or dataset [C]. But it is a slow-to-mid-frequency (roughly 1–16 Hz, centred on 4–8 Hz) reduction, i.e. lighter NREM sleep before experience reports, not a broadband quietening [C/I]. Partly protocol-driven in Zhang and Noreika; cleanly present in Tononi, where it was already known [I].

## (e) Permitted
1. "One prediction was written down in advance and tested once on 515 awakenings from three sets of recordings; it was supported (effect −0.38, p about 0.0003), and an independent recomputation from the raw recordings gave the same answer."
2. "The measure was dominated by slower rhythms: more than half of it is 4–8 Hz power."
3. "Looked at band by band, power below about 16 Hz was lower before reports of experience; power above 16 Hz was not, and leaned slightly higher."
4. "So the evidence does not show the brain 'quieter at all speeds'; it shows less slow and medium-speed activity, as in lighter sleep."
5. "The difference does not appear to come from movement or muscle artefact, time of night, the choice of reference, or any single person or dataset."
6. "In two of the three datasets part of the difference tracks how the awakenings were scheduled; the cleanest dataset is one from which a similar finding had already been published."
7. "Across all seven datasets, mixing the four that suggested the idea with the three that tested it, the 4–8 Hz reduction appears in every one; faster activity goes different ways in different datasets."
8. "This is an association half a minute before waking, not evidence about what causes experience."

## Forbidden
"Quieter at all speeds/frequencies"; "broadband"; "replicated in seven datasets" without the mixing caveat; "the awakening was located" for Tononi/Noreika; "independent of the published literature"; any causal wording; "contradicts Siclari"; "high-frequency power is lower"; "three datasets each show it"; seven-dataset p as a test.
