# Round 2 — physics red team

Reviewed 2026-10-03. Scope: scenarios 00/02/04, `sims/field_constraints.py`, `sims/chooser.py`, research 02/07.
Check scripts (not in repo): session scratchpad `check.py`, `chaos2.py`. Tags: **[C]** computed here, **[W]** looked up (URL given), **[R]** recalled, not checked.

Bottom line: the F1 verdict (no pushing field) survives, but with a far thinner and more model-dependent margin than "10⁸–10²²". Three other claims are wrong as stated: the one-way-field impossibility, "unbiased choosing does nothing", and the aiming-problem result, which is an artefact of the sim design.

## Findings

| # | Claim attacked | Verdict | Why | Sev | Suggested fix |
|---|---|---|---|---|---|
| 1 | Jaw 1: R2 is self-undermining, so sentience causally influences neurons | WEAKENED | The argument is epistemic (our reports would not be evidence), not a proof that R2 is false. It also presupposes sentience is a separate thing that "influences"; under A/B/F it *is* the neural process, so there is no pincer on them. Acquaintance and common-cause replies are not addressed. | med | Restate as "reports must be explained by whatever sentience is"; label it a premise, not a result. |
| 2 | Jaw 2: neuron physics "known and tested to many decimal places" | WEAKENED | Precision tests are on few-body systems. In tissue, the repo's own numbers give energy balance only to ~1 W and event statistics to 1–10%. Closure is an EFT extrapolation that assumes locality and no configuration-dependent law; it says nothing on outcome selection or boundary conditions. | med | Say "no room for a new local force" and list the assumptions. |
| 3 | Criterion "≥1% of kT on one channel" is generous | BROKEN | Not a floor. (a) Scenario 4 grants the chooser √N pooling (ε = 8×10⁻⁹ at N = 10¹⁵), which is equivalent to ΔE = 4εkT ≈ 3×10⁻⁸ kT per channel; Scenario 2 denies the pusher the same gain. (b) Radical-pair sensors respond at 1.1×10⁻⁷ kT per spin [C]. (c) Networks respond to 0.5 mV/mm, about 0.07 kT per channel [C]. | high | Use one criterion in both scenarios; report shortfalls under the pooled one. |
| 4 | F1 shortfall "at least eight powers of ten" | WEAKENED | Under the pooled criterion the minimum shortfall is 10²·⁸ (10 nm), not 10⁸ [C]. At 1–10 nm the lab-only shortfall is a factor of 37 under the 1% criterion, and the field *passes by 10⁴* under the pooled one. Everything there rests on stellar cooling. | high | Publish both columns; state that 1–10 nm is closed by stars alone. |
| 5 | Stellar cap applied correctly | WEAKENED | Arithmetic is right (α = 1.7×10¹³ [C]) and the mass range is right (m ≪ keV). But the bound is evadable by environment-dependent mass or coupling; a minimal model evading all stellar bounds exists [W] https://arxiv.org/abs/2006.15112 . The repo dismisses screening in one clause, with no calculation. | med | Add a row "if stellar bounds are evaded"; compute chameleon/symmetron range at tissue density. |
| 6 | Electron-coupled scalar: "< 0.001 kT" | WEAKENED | Reproduced: 3.7×10⁻⁴ kT [C]. That is only 27× below the repo's own 1% criterion and 10⁴× *above* the pooled one. The conclusion is saved only because the wrong bound was used: at 5 cm range torsion balances, not stars, apply, giving ~2×10⁻¹³ kT [C]. | med | Use the lab bound at that range; delete the stellar-limit figure. |
| 7 | Lab bounds at 100 nm (10¹¹) and 1 µm (10⁷) | UNCHECKED | Read off a figure; the abstract confirms only "40–8000 nm, up to 10³ improvement" [W] https://arxiv.org/abs/1410.7267 . If the 100 nm value is really ~10¹³, the stellar cap takes over and the shortfall drops ~2 orders. | med | Get tabulated values. |
| 8 | Target = single channel; no N gain | HOLDS | A whole-neuron or whole-brain target only gains a uniform potential shift, which does no work on any gating variable. A mechanical route also fails: brain self-attraction × α = 10⁻³ is 4×10⁻¹¹ m/s² [C], against a vestibular threshold of ~10⁻² [R]. Also missed in the repo's favour: a field sourced by static tissue mass carries no signal. | low | Add these two lines. |
| 9 | Table covers "charge-like but not EM" | WEAKENED | A dark photon coupling to charge is outside the neutral-matter Yukawa framework entirely. It is closed, but by a different argument: mixing ≲ 10⁻⁷ [R] gives 10⁻¹⁴ × the 1.3 eV gating work = 5×10⁻¹³ kT [C]. Spin-coupled fields are listed in research/02 but never propagated to a neural sensitivity. | med | Add dark-photon and spin-coupled rows, the latter against the radical-pair threshold. |
| 10 | F2: one-way coupling "is not available" in field theory | BROKEN | True only for exactly zero back-reaction in a Lagrangian theory. Arbitrarily asymmetric coupling is the generic weak-coupling limit: the field's record of matter scales with g·(source), while the back-reaction on matter can sit far below thermal noise. Non-Lagrangian and hybrid classical–quantum dynamics also exist. F2 falls to Jaw 1 alone, which is a philosophical premise. | med | Drop the physics claim; rest F2 on Jaw 1 and say so. |
| 11 | F4 MRI argument | WEAKENED | Numbers are fine: RF E-field ~600 V/m against 1–5 V/m endogenous; 3 T is 6×10⁴ × Earth's field and 3×10¹³ × the brain's own [C]. But Maxwell is linear: an added uniform or 128 MHz field does not erase the brain-generated spatial pattern, which is what Pockett identifies with experience [W] https://loc.closertotruth.com/theory/pockett-s-conscious-and-non-conscious-patterns . The argument only hits "total field amplitude = experience", which nobody holds. | med | Aim at pattern identity; use in-band perturbations (tACS, gradient switching at ~2.5 V/m, kHz). |
| 12 | F4 split-brain: "the field still spans the cut" | WEAKENED | Endogenous fields fall off over millimetres; at centimetres they are far below the 0.5 mV/mm threshold. The field barely couples the hemispheres with or without the cut, so the observation does not discriminate. McFadden is causal, Pockett is not [W] https://en.wikipedia.org/wiki/Electromagnetic_theories_of_consciousness ; the two need separate treatment. | med | Compute inter-hemisphere field strength; treat the two theories separately. |
| 13 | S4 step 2: no bias means no effect | BROKEN | False dichotomy. (a) Choosing which observable and when (Stapp, Zeno) changes dynamics with exact Born outcomes; it fails on decoherence, a different reason. (b) In the repo's own two-pool model the aggregate "on" frequency stays at 50%: the bias is +ε in one pool and −ε in the other. Marginal statistics are untouched; only role-conditioned statistics move. | high | Replace with three cases: outcome bias, question or timing choice, role-conditioned selection. |
| 14 | Two-pool numbers | HOLDS (arithmetic) / WEAKENED (model) | Reproduced 2.4×10⁻³, 2.4×10⁻⁵, 7.5×10⁻⁹ [C]; the formula assumes N per pool, a √2 ambiguity. Independence and a perfect linear readout are assumed, and only intrinsic noise is beaten, so these are lower bounds. The 10¹⁸ events/s figure is unsourced. | low | State the assumptions. |
| 15 | Verdict window "10⁻⁴ to 10⁻²" and "experiments that would close it" | BROKEN | The repo's own table says 8×10⁻⁹ to 2×10⁻⁵ suffices, so the window is ~10⁻⁸ to 10⁻². Experiment 1 reaches 8×10⁻⁴ at 5σ with 10⁷ events [C], closing 1.5 of ~6 decades. By finding 13b it also measures the wrong quantity unless each event's sign is known in advance. | high | Correct the window; say plainly that no proposed experiment closes it. |
| 16 | Aiming problem: "influence fades to chance within about eight steps" | BROKEN | Artefact of a one-shot nudge. Same network, same 5% bias applied at every step [C]: goal-only chooser 77% at every lead time; wiring-aware chooser 92%, 97%, 99%, 99.9% at leads 1, 2, 3, 5; still 99% at lead 8 with the final step excluded. Chaos amplifies a sustained bias. At ε = 0.005: 67% sustained against 51% one-shot. Near criticality (g = 1): goal-only 87%. | high | Rerun with sustained bias; withdraw "must simulate the brain forward". The residual requirement is knowing the readout. |
| 17 | "Why stop at the skull" | WEAKENED | Assumes a chooser that favours future pleasant outcomes anywhere. A chooser confined to events that constitute the experiencing system has a principled boundary. The 3×10⁻⁵ bound comes from intention experiments, mostly with no hedonic stake. Tinsley's 51.6 ± 1.0% has no power below ε ≈ 10⁻² and no capture-efficiency baseline, so it is not evidence. | med | Split "teleological" from "substrate-local"; drop Tinsley. |
| 18 | "Choosing costs nothing"; entropy cost 10⁻⁸ W | WEAKENED | Reproduced 8.6×10⁻⁹ W [C]. But gating states differ by many kT; a sustained aimed bias is a Maxwell demon. The figure is a second-law violation rate, not a cost paid. | low | Reword. |
| 19 | Albrecht–Phillips reading | HOLDS | n_Q reproduced: water 0.55, air −0.35 [C]. Interpretation-dependent: nothing to choose in Everett; in Bohm the chooser is the initial distribution. | low | Note this. |
| 20 | Faster-than-light signalling cost | HOLDS | Biasing one side of an anticorrelated pair shifts the remote marginal. Not fatal to consistency: signalling non-equilibrium Bohmian theories exist. | low | — |

