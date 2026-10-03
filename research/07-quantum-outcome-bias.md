# 07 — Quantum outcome bias: can something *choose* rather than push?

Compiled 2026-10-03. A Born-rule deviation ("consciousness-biased collapse") costs no energy, so the force bound does not apply. What constrains it?

Notation: ε = shift in probability of a binary outcome away from its Born value (p = 0.5 + ε).
Tags: **[V]** source fetched and read; **[S]** search-snippet only; **[R]** recalled, unchecked; **[G]** my own order-of-magnitude estimate/derivation.

---

## 1. Is the brain's randomness quantum or thermal?

**(a) Albrecht & Phillips** (arXiv:1212.0953; PRD 90, 123514). Model a fluid as billiards; quantum uncertainty in impact parameter Δb is amplified per collision by (1 + 2l/r). n_Q = collisions until Δb reaches the molecular radius.

| System | r (m) | l (m) | Δb (m) | n_Q | Tag |
|---|---|---|---|---|---|
| N₂ at STP (air) | 1.6e-10 | 3.4e-7 | 2.9e-9 | −0.3 | [V] |
| Water, body temp | 3.0e-10 | 5.4e-10 | 1.3e-10 | 0.6 | [V] |
| Billiard balls | 0.029 | 1 | 5.1e-17 | 8 | [V] |
| Bumper cars | 1 | 2 | 3.4e-18 | 25 | [V] |

Source: https://arxiv.org/pdf/1212.0953 (Table I). n_Q < 1 means every collision is already quantum-uncertain: "all randomness in these … systems is fundamentally quantum". Neuron/coin step [V]: neural timing jitter δt_n ≈ 1 ms, attributed to fluctuations in the number of open ion channels (driven by Brownian motion of polypeptides in water); with v_h = v_f = 5 m/s, d = 0.01 m this gives δN = 0.5 coin revolutions, so the flip is "a Schrödinger cat". They give no separate neuron n_Q.
Critiques: a plausibility estimate (hard spheres, no decoherence); "quantum in origin" is not "coherent" — it decoheres at once and behaves as thermal noise [G]. No published rebuttal found.

