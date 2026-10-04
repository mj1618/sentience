# Round 12 — Evidence for scenario 21 (does time create sentience?)

Neutral evidence only; no scoring. Tags: **[V-full]** methods/results read in full text; **[V-abs]** abstract only; **[S]** search snippet; **[R]** recalled, not re-read this round. "Feeling" = self-rated valence unless stated.

## Row 1 — T1* duration floor (cortical activity)

- **Libet et al. 1964** (J Neurophysiol 27:546) **[R]** — awake neurosurgical patients, surface stimulation of S1 with pulse trains. Recalled result: at liminal intensity a train of roughly 0.5 s was needed for a reported sensation; raising intensity shortened the required train (an intensity–train-duration curve). Whether single high-intensity pulses gave sensation or only a motor twitch could not be checked; full text not obtained.
- **Ray, Meador et al. 1999** (Neurology 52:1044; doi:10.1212/wnl.52.5.1044) **[V-abs]** — epilepsy patients with subdural grids over somatosensory or occipital cortex (n not in abstract). Single 100 µs pulses and trains applied; perception thresholds measured. Threshold "changed little" for trains ≥250 ms and "increased sharply" below that. Authors say this confirms Libet's train-duration effect, in visual cortex too, but they saw no motor responses with short trains. The abstract describes a rising threshold, not an absolute floor; whether single pulses were ever perceived is not stated in the abstract.
- **Pockett 2002** (Conscious Cogn; doi:10.1006/ccog.2002.0549) **[V-abs]** — reanalysis, no new data. Argues Libet's ~500 ms reflects facilitation at near-threshold intensity and that his data fit ~80 ms to consciousness. **Gomes 1998** (https://philarchive.org/rec/GOMTTO) **[S]** — minimum train duration is time needed to build an effective stimulus (intensity × duration integration), not a latency of experience.
- **Intracortical microstimulation, human visual cortex.** Schmidt et al. 1996 (Brain; PMID 8800945) **[V-abs]**: n=1 blind woman, 38 electrodes; phosphenes with pulse trains, brightness varied with amplitude, frequency, pulse duration; phosphenes usually ended at train offset. No short-duration limit reported in abstract. Grani et al. 2025 (Sci Adv; PMC12588288) **[V-full, partial]**: n=2; brightness ratings rose with train duration (100–500 ms) and frequency; durations <100 ms not tested.
- **TMS phosphenes** **[R]** — a single sub-millisecond pulse over occipital cortex yields a reported phosphene. Evoked neural activity is longer than the pulse: Romero et al. 2019 (Nat Commun; PMC6572776) **[V-full]**, 2 macaques, 476 parietal neurons, 28% affected; commonest effect a spike burst from ~10 ms lasting <50 ms, with later excitation/inhibition analysed out to 200 ms. Parietal cortex; no perceptual report.
- **Bloch's law** **[R]**; Donner 2021 review (J Exp Biol; PMC8353166) **[V-full, partial]** — below a critical duration (~tens to ~100 ms, shorter at high light levels) detection depends on intensity × duration; i.e. for *stimulus* duration, intensity compensates down to very brief flashes. The neural response outlasts the stimulus.
- **Backward masking** (Rolls & Tovée 1994) **[R]** — with ~20 ms mask asynchrony, inferotemporal neurons fire ~20–30 ms; identification above chance with reduced awareness. Not re-read.
- **Not found:** a duration below which *no tested intensity* of cortical stimulation produces report; nor, verified in full text, report from a single high-intensity cortical pulse with confirmed brief neural response.

## Row 3 — T2* irreversibility as marker

**Monkey ECoG (one shared dataset, Neurotycho; 128 channels, eyes closed) analysed three ways:**