## Independent recomputations [C]

| Quantity | Repo | Mine |
|---|---|---|
| kT at 310 K | 27 meV | 26.7 meV |
| α needed, 1 nm / 10 nm / 10 µm / 10 cm (1% kT) | 4×10²³ / 4×10²¹ / 4×10¹⁵ / 10⁸ | 3.7×10²³ / 3.7×10²¹ / 3.7×10¹⁵ / 1.1×10⁸ |
| Shortfall, 1% kT, with stellar cap (orders) | 10.3 / 8.3 / 11.4 / 11.0 | same |
| Shortfall, lab bounds only | not given | 1.6 / 1.6 / 11.4 / 11.0 |
| Shortfall, pooled criterion (3×10⁻⁸ kT) | not given | 4.8 / 2.8 / 5.9 / 5.5 |
| Pooled criterion, lab only | not given | −4.0 / −4.0 (passes) / 5.9 / 5.5 |
| Electron-coupled, stellar g_e | < 0.001 kT | 3.7×10⁻⁴ kT |
| Same range, lab cap α = 10⁻³ | not given | 1.8×10⁻¹³ kT |
| Chaos, one-shot, leads 0/1/3/8 (naive; linear) | 80, 49, 51, 52; 80, 73, 66, 53 | 80, 48, 50, 51; 80, 72, 66, 55 |
| Chaos, sustained (naive; linear) | not run | 80, 78, 77, 77; 80, 92, 99, 99.9 |

