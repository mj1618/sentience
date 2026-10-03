# 10 — Detecting a chooser: what could be measured, and how well

Brief compiled 2026-10-03. Tags: **[V]** page fetched and number read from it; **[S]** search-result snippet only; **[R]** recalled, not checked; **[G]** my own estimate/arithmetic. The web-search budget ran out part-way; items that could not be checked are listed in §8.

Statistical yardstick used throughout **[G]**: for N binary events with p≈0.5, the smallest bias detectable at 5σ is δ ≈ 2.5/√N; for a correlation between two event streams, r_min ≈ 5/√N.

That gives δ = 2.5e-3 at N=1e6, 2.5e-4 at 1e8, 2.5e-5 at 1e10, and needs N≈1e17 for 1e-8. Direct counting can reach the upper window (1e-2 … ~1e-5) but not 1e-8; the low end is reachable only through amplification (behavioural endpoints, interventions).

## 1. What can be recorded from awake brains, event by event

| Method | Verified capability | Events per experiment |
|---|---|---|
| Neuropixels | 2.0 probe: 5,120 sites on 4 shanks, 384 channels/probe; same neurons tracked >2 months [S] ([PubMed](https://pubmed.ncbi.nlm.nih.gov/33859006/)). Steinmetz 2019: ~30,000 neurons, 42 regions [S] ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6913580)). IBL brain-wide map: 621,733 neurons, 699 insertions, 139 mice, 12 labs [S] ([IBL](https://internationalbrainlab.com/brainwide-map)) | ≈889 units/insertion [G]; at ~5 Hz [R] × 1 h ≈ 1.6e7 spikes per insertion-session [G]; whole IBL set ~1e10 spikes [G] |
| 2-photon voltage imaging | >100 densely labelled neurons, kHz frame rate, 0.4×0.4 mm, >1 h, awake mice [S] ([PubMed](https://pubmed.ncbi.nlm.nih.gov/36973547/)) | ~1e6 spikes plus subthreshold traces per session [G] |
| In-vivo whole-cell patch | Awake robot multipatch: dual/triple recordings in 18% of trials (29% anaesthetised) [S] ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5812718/)). Rat dentate granule cells: EPSC rate 15.1 ± 1.6 Hz awake [V] ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3909463/)) | ~1e4 EPSCs per cell per 10 min [G]; tens of cells per study |
| Glutamate imaging (iGluSnFR3) | In vivo bouton imaging at 500 Hz with paired electrophysiology; 70% of presynaptic APs detected at 0.2 Hz false-positive rate; 1,609 thalamocortical boutons across 13 mice; 15-min "optical mini" recordings without SNR loss; 1.5 min continuous paired recording per bouton [V] ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10250197)) | ~1e3 release/failure events per bouton per 15 min, ~1e5 per field, 1e7 per 100-session study [G] |
| Single-channel in vivo | Cell-attached single-channel recording is routine in slices and isolated neurons [S] ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1156600)); I found no in-vivo awake single-channel dataset | effectively 0 today |

Two design caveats. A spike is not an elementary quantum event but the output of thousands of synaptic and channel events [R], so spike counts are a diluted proxy. And optical release detection misses 30% of events [V], so only *differential* comparisons (same bouton, two conditions) can approach the statistical limit.

## 2. Variability structure a chooser must hide in