- **Sanz Perl et al. 2021** (Phys Rev E 104:014411; arXiv 2012.10792) **[V-full, preprint]** — wake vs deep sleep (2 animals, 21 sessions), propofol (2 animals, 4 sessions), ketamine (2 animals, 4 sessions), ketamine+medetomidine (4 animals, 11 sessions). Measure: entropy production and curl of probability flux on first PCA components. Result: all reduced-consciousness states, **including ketamine**, closer to equilibrium than wake. Human fMRI part: n=15, wake, N1, N2, N3 and two propofol levels, using *model-generated* extended time series; lower in N2, N3 and propofol, **not N1**. No REM. Authors report no significant correlation between entropy production and band power (1–60 Hz).
- **de la Fuente et al. 2023** (Cereb Cortex; doi:10.1093/cercor/bhac177; bioRxiv 10.1101/2021.09.02.458802) **[V-full, preprint v1 only; journal version not read]** — same data: wake (2 animals, 8 sessions), deep sleep (2 animals, 21 sessions), **ketamine ~5.0 mg/kg, described as anaesthetic dose** (2 animals, 4 sessions). Measure: accuracy (AUC) of deep networks classifying forward vs time-reversed 4 s epochs; 81 models. Wake: all models AUC > 0.75. Ketamine: low-complexity frequency models at chance, **all phase-based models at chance**, but *higher-complexity frequency models performed similarly to wake*. Sleep: frequency models mostly at chance. Model predictions were less consistent in sleep and ketamine. No report of experience (animals); authors themselves note dreaming or ketamine "dreams" as a possible reason some models succeeded. Arousal not controlled; inputs were frequency/phase of PCA components.
- **Deco et al. 2022, INSIDEOUT** (Commun Biol; PMC9187708) **[V-full]** — same dataset, 4 monkeys; measure: squared difference of forward vs reversed time-shifted correlations (T=4 samples), signals z-scored. Text: non-reversibility for "sleep and all anaesthesia conditions **(except for ketamine)** is lower than in the awake state"; recovery after ketamine also did not return as with other agents. So for ketamine, the same recordings give "reduced" under two methods and "not reduced" under a third. Supplementary: human fMRI (n=18) lower in deep sleep; HCP all seven tasks > rest.

- **G-Guzmán et al. 2023** (Interface Focus; PMC10102727) **[V-full]** — fMRI resting state; 13 controls, 31 minimally conscious (MCS), 24 unresponsive wakefulness (UWS). Same INSIDEOUT measure, T=1 TR. Controls > MCS > UWS, all significant. UWS patients have eye-opening arousal; metabolic/activity level not matched or reported; two scanners (controls all on one).

- **Lynn et al. 2021** (PNAS; PMC8617485) **[V-full]** — HCP fMRI, n=590; entropy production from transitions among 8 clustered states. Rest lowest; motor task ~20× rest; entropy production correlated with motor response rate across tasks (r=0.774, p=0.024); 2-back about double 0-back with response rate equal. Controls for head motion and signal variance are in the SI (not read).

- **Kringelbach et al. 2023** (Sci Adv; PMC9839335) **[V-full, partial]** — HCP, n=176; **movie-watching had lower non-reversibility than rest**, and rest lower than tasks (all p<0.001); authors state movie-watching levels are "similar to anesthesia and deep sleep" as quantified in earlier papers. Movie at 7 T, tasks at 3 T.
- **Shinozuka et al. 2025** (Imaging Neurosci; PMC12319965) **[V-full, partial]** — MEG, n=16, LSD 75 µg i.v. vs placebo, four conditions. **LSD reduced irreversibility** in all conditions (p≤0.003), ≥74/90 regions; no region increased. Subjective intensity relation not checked.

**REM sleep** — no REM data in any of the multivariate (INSIDEOUT/entropy-production) studies found. Single-channel EEG studies, different definition (ordinal/visibility-graph asymmetry of one signal):
- Xiong et al. 2019 (Nonlinear Dyn; doi:10.1007/s11071-019-04768-2) **[V-abs]** — NREM *more* irreversible than REM; highest in slow-wave sleep; attributed to slow oscillations.
- Yao 2024 (Phys Rev E 109:054104) **[V-abs]** — PhysioNet polysomnography; permutation irreversibility decreases as sleep deepens; wake and REM "demonstrating greater differences than others"; result depends on handling of equal values and "contradictory results" can arise.
These two disagree in direction; neither has dream reports.