The exact Yukawa integral over a uniform medium gives 4πρλ²Gm, three times the repo's sphere estimate. A uniform medium, though, gives no energy *difference* between channel states, so the "generous" column is more generous than stated.

## Not considered at all

1. **Sustained or role-conditioned selection with exact marginals** (finding 13b). Test: role-labelled event statistics; aggregate frequency tests are blind to it.
2. **Bohmian quantum non-equilibrium (Valentini)**, cited in research/07 but never gamed out. Test: sub-Born or super-Born variance in tissue; signalling in entangled pairs.
3. **Retrocausal / two-state-vector / final boundary condition.** Outcomes fixed by a future constraint, so there is no forward aiming problem. Test: post-selection anomalies in weak measurements on living tissue.
4. **Strong emergence: configuration-dependent law with no new field** (Carroll's loophole (a), listed and then dropped). Test: precision energy and momentum balance in awake brain; the current bound is ~1 W.
5. **Superdeterminism / correlated initial conditions.** Test: Hardy-type Bell test with human-driven settings.
6. **Hybrid classical–quantum dynamics** (stochastic classical field sourced by quantum matter; the effectively one-way case). Test: anomalous heating and decoherence bounds.
7. **Fields sourced by organisation, not by mass or electron number.** Source-side lab bounds are void; only the target coupling is capped, by stars. Test: a detector beside an awake brain.
8. **Large-amplitude background fields.** The shift is g·φ; φ is bounded by energy density, not by g. Test: atomic-clock and equivalence-principle bounds near a head.
9. **Spin-coupled fields acting on radical pairs or nuclear spins.** Test: replicate the xenon isotope result; comagnetometer near tissue.
10. **Criticality and stochastic resonance** as amplifiers of sub-thermal coherent inputs. Test: a measured cortical susceptibility to tACS sets the gain.
11. **Collapse timing with exact Born statistics** (Chalmers–McQueen, non-radiating Penrose collapse). In a decohered brain this changes no behaviour, so it fails Jaw 1; the repo never notices. Test: interference in Φ-superposed devices.
12. **Screened fields, done quantitatively**, and **mediators with range under 0.01 nm** acting inside nuclei. Test: atom-interferometry bounds mapped to tissue density.
13. **Information-theoretic or constructor-theoretic laws** constraining which transformations are possible. No dynamical signature; testable only if they forbid an otherwise allowed process.
14. **Psychophysical laws without force** (lawful supervenience). Untestable by physics; relevant because it answers the Jaw 1 evolution argument.