**(b) Koch & Hepp 2006** (Nature 440, 611; https://pubmed.ncbi.nlm.nih.gov/16572152) [S]: argue against quantum computation in the brain; classical description of higher brain function suffices. They do not deny that microscopic events are quantum, only that coherence/entanglement survives to do work. Usual backing figure: Tegmark decoherence times ~1e-13–1e-20 s [R].

**(c) Noise sources** — Faisal, Selen & Wolpert 2008 (https://wolpertlab.neuroscience.columbia.edu/sites/default/files/content/papers/FaiSelWol08.pdf):

| Quantity | Value | Tag |
|---|---|---|
| Johnson + shot noise vs channel noise in CNS neurons | "three orders of magnitude smaller" | [V] |
| Axon diameter where single Na⁺ channel openings trigger spontaneous spikes | < 0.3 µm | [V] |
| Axons "useless for communication" below | 0.08–0.10 µm | [V] |
| Channel-noise spike-time jitter significant in axons of | 0.1–0.5 µm | [V] |
| Postsynaptic amplitude CV per release | > 0.2, "fully accounted for by noise" | [V] |
| Release probability, hippocampal synapses | 0.09–0.54 (single axon); cortex 0–0.9 | [S] https://bionumbers.hms.harvard.edu/bionumber.aspx?id=111652 |
| Na⁺ channel density at axon initial segment | ~200 Nav1.6/µm² (EM) | [S] https://pubmed.ncbi.nlm.nih.gov/18204443 |
| Channels involved per spike at the initiation site | ~1e4–1e5 total (150 µm² × 200/µm²); ~1e2–1e3 open at threshold | [G] |
| Spontaneous miniature release per synapse | ~1e-3–1e-2 Hz | [R]/[G], not found |

**(d) London et al. 2010** (Nature 466, 123; https://ideas.repec.org/a/nat/nature/v466y2010i7302d10.1038_nature09086.html): one extra spike in one neuron → **~28 extra spikes** in its targets [V]; resulting intrinsic membrane-potential noise ±2.2–4.5 mV [S]. Perturbation growth rate (Lyapunov-style) was **not found**; with gain ≫1 per synaptic step (~few ms) a one-spike difference should decorrelate the local microstate within tens of ms [G]. Cortex strongly amplifies single events, but the product is coding-irrelevant *noise* (rate code).

**(e) Quantum events that reach perception**

| Event | Numbers | Tag |
|---|---|---|
| Rod single-photon response (toad; Baylor, Lamb & Yau 1979) | ~1 pA quantal event (5% of dark current), SD 0.2 pA; success rate vs intensity consistent with one photoisomerisation each | [S] https://pubmed.ncbi.nlm.nih.gov/112243/ |
| Human single-photon detection (Tinsley et al. 2016) | 30,767 trials, 2,420 post-selected single-photon events; P(correct) = 0.516 ± 0.010 (p = 0.0545) | [S] https://www.rockefeller.edu/news/11808-study-suggests-humans-can-detect-even-the-smallest-units-of-light/ |
| Radical-pair magnetoreception (ErCRY4, robin) | Sensitive to ~50 µT field; µs-scale spin coherence | qualitative [S] https://media.nature.com/original/magazine-assets/d41586-021-01596-6/d41586-021-01596-6.pdf; numbers [R] |

**(f) Beck–Eccles; Stapp.** Beck & Eccles: exocytosis triggered by tunnelling of a quasiparticle of mass ~1e-23 g (≈6 hydrogen masses); mind raises the tunnelling probability [S] (https://arxiv.org/pdf/quant-ph/0210102). Critique: SNARE-driven fusion arrests at 4 °C, i.e. thermally activated, not tunnelling [S] (same source). Stapp: Ca²⁺ leaving a ~1 nm channel is a spreading wave packet over the ~50 nm to the release site, making release quantum-indeterminate; mind then holds a chosen "template" by rapid Process-1 probing (quantum Zeno) [S] (https://arxiv.org/pdf/quant-ph/9905053). The snippet quotes a spread of ~0.2 nm; I recall Stapp claiming a much larger spread — **unresolved**. Critique (Georgiev, https://arxiv.org/pdf/1412.4741) [S]: Monte Carlo shows the Zeno effect fails for times longer than the decoherence time; local projections cannot lower von Neumann entropy; the mind has no state of its own in the formalism.

---

## 2. How well is the Born rule tested?

| Test | Bound | Tag / URL |
|---|---|---|
| Triple slit, Sinha et al. 2010 (Sorkin κ: third-order / pairwise interference) | < 1e-2 | [S] https://insidetheperimeter.ca/pi-and-iqc-researchers-perform-triple-slit-test-quantum-mechanics/ |
| Three-path interferometer, Söllner et al. | ~1 order better (~1e-3) | [S] https://ar5iv.arxiv.org/html/1412.2198 |
| Five-path, Kauten et al. 2017 | "more than four orders of magnitude" below pairwise term [V]; κ < 3e-5 classical light, < 2e-3 single-photon regime [S] | https://arxiv.org/abs/1508.03253 |
| Outcome frequencies on quantum processors | shot-noise 1/√N confirmed to N = 20,000 (≈3.5e-3 [G]); device bias dominates | [S] https://www.researchgate.net/publication/401265992_Born-Rule_Deviations_Tested_on_Quantum_Processors |
| QRNG (Quantis) raw output | hardware imbalance requires von Neumann unbiasing [S]; ENT suite finds "significant biases" in delivered output [V] | https://eprint.iacr.org/2017/842 |
| BIG Bell Test 2018 | >100,000 people, 97,347,490 human-chosen bits, 13 experiments, 12 labs; all violate local realism as QM predicts; no ε-style precision in abstract | [S]/[V] https://arxiv.org/abs/1805.04431 |

Key point: Sorkin tests probe the *form* of the rule (no third-order interference), not *which outcome occurs*. **Absolute** 50/50 frequency tests are limited by apparatus imbalance at ~1e-3–1e-2 [G]; no dedicated precision test of branching frequency better than ~1e-3 was found. Only **differential** tests (same device, with vs without a mind "wanting") go lower — Section 4.

---

## 3. Theoretical consequences of Born-rule deviation

| Result | Content | Tag / URL |
|---|---|---|
| Gisin 1990 | Weinberg's nonlinear QM permits a "Bell telephone": faster-than-light signalling via singlet states | [S] https://arxiv.org/pdf/quant-ph/0012041 |
| Polchinski 1991 | Forbid EPR signalling and you get communication between Everett branches instead | [S] https://inspirehep.net/literature/28047 |
| Aaronson 2005 | Postselection on outcomes gives PostBQP = PP (⊇ NP) | [S] https://arxiv.org/pdf/quant-ph/0412187 |
| Bao, Bouland & Jordan 2016 | Born exponent p = 2 + δ, any small δ: superluminal signalling *and* faster-than-Grover search; the two always appear together across four classes of deviation | [S] https://arxiv.org/pdf/1511.00657 |
| Valentini | Born rule is an *equilibrium* (ρ = \|ψ\|²) of pilot-wave dynamics. Non-equilibrium matter would allow instantaneous signalling, sub-uncertainty measurements, distinguishing non-orthogonal states, breaking QKD, outpacing quantum computers. Relaxation is fast, so today's matter is in equilibrium; candidates are relic particles and primordial CMB anomalies | [S] https://arxiv.org/pdf/1408.2836 |

Reading for our loophole: these theorems bite when the bias acts on one half of an *entangled* pair in a way the biasing agent controls. A chooser that biases only locally decohered events still technically breaks no-signalling whenever those events are entangled with distant records (nearly always), but exploiting it needs ~1/ε² controlled pairs [G]. In Valentini's framework a persistent bias must be continually pumped out of equilibrium: an H-theorem (second-law) cost, not an energy cost.

---

## 4. Mind-over-quantum-outcome experiments

| Study | N / design | Result | ε per bit | Tag / URL |
|---|---|---|---|---|
| Schmidt 1970, cat + heat lamp | 9,000 trials | 4,615 hits (p < 0.01) | +1.3e-2 [G: 115/9000] | [S] https://psi-encyclopedia.spr.ac.uk/articles/animals-psi-research/ |
| Schmidt 1970, cockroaches + shock | 25,600 trials | 13,109 shocks: *more*, not fewer (p < 0.001) | 1.2e-2, wrong sign | [S] same |
| Peoc'h 1995, chicks + robot | 80 groups × 15 chicks | robot nearer in 71% of groups (p < 0.01); unreplicated, edge-effect critiques | n/a | [S] https://psi-encyclopedia.spr.ac.uk/articles/rene-peoch/ |
| PEAR benchmark | millions of 200-bit trials | "of the order of 1 bit in 10,000" | ~1e-4 | [V] https://psi-encyclopedia.spr.ac.uk/articles/psychokinesis-research/ |
| Jahn et al. 2000, three-lab consortium | 227 operators, 3 × 250 sessions × 3,000 trials × 200 bits ≈ 4.5e8 bits [G] | right direction but "failed by an order of magnitude", not significant | ≲ 1e-5 observed; 2σ sensitivity ≈ 5e-5 [G] | [S] https://www.academia.edu/6873653 (403 on fetch) |
| Bösch, Steinkamp & Boller 2006 | 380 studies, 1961–2004 | "very small", "extremely heterogeneous"; effect size inversely related to sample size; three largest studies π = 0.499989–0.499997 (opposite to intention); 377 remaining: 3.6σ fixed / 4.1σ random effects | overall π ≈ 0.499997 (fixed), 0.500035 (random) [R] → \|ε\| ≲ 3.5e-5 | [S] https://www.researchgate.net/publication/6963201 ; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.00379/full |
| Maier, Dechamps & Pflitsch 2018 (preregistered, Quantis) | 12,571 people × 100 trials = 1.26e6 bits | 50.02% (SD 5.06); BF01 = 10.07, strong evidence for null | +2e-4 ± 4.5e-4; \|ε\| < 1.1e-3 at 95% [G] | [V] frontiersin URL above |
| Dechamps, Maier et al. 2021 | 4 studies, subliminal priming | Study 1 positive; Studies 2–4 "no deviations from the Born rule" | — | [S] https://journals.lub.lu.se/jaex/article/view/23205 |
| Radin et al. 2012/2016 double slit | attention toward slits | claimed fringe shift ~0.001% | 1e-5 (intensity fraction) | [V] https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01891/full |
| Walleczek & von Stillfried 2019 (advanced protocol, Radin blind) | 10,000 trials, 8 conditions | 0 of 2 predicted effects; *sham* condition gave false positive, 0.0159%, p = 0.021 | systematic floor ~1.6e-4 | [V] same |
| Guerrer 2019 | 160 exploratory sessions | z = 3.95 exploratory; confirmatory null | — | [S] https://psi-encyclopedia.spr.ac.uk/articles/gabriel-guerrer/ |

Pattern: effect shrinks as sample size grows (1e-2 → 1e-4 → ≤ 3e-5), the largest studies point the wrong way, and preregistered replications are null. **Upper bound on intention-linked bias of an external quantum RNG: |ε| ≲ 3e-5 per bit (meta-analytic, largest studies); ≲ 1e-3 per bit from the single cleanest preregistered study.**

---

## 5. Quantum statistics inside living neural tissue

| System | Finding | Precision | Tag |
|---|---|---|---|
| Rod photon responses | Counts consistent with Poisson; quantal amplitude CV ≈ 0.2 (Baylor 1979; Rieke & Baylor 1998) | ~10% at best [G]; isolated retina, not awake animal | [S] https://pubmed.ncbi.nlm.nih.gov/112243/ |
| Vesicle release | Binomial (uniform or non-uniform p) "generally provided good fits" | chi-square on ~1e2–1e3 trials → ε ~ 3e-2–1e-1 [G] | [S] https://pubmed.ncbi.nlm.nih.gov/14667542/ |
| Ion-channel gating | Liebovitch "fractal" kinetics claim; Korn & Horn 1988 and McManus et al. 1988: Markov models fit better on all channels tested (likelihood, AIC) | patch-clamp, excised | [S] https://scholars.uthscsa.edu/en/publications/fractal-models-are-inadequate-for-the-kinetics-of-four-different-/ |
| Awake vs anaesthetised statistics comparison | **None found** | — | — |

No one has tested microscopic event frequencies in awake tissue to better than a few percent, and release probability is itself biologically regulated, so there is no fixed "Born value" to compare against.

---

## 6. Existing theories of this type

| Theory | Quantitative prediction | Tag / URL |
|---|---|---|
| Stapp (Zeno) | Mind chooses which observable and how often; outcomes stay Born. No ε. Needs coherence longer than the decoherence time (fails per Georgiev) | [S] https://arxiv.org/pdf/1412.4741 |
| Chalmers & McQueen (IIT + CSL) | Superpositions of integrated-information states collapse at a rate tied to Φ; simple "never superposed" version falsified by Zeno; testable in principle on quantum computers. Born rule kept; no ε | [S] https://arxiv.org/pdf/2105.02314 |
| Kent, *Quanta and Qualia* | Motivates "conscious observers deviate — perhaps only very subtly and slightly — from quantum dynamics"; calls for experiments with observers in the loop. No number | [V] https://arxiv.org/abs/1608.04804 |
| Kent, *Testing causal quantum theory* | Local hidden-variable alternative surviving via the collapse-locality loophole; predicts Bell violations vanish if collapse (possibly observer-linked) is delayed beyond light-crossing. Binary prediction, no ε | [S] https://ar5iv.labs.arxiv.org/html/1807.09663 |
| Hardy 2017 | Bell test with ~100 people at each end, ~100 km apart, EEG switching settings; "very unlikely" outcome: Bell inequality *satisfied* when humans choose. Binary | [S] https://arxiv.org/pdf/1705.04620 |

None states a magnitude for ε. The BIG Bell Test is a weak partial version of Hardy and found standard QM.

---

## Constraints this yields

1. **Strong** — Intention/feeling does not bias an *external* quantum RNG above ε ≈ 3e-5 per bit (Bösch large studies; Jahn 2000), and the cleanest preregistered test bounds it at ~1e-3 with Bayesian support for zero.
2. **Strong (theoretical)** — Any controllable Born deviation on entangled systems gives superluminal signalling and super-Grover computation (Gisin; Polchinski; Bao et al.). A chooser must be either uncontrollable-in-principle or confined to events never usefully entangled.
3. **Moderate** — The form of the Born rule (no higher-order interference) holds to 3e-5 (classical light) / 2e-3 (single photons). This does not test outcome selection.
4. **Moderate** — Brain noise is plausibly quantum in *origin* (Albrecht–Phillips n_Q = 0.6 for water) and cortex amplifies single events (1 spike → 28). So a chooser has a lever; but the amplified variability behaves as coding-irrelevant noise.
5. **Moderate** — Animal results (Schmidt ε ≈ 1e-2) are small-N, one wrong-signed, unreplicated; they sit exactly where small-study bias predicts.
6. **Weak** — In-tissue statistics (rod Poisson, binomial release, Markov gating) agree with standard stochastic models at only ~1e-2–1e-1 precision, in vitro or anaesthetised.
7. **Weak** — Absolute 50/50 frequency tests are apparatus-limited at ~1e-3–1e-2; no theory in Section 6 supplies an ε to aim at.

## Where a bias could still hide

- **System:** microscopic events *inside the conscious brain itself* (channel gating at threshold, vesicle release, Ca²⁺ arrival), in awake tissue, where the experiencing system and the biased system are the same. No experiment has looked.
- **Magnitude not excluded:** ε up to **~1e-2 per event** [G], set by in-vitro fit precision and by biological regulation of the baseline probabilities. Lower edge of interest: to shift a threshold crossing involving N ≈ 1e2–1e4 quasi-independent events a coherent bias needs ε ≳ 1/√N ≈ **1e-2–1e-1** to beat the noise on one decision, or ~**1e-4–1e-3** if it can act consistently across ~1e4–1e6 synapses/decisions and let London-type amplification do the rest [G].
- **So the open window is roughly 1e-4 ≲ ε ≲ 1e-2 per event, internal to an awake brain, not transferable to external devices** (external devices are closed to ≲ 3e-5).
- **What would close it:** (i) release/gating statistics in awake vs anaesthetised preparations with N ≳ 1e6 events (ε sensitivity ~5e-4); (ii) a Hardy-type Bell test with space-like-separated human choices; (iii) checking whether such an internal bias would leak into any entangled external record, which the no-signalling theorems say it eventually must.
- **Cost of the loophole:** the bias must be aimable inside the skull but not outside it — a restriction no listed theory derives.