**Seizures**
- Schindler et al. 2016 (Clin Neurophysiol; doi:10.1016/j.clinph.2016.07.001) **[V-abs]** — intracranial EEG; time-irreversible signals in 31 of 32 seizure recordings; maximal irreversibility always during seizures. Single-channel measure; focal epilepsy surgery candidates; consciousness during seizures not reported; not generalised seizures.
- **Not found:** multivariate irreversibility during generalised seizures.

## Row 4 — T2c irreversibility vs felt intensity

- **None found** relating irreversibility or entropy production to self-rated valence or emotional intensity, with or without activity matching.
- Indirect only: HCP EMOTION task (face/shape matching, no valence rating) is mid-ranked among tasks (Deco et al. 2023, Netw Neurosci; PMC10473271; order SOCIAL > RELATIONAL > EMOTION > GAMBLING > MOTOR > WM > LANGUAGE, all > rest); at network level EMOTION and RELATIONAL were "almost as low" as rest **[V-full]**. Lynn 2021: entropy production tracks motor response rate and cognitive load **[V-full]**. Movie-watching lower than rest (Kringelbach 2023).

## Row 5 — T3e hippocampal amnesia

- **Feinstein, Duff & Tranel 2010** (PNAS; PMC2867870) **[V-full via page summary]** — 5 patients with severe anterograde amnesia from bilateral hippocampal damage, 5 matched controls. Sad film clips (~19 min) and happy clips (~17 min) on separate occasions. Self-report (0–100 analogue scales, bipolar valence, PANAS) at baseline and three times up to ~30 min after. Patients recalled a mean 5 (sad) and 4 (happy) details vs 29 for controls (sad). Patients' sadness persisted "at a higher level of intensity and for a longer period" than controls; happiness at "similar level of intensity" and time course. Facial expression coded; **no autonomic measures**. Group numbers shown in figures, not extracted here.
- **Hassabis et al. 2007** (PNAS; PMC1773058) **[V-full via page summary]** — 5 hippocampal amnesics, 10 controls; imagining new scenes. Patients impaired on experiential index, including fewer "thought/emotion/action" details (p=0.001) *within imagined scenes*. **No measure of current feeling.** One patient (P01) unimpaired.
- **Klein et al. 2002**, patient D.B. **[R]** — could not imagine his personal future; no valence ratings recalled.

## Row 6 — T3* interoceptive/homeostatic prediction disrupted

- **Pure autonomic failure.** Heims et al. 2004 (Neuropsychologia; doi:10.1016/j.neuropsychologia.2004.06.001) **[V-abs]** — patients vs healthy controls (n not in abstract): unimpaired on gambling task, emotional face recognition, theory of mind, social cognition; **worse on one emotional attribution test** "perhaps more sensitive to subjective feeling states", not emotion-specific, "requires further validation". Critchley, Mathias & Dolan 2001 (Nat Neurosci) **[R]** — recalled as reporting subtly blunted self-reported emotional experience in such patients; not verified.
- **Spinal cord injury.** Cobos et al. 2002 (Biol Psychol; doi:10.1016/s0301-0511(02)00061-3) **[V-abs]** — 19 patients, 19 matched controls; valence and arousal ratings of affective pictures did not differ; heart-rate modulation similar. Cobos et al. 2004 (Cogn Emot) **[V-abs]** — same 19+19; interview on past vs present emotions: no decrease on any scale; sadness increased more than controls. Lesion levels not given in abstracts. Hohmann 1966 (n=25; reported *reduced* feeling with higher lesions, retrospective interview) and Chwalisz et al. 1988 (no reduction) **[R]**.
- **Insula.** Damasio, Damasio & Tranel 2013 (Cereb Cortex; PMC3657385) **[V-full via page summary]** — n=1 (patient B, herpes encephalitis): insulae destroyed bilaterally, plus hippocampi, amygdalae, anterior cingulate, posterior orbitofrontal; brainstem, hypothalamus, S1/S2 intact. Assessed by 27 years of observation, self-report, spouse questionnaire, 10 naïve raters on 7-point scales. Dense amnesia ("permanent present"). Reported pain, pleasure, itch, hunger, thirst, happiness, sadness, fear. No standardised self-rating numbers. Feinstein et al. 2016, "Roger" (Brain Struct Funct; PMC4734900) **[V-full]** — n=1; bilateral insula, anterior cingulate, amygdala damage; cold-pressor with continuous 0–10 sensory and affective ratings vs 29 healthy men: affective ratings reached 10/10 in 3 of 4 trials (8.7 in the fourth), above the comparison group's 75th percentile; heart rate and skin conductance rose; early withdrawal; warm-water control near floor.
- Caveat for the row: in these cases afferent or cortical *representation* is disrupted; whether brainstem/hypothalamic *prediction* is disrupted was not measured.