| Quantity | Value | Source |
|---|---|---|
| Spike-count noise correlation r_sc | 0.1–0.2 for nearby, similarly tuned, well-driven pairs; lower at low rates and short windows; inflated by multi-unit contamination | [V] [Cohen & Kohn 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3586814) |
| r_sc under anaesthesia | Opioid anaesthesia adds 1–2 Hz global fluctuations; removing them brings correlations down to awake levels | [S] [Ecker et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3990250) |
| r_sc with attention | Attention reduces correlations (roughly halved in V4 [R]) | [S] same review |
| r_sc with task | Structure of V1 correlations changes with task instruction, so it "primarily reflects feedback" | [S] [Bondy, Haefner & Cumming 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5876152) |
| Fano factor | ~1–1.5 in cortex [R]; drops at stimulus onset in all 14 datasets, 7 areas, awake or anaesthetised | [S] [Churchland et al. 2010](https://pubmed.ncbi.nlm.nih.gov/20173745/) |
| Gain model | Poisson spiking × slowly fluctuating gain accounts for single-neuron super-Poisson variance; shared multiplicative gain + additive offset accounts for pairwise structure | [S] [Goris 2014](https://www.cns.nyu.edu/pub/eero/goris13-reprint.pdf), [Lin 2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4534383/) |

**Choice probability (CP).** Britten et al. 1996: mean CP 0.55 in MT [S] ([commentary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4853373/)). Standard account: with r_sc ≈ 0.1–0.2 among pooled neurons, a single neuron's noise is shared by the pool, so CP≈0.55 follows without any single neuron being pivotal (Shadlen 1996 [R]); Haefner et al. 2013 give the analytic relation CP = f(read-out weights, noise covariance) [S] ([Nat Neurosci](https://www.nature.com/articles/nn.3309)).

Nienborg & Cumming 2009 (V2, 76 neurons, 57 with CP>0.5) [V] ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2917918)) found three things a pure bottom-up account does not predict: CP plateaus after ~500 ms while the psychophysical kernel decays; larger rewards *reduced* CP while improving stimulus use; and a choice-dependent gain change (median 1.16×) correlated with CP. Wimmer et al. 2015 reproduce the time course with a hierarchical network: bottom-up early, top-down feedback late [V] ([commentary](https://pmc.ncbi.nlm.nih.gov/articles/PMC4853373/)).

Assessment **[G]**: ordinary network models explain CP qualitatively and I found no reported anomaly. But this is a *sufficiency* argument: the late top-down component is "noise correlated with the decision, of unmeasured origin", and no study shows measured physical state accounts for all of it. It is where a role-conditioned chooser would hide, and where to look.

## 3. Is the noise predictable from prior physical state?

- In vitro, identical fluctuating current gives spike timing reproducible to <1 ms [S] ([Mainen & Sejnowski 1995](https://redwood.berkeley.edu/wp-content/uploads/2018/08/mainen-sejnowski.pdf)). The spike generator is nearly deterministic; variability enters through synapses and network state.
- In vivo, Stringer et al. 2019 (~10,000 V1 neurons): arousal variables explain ~50% of the first population dimension; face-video motion predicts ~31% of the *reliable* spontaneous variance; ≥100 reliable latent dimensions [V] ([bioRxiv](https://www.biorxiv.org/content/10.1101/306019v2.full)).
- Residual **[G]**: about two-thirds of the shared variance and all the private variance is unexplained by measured behaviour. "Unexplained" means unmeasured, not shown to be random; nobody has tested whether an in-vivo release outcome was predictable from the synapse's prior state.

## 4. Physics measurements near living brains

- **Awake vs anaesthetised synaptic statistics.** Pernía-Andrade & Jonas 2014, rat dentate granule cells in vivo [V] ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3909463/)):

| | Anaesthetised (15 cells) | Awake (13 cells) |
|---|---|---|
| EPSC frequency | 15.7 ± 1.6 Hz | 15.1 ± 1.6 Hz |
| EPSC amplitude | 8.76 ± 0.69 pA | 21.30 ± 2.4 pA |
| Decay τ | 5.95 ± 0.26 ms | 3.84 ± 0.36 ms |

  These are spike-driven events, not TTX-isolated minis. I found no study comparing true miniature-release statistics awake vs anaesthetised vs slice.
- **MEG.** Commercial zero-field OPM: <15 fT/√Hz specified, 7–10 typical, 3–100 Hz [S] ([QuSpin](https://quspin.com/products-qzfm-gen2-arxiv/)); SQUID ~2–5 fT/√Hz [R]. No brain magnetic signal is reported as unexplained by neural currents, to my knowledge [R].
- **Ultraweak photon emission.** Established: tissue emits 10–1e3 photons/cm²/s [V] ([Salari et al. 2026](https://arxiv.org/html/2603.26630v1)). Not established: extracranial "brain" emission. Dotta/Persinger 2012 claimed +5e-11 W/m² when imagining light [S] ([abstract](https://www.qigonginstitute.org/abstract-print/7211)), ≈1e4 photons/cm²/s [G]. Salari et al. attribute a recent 25–35 kcounts/s claim to background light: dark forehead ~80 counts/s against 25 counts/s PMT dark rate; a 10 mm leak gives ~40,000 counts/s; scalp+skull transmit 0–2% at 620 nm; the claim would need ≥1e8 photons/cm²/s from brain, 5–7 orders above baseline [V].
- **Torsion balance, atomic clock, dark-matter-style detectors near awake subjects.** None found. This is a gap, not a null result.

## 5. Non-equilibrium and retrocausal variants

| Model | Deviates from standard QM? | Notes |
|---|---|---|
| Valentini non-equilibrium | Yes, if ρ ≠ \|ψ\|² | Predicts signal-nonlocality [S] ([quant-ph/0203049](https://arxiv.org/pdf/quant-ph/0203049)); relaxation is exponential so ordinary matter today is in equilibrium; proposed tests: large-scale CMB power deficit, relic particles, late Hawking radiation, collider spin probabilities [V] ([Valentini 2024](https://arxiv.org/html/2411.10782v1)). A brain chooser of this type needs a new non-equilibrium source and would show as **no-signalling violations** |
| Two-state vector (Aharonov, Vaidman) | No | Same predictions as standard QM [S] ([arXiv:0706.1347](https://arxiv.org/pdf/0706.1347)); suitably distributed final states reproduce Born statistics [S] ([Aharonov & Gruss](https://arxiv.org/abs/quant-ph/0105101)) |
| Price / Wharton retrocausal | No | "Retrocausal but not retro-signaling" [S] ([arXiv:1805.09731](https://arxiv.org/pdf/1805.09731v1)) |
| Cramer, Kastner, Sutherland | No, by construction [R] | Not checked this session |

Distinguishability **[G]**: a *generic* final boundary condition is empirically invisible. A *special* one (post-selection on a future state) is distinguishable in principle, with the same signature as Valentini's: marginal statistics at one site depending on a later or distant choice.

## 6. Human-in-the-loop tests

- **BIG Bell Test** (Nature 557:212, 2018): ~100,000 participants, 97,347,490 binary choices, >1,000 bits/s for 12 h on 30 Nov 2016, 13 experiments in 12 labs; local realism violated as QM predicts [V] ([arXiv:1805.04431](https://arxiv.org/abs/1805.04431)). Human bits were stored and fed in, not space-like separated from the measurement.
- **Hardy 2017**: 100 people at each end of ~100 km, EEG signals switch settings; a failure of QM would indicate mind–matter duality; bottleneck is human switching rate; "just about feasible" [V] ([arXiv:1705.04620](https://arxiv.org/abs/1705.04620)). No completed run found [R].
- **Quantum RNG with affective outcomes**: Maier, Dechamps & Pflitsch 2018: 12,571 people × 100 trials, Quantis QRNG selecting positive vs negative image+sound; mean 50.02% (SD 5.06), BF01 = 10.07 for the null; not pre-registered [V] ([Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.00379/full)). That is 1.26e6 trials, SE ≈ 4.5e-4 [G], so an external-device bias above ~2e-3 is excluded for mild stakes. I found no post-2010 study using pain or reward in animals with a QRNG.

## 7. Xenon isotopes (Li et al., Anesthesiology 2018;129:271–277)

| Item | Value | Tag |
|---|---|---|
| Subjects | 80 male C57BL/6 mice, randomised to 4 groups (so 20 per isotope [G]) | [S] ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29642079/)) |
| Endpoint | Loss of righting reflex ED50, xenon alone and with 0.50% isoflurane | [S] |
| ED50, xenon alone | ¹³²Xe 70 ± 4%, ¹³⁴Xe 72 ± 5% (spin 0); ¹³¹Xe 99 ± 5% (spin 3/2); ¹²⁹Xe 105 ± 7% (spin 1/2) | [V] ([Smith et al. 2021, Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC7973516/)) |
| ED50 with isoflurane | range 15–23% | [V] ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29642079&resultType=core&format=json)) |
| ± is SD or SE | **not verified** | |
| Isotope purity, supplier, blinding, chamber | **not verified** (paywalled) | |
| Cost | Only datum found: 1% enriched-¹²⁹Xe mix, $5,100 per 2,000 L cylinder, i.e. ≈$255 per litre of enriched xenon [G from S] ([trial protocol](https://cdn.clinicaltrials.gov/large-docs/26/NCT02220426/Prot_SAP_000.pdf)). No price found for enriched ¹³¹Xe, ¹³²Xe, ¹³⁴Xe | |

Criticisms. Published: the spin-1/2 vs spin-3/2 ordering is too uncertain to constrain mechanism [V] (Smith et al.). Mine **[G]**: ED50s of 99% and 105% sit at or beyond the top of the ambient-pressure dose range; four separate gas lots mean a lot-specific impurity would mimic an isotope effect; blinding unknown.

Replication: none found 2019–2026. Follow-ups are theory only: a radical-pair model (Smith et al. 2021) and a May 2026 CISS perspective with no new data [V] ([arXiv:2605.19395](https://arxiv.org/abs/2605.19395)). A GitHub checklist (Aug 2026) outlines a replication protocol but names no lab and has no data [V] ([issue](https://github.com/osskosc-lab/QICQ/issues/2)).

Power **[G]**, pooled spin-0 vs pooled spin-bearing difference ≈ 30 points:

| Assumption | n per isotope for 90% power, α=0.05 | n for 90% power at 5σ |
|---|---|---|
| ± is SE of the fitted ED50 (difference 29 ± 6.4, z≈4.5 at n=20) | ~11 | ~39 |
| True effect half as large (winner's curse) | ~41 | ~156 |
| ± is SD across animals (d≈6) | 3 | <10 |

## 8. Not verified

Li 2018 methods (SD/SE, purity, blinding, chamber); isotope prices beyond one ¹²⁹Xe quote; SQUID noise floor; attention effect size; Fano values; Kastner/Cramer/Sutherland equivalence; Britten's 0.55 (secondary source only). All absence claims (in-vivo single-channel data, sensors near brains, xenon replication, animal QRNG study, Hardy run) are failures to find, not proofs.

## Candidate experiments

**1. Blinded five-gas xenon replication.**
- Measured: LORR ED50 in mice for ¹²⁹Xe, ¹³¹Xe, ¹³²Xe, ¹³⁴Xe and natural xenon; coded cylinders, mass-spec assay of each lot, pressurised chamber so all ED50s are bracketed, crossover within animal.
- Events: 40 mice per gas (200 total) [G].
- 5σ sensitivity: ~15-point ED50 shift [G].
- Chooser signatures: not a direct chooser test. A positive result shows a spin-sensitive microscopic process is behaviourally amplified, the precondition for a bias or role-conditioned chooser. Retrocausal: no prediction.
- Confound: gas-lot impurities; hyperbaric effects.
- Feasibility: high; gas cost is the main item (tens of litres per isotope at ~$250/L or more [G]); one lab, under a year.

**2. Same-bouton release statistics across brain states.**
- Measured: release vs failure per presynaptic spike (iGluSnFR3 plus paired or voltage-imaged presynaptic spikes), awake → anaesthetised in the same boutons, then matched slice.
- Events: ~1e5 per session, ~1e7 per 100 sessions [G].
- 5σ sensitivity: differential release-probability shift ~8e-4; pairwise co-release correlation ~1.6e-3 [G].
- Chooser signatures: simple bias gives a state-dependent shift in release probability not predicted by spike history. Role-conditioned gives unchanged marginals but excess co-release among boutons on the same postsynaptic cell, awake only. Retrocausal gives release outcome correlating with a *later* externally randomised event (reward or none) after conditioning on everything earlier.
- Confound: neuromodulators shift release probability by far more than 1e-3; detection errors.
- Feasibility: medium; all parts demonstrated separately.

**3. Choice-probability residual audit (public data).**
- Measured: on zero-signal trials, choice-predictive spiking left after regressing out face video, pupil and population latents, against the ceiling a fitted feedback model allows.
- Events: IBL set, 621,733 neurons, ~1e10 spikes [G]; per-neuron CP standard error ≈ 1/√(3·trials) ≈ 0.03 at 400 trials [G].
- 5σ sensitivity: population-mean residual CP ~1e-3 [G], limited by shared noise, not counts.
- Chooser signatures: simple bias gives a small uniform residual CP. Role-conditioned gives residual concentrated in decision-pivotal neurons and pairwise terms with unchanged single-neuron rates. Retrocausal gives pre-stimulus residual CP surviving removal of history terms.
- Confound: unmeasured top-down signals mimic a chooser; a null is informative, a positive is not.
- Feasibility: very high; analysis only.

**4. No-signalling audit of human-setting Bell data, then a Hardy run.**
- Measured: whether one side's outcome marginals depend on the distant human-chosen setting.
- Events: up to 9.7e7 human bits already recorded [V].
- 5σ sensitivity: marginal shift ~2.5e-4 [G] if all trials were pooled; less per experiment.
- Chooser signatures: simple bias and role-conditioned predict nothing. Valentini non-equilibrium or a special final boundary predicts a no-signalling violation, the only clean discriminator for those variants.
- Confound: detector drift and setting-dependent efficiency.
- Feasibility: re-analysis high; Hardy's 100 km EEG version low.

**5. Differential null-sensor run for an organisation-sourced field.**
- Measured: OPM array (7–10 fT/√Hz) plus a current-insensitive sensor (torsion pendulum or comagnetometer) beside an animal cycled awake ↔ anaesthetised, with a current-dipole phantom control.
- Events: ~1e3 state transitions over weeks [G].
- 5σ sensitivity: OPM ~1 fT in a 1 Hz band after 1e3 averaged transitions [G]; torsion limit not estimated.
- Chooser signatures: none for bias or retrocausal types. An organisation-sourced field predicts a state-locked signal in the current-insensitive sensor unexplained by modelled neural currents.
- Confound: cardiac, respiratory and movement artefacts change with state.
- Feasibility: OPM part high; torsion part medium, apparently never tried.