## Row 7 — strong T4: timelessness with valence

- **Berkovich-Ohana et al. 2013** (Front Psychol; PMC3847819) **[V-full, partial]** — 12 long-term meditators (11 analysed) volitionally produced "timelessness" for 30 s epochs in MEG; post-session interviews and 1–10 success/stability ratings. **No valence rating.**
- **Hruby, Schmidt, Feinstein & Wittmann 2024** (Sci Rep; PMC11039655) **[V-full]** — n=50 healthy, crossover, 60 min floatation vs bed rest. Floatation gave stronger "loss of the sense of time" (p=0.007) and body-boundary dissolution; after floatation, positive affect rose (SAM valence, p=0.017), anxiety and tension fell. Affect rated *after* the session; mediation of anxiety reduction was via body boundaries, not time loss. Mild, pleasant affect rather than "intense".
- **Psychedelics** **[R]** — Mystical Experience Questionnaire and 5D-ASC: "transcendence of time and space" items load alongside "positive mood/blissful state" in the same sessions (e.g. Griffiths 2006, n=36). Retrospective questionnaires; not re-read. Yanakieva et al. 2019 (PMC6591199) **[V-full, partial]** — n=48, LSD microdoses lengthened reproduced intervals ≥2 s without subjective effects; not a timelessness study.
- **Extreme fear.** Stetson, Fiesta & Eagleman 2007 (PLoS One; PMC2110887) **[V-full]** — ~20 participants, 31 m free fall; retrospective duration estimates 36% longer for own fall (n=7 for that measure); no gain in flicker-fusion resolution. Dilation, not timelessness; fear not rated.
- **Flow** **[R]** — "transformation of time" co-reported with enjoyment, retrospectively. **Depersonalisation** **[R]** — altered time often co-occurs with emotional numbing. Neither read.

## Row 9 — T5* discrete updating

- **VanRullen 2016** (TiCS; doi:10.1016/j.tics.2016.07.006) **[V-abs]** — review: "not one but several rhythms of perception" depending on modality, task, stimulus, region; visual ~10 Hz sensory and ~7 Hz attentional.
- **Herzog, Kammer & Scharnowski 2016** (PLoS Biol; PMC4829156) **[V-full, partial]** — argue against both continuous and simple snapshot models (apparent motion with 3 ms differences; fusion over ~40 ms); propose two-stage model: continuous unconscious processing, then discrete conscious percepts, with windows up to ~400 ms (feature-fusion + TMS). **Herzog, Drissi-Daoudi & Doerig 2020** (TiCS) **[V-abs]** — long-lasting postdictive effects taken to favour the two-stage discrete model. Window length varies by paradigm.
- **White 2018** (Conscious Cogn; doi:10.1016/j.concog.2018.02.012) **[V-abs]** — "Evidence does not consistently support any proposed duration"; EEG periodicity is not periodicity of perception; frame timing appears flexible.
- **Brookshire 2022** (Nat Hum Behav; PMC9489532) **[V-full, partial]** — standard analyses give false positives under aperiodic structure; reanalysis of published datasets found "no evidence for behavioural rhythms in attentional switching".
- **Keitel et al. 2022** (Eur J Neurosci; PMC9544967) **[V-full, partial]** — special-issue overview: frequencies differ between studies and tasks; several failures to find pre-stimulus alpha-phase effects (Benwell, Ruzzoli, Vigué-Guix) and a non-replication of rhythmic attentional sampling, alongside some replications (Plöchl; Ho).
- **Continuous wagon-wheel illusion** (~13 Hz; VanRullen 2005–06; critique Kline, Holcombe & Eagleman 2004: two wheels can reverse independently) **[R]**. **Orch-OR** "conscious moments" at ~40 Hz (Hameroff & Penrose) **[R]** — theoretical claim; no perceptual evidence located.

## Row 10 — T6*/N*: rate changes

- **Wearden & Penton-Voak 1995** (QJEP B; doi:10.1080/14640749508401443) **[V-abs]** — review of human studies 1927–1993: in "almost all cases" subjective time ran faster with raised body temperature and slower when lowered ("observations of the latter type were rare"); parametric trend; authors' favoured explanation is **arousal**. Measures were timing behaviour (mostly counting <100 s), not feeling. **Hoagland 1933** (wife with fever counting seconds) **[R]**; **Baddeley 1966** cold divers **[R]**.
- **Mild cooling, awake.** Falla et al. 2021 systematic review (PMC8470111) **[V-full, partial]** — 18 studies; core cooling impairs complex cognition; mood not a review outcome. Snippet **[S]**: memory registration falls ~70% at core 34–35 °C; volunteers report severe discomfort and shivering. No study found with self-rated valence across core temperatures *with cognition intact*; cognition is itself impaired by ~35 °C.
- **Fever** **[R]** — endotoxin studies show negative mood with fever; confounded by cytokines. Nothing read.
- **Poikilotherms.** Neural rates have Q10 ≈ 2–3 **[R]**. Snippets **[S]**: zebrafish nociceptive behaviour depends on water temperature; activity falls at 7–10 °C. Behavioural markers only.
- **Rate-altering drugs** (stimulants, sub-sedative benzodiazepines) and **slowed-implementation thought experiments** (Searle, Block; argument, not evidence) **[R]** — nothing read.
- **Not found:** any dataset meeting the row's criterion (self-rated feeling under a rate change with cognition and relative timing intact).

## T7 (unscored; all [R])

Smolin's temporal naturalism holds that time's passage is fundamental and laws evolve; he suggests qualia are intrinsic aspects of events, especially novel ("precedent-free") ones. Whitehead's basic units are "occasions of experience" that become and perish; Bergson holds lived duration is real and irreducible to clock time. Presentists and growing-block theorists (Ellis's evolving block universe) say only the present, or past plus present, exists; block-universe theorists say felt passage is a feature of minds. Gisin's intuitionist physics denies infinite-precision real numbers, making the future genuinely open ("creative time"). Proposed empirical handles are indirect: Smolin's law-evolution predictions, Ellis's link to wavefunction collapse, Gisin's finite-information indeterminism. None proposes a test that distinguishes experience-with-passage from experience-without.

## Summary table

| Row | Best evidence | Quality |
|---|---|---|
| 1 | Ray 1999 (abstract): threshold rises sharply for trains <250 ms; Libet 1964 (recalled); no absolute-floor study found | weak (key papers not read in full) |
| 3 | Monkey ECoG: ketamine reduced under two methods, not under a third, same dataset, no reports; DOC graded; tasks > rest; movie < rest; LSD < placebo; REM single-channel, conflicting; seizures high in single-channel focal iEEG (abstract) | moderate for wake/NREM/DOC/task; weak for ketamine, REM, seizures |
| 4 | No direct study | none found |
| 5 | Feinstein 2010 (n=5): self-rated sadness/happiness present and sustained; Hassabis 2007 no affect measure; patient B | moderate (small n; no autonomic data) |
| 6 | Cobos 2002/2004 (n=19+19) ratings normal; Heims 2004 mostly unimpaired, one test worse; Roger (n=1) affective pain 10/10; patient B (n=1) | moderate (abstracts; single cases) |
| 7 | Hruby 2024 (n=50): time-sense loss with improved affect, rated after; psychedelic questionnaires (recalled) | weak–moderate (retrospective; mild affect) |
| 9 | VanRullen 2016 multiple rhythms; White 2018; Brookshire 2022; Keitel 2022; Herzog two-stage model | moderate |
| 10 | Wearden & Penton-Voak 1995 (timing, not feeling); cooling impairs cognition by ~35 °C | weak; none found for the stated criterion |
| T7 | Philosophical positions only | n/a |
