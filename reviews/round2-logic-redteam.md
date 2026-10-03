# Round 2 red team — top-level logic

Reviewer: adversarial (philosophy of mind / science). 2026-10-03. Read: README, LEDGER,
scenarios 0–5, research/01, parts of research/02–03, `sims/valence_evolution.py` (exp J).
Web-checked: Li 2018 xenon ED50s (match PubMed); Robinson's common-cause reply (exists,
contested). Other [R]/[S] citations not checked.

## 1. Findings

| # | Claim attacked | Verdict | Why | Sev. | Fix |
|---|---|---|---|---|---|
| 1 | Pincer Jaw 1: "R2 is self-undermining, so sentience causes neurons" (C1 strong) | **BROKEN as an elimination** | (a) False dichotomy: "caused by" vs "accidentally about". Chalmers (1996 ch. 5; 2003): phenomenal beliefs are partly *constituted* by the experience (acquaintance), so justification is not causal. Robinson: report and feeling share a common neural cause, so reports covary lawfully with feelings. (b) It is an epistemic premise ("we would lack evidence") used for a metaphysical conclusion ("it is false"). (c) Self-inflicted wound: Scenario 1 point 4 says a firewalled planner reports ineffable feelings "whether or not they are", and research/01 constraint 11 says grounded self-report occurs in non-sentient systems. If so, report is weak evidence for any option, and Jaw 1 loses its force against E specifically. | High | Downgrade C1 to "moderate, conditional on a causal theory of phenomenal knowledge". Write the Chalmers/Robinson steelman and reply to it. |
| 2 | Jaw 1 applied only to E | **BROKEN (asymmetric)** | B: swap the quiddities, keep the structure, and every report is unchanged, so B faces the same paradox (Howell 2015). F satisfies Jaw 1 only by denying the thing. A satisfies it by stipulated identity. | High | Add a column "does Jaw 1 bite?" per option, honestly filled. |
| 3 | Experiment J eliminates E "twice over"; 2⁻ⁿ | **BROKEN** | In the code the "epi" arm sets `felt = 1.0*e` and lets `w` drift: chance alignment is true by construction, not a result. It refutes only law-free "free-floating" feelings, which no epiphenomenalist holds. The scenario's own "loophole" concedes this, then the ledger still books C4 against E. | High | Remove J as evidence against E. Keep as a demonstration about signals. |
| 4 | C4: character "fixed by the *functional role*" (strong) | **WEAKENED** | The loophole yields "fixed by the brain state". Functional role is one reading; substrate/causal-structure (IIT, Searle) is another. Functionalism is smuggled in at exactly this step. | High | Restate: "character supervenes lawfully on brain state". |
| 5 | Option table A–F is the space | **BROKEN (not exhaustive)** | See §3. No residual row. A conflates type identity with functionalism (opposite verdicts on AI). C is called "a special case of A" but is anti-functionalist. | High | Rebuild the table on two axes: ontology × what fixes the correlate (function / causal structure / substrate). |
| 6 | "Every surviving option hands the question back to which organisation" | **WEAKENED (artefact)** | True of *every* option including E and dualism: all accept neural correlates. So it is not a convergence produced by the eliminations; the eliminations do no work. "Organisation" equivocates between functional organisation, physical causal structure and material. The repo then tests only the first, by simulation. | High | Replace with: "all options need a correlate; they disagree whether it is multiply realisable." Make that disagreement the project's central test. |
| 7 | C2: shortfall ≥10⁸ | **WEAKENED (margin)** | Scenario 2 demands 1% kT per channel. Scenario 4 shows 8×10⁻⁹ bias per event suffices if coherent over 10¹⁵ events. A push changes open probability by ~δ/kT, so the required push drops ~6 orders. Generous shortfall at 1–10 nm becomes ~10²–10⁴, not 10⁸. Still excluded, but the stated margin contradicts the repo's own Scenario 4. | Medium | Recompute with coherent-sum threshold; state both. |
| 8 | C3: one-way coupling "not available in field theory" | **WEAKENED** | True of Lagrangian theories. Psychophysical laws need not be Lagrangian; assuming so begs the question against dualism. Its second leg is Jaw 1 (finding 1). | Medium | Scope the claim. |
| 9 | Scenario 4 "why stop at the skull" | **WEAKENED** | Assumes the chooser serves hedonic benefit anywhere. Stapp/Chalmers–McQueen act only on the system whose state is the experience: a principled boundary. Micro-PK data are then irrelevant to the in-brain window. | Medium | Drop PK bound as evidence against in-brain bias. |
| 10 | Affect-first favoured "by C8, C10, C11" | **WEAKENED** | C10: congenital insensitivity removes nociceptive *input* (Nav1.7), not just the feeling; shows signals matter. C11: Scenario 5 says the same patients are "awake and aware" with no affect, which is evidence *against* affect as the base of consciousness. Only C8 supports. | Medium | Re-score. |
| 11 | Scoreboard movements | **WEAKENED (overconfident)** | E 10→2 rests on findings 1–3. A/F 45→60 and B 25→30 are renormalisation, not evidence; B rises while declared untestable. Now-column sums to 99 with no "none of the above". | High | §2. |
| 12 | Toy sims rated as constraints on feeling | **WEAKENED** | C5–C7 are about reward signals. Scenario 5 already falsified C5's lifespan half and found the markers "cannot draw the line", yet the ledger is unchanged. C7→"explains ineffability" is an analogy: the sim has no reports. | Medium | Separate function-ledger from feeling-ledger. |
| 13 | LEDGER is current | **BROKEN (stale)** | Does not reflect Scenario 4's correction ("choosing rule is open"), Scenario 5's C5 correction, or the third term. | Low | Sync after every scenario. |
| 14 | C12 (valence gap); F1 pushing-field exclusion, qualitatively | HOLDS | F1 holds even after finding 7. | – | – |

## 2. Alternative scoreboard

| Family | Repo now | Mine | Reason |
|---|---|---|---|
| Epiphenomenalism / property dualism with psychophysical laws | 2 | 8 | Pincer and J do not touch the lawful version. Its real cost is inelegance. |
| Interactionist dualism (quantum-locus or non-conservative) | – | 2.5 | Scenario 4 leaves it open; aiming problem is a real cost. |
| New pushing field | 1 | 0.5 | Holds. |
| Quantum collapse / chooser | 3 | 3 | Unreplicated hints only. |
| EM field identity | 3 | 2 | Scenario 2 argument is fair. |
| Functional organisation (multiply realisable) | 60 (lumped) | 25 | |
| Substrate/causal-structure physicalism (biological naturalism, enactive, IIT-as-physicalism) | – | 12 | Never tested by the repo. |
| Illusionism | (lumped) | 8 | |
| Russellian monism / panpsychism | 30 | 15 | No evidence moved it; should not rise by default. |
| Idealism / non-Russellian neutral monism | – | 6 | |
| Question mis-framed / not yet conceived / mysterian | – | 18 | History of the field; C12 of research/01. |

## 3. Missing positions

| Position | Relative to pincer | Test |
|---|---|---|
| Lawful epiphenomenalism / naturalistic dualism (Chalmers) | Passes Jaw 2; Jaw 1 contested | None empirical |
| Interactionism where conservation fails locally (Cucu & Pitts 2019) or acts at indeterminacy | Rejects Jaw 2's premise | Scenario 4 experiments 1–3 |
| Strong emergence / downward causation (Broad, O'Connor) | Rejects Jaw 2: configurational laws | Deviations from micro-physics in large coherent tissue; none sought |
| Biological naturalism (Searle) | Passes both; denies function suffices | Functional isomorph in silicon lacks markers: currently untestable, so say so |
| Enactivism / autopoiesis (Thompson) | Passes both; correlate is the living organisation | Unicellular valence markers; anaesthetic action on paramecia (research/03 l.91) |
| IIT | Passes both; causal structure, not computation | Same function, feed-forward vs recurrent hardware |
| Higher-order theories | Under A, but predicts first-order valence is unfelt | Scenario 3's crux *is* HOT vs first-order; name it |
| Idealism (Kastrup) | Dissolves Jaw 2 | Only via dissociation-boundary predictions |
| Neutral monism (James, Mach); relational/QBist | As B without combination; QBism denies observer-independent closure | None yet |
| Mysterianism (McGinn) | Compatible; predicts permanent gap | Meta-induction over failed theories |

## 4. Owner's hypothesis

- **Not distinct.** "Affect is the base, cognition serves it" = Panksepp/Solms/Denton. "Feeling at the hand-over to the planner" = Dickinson & Balleine. The three-term version is the standard state/content split plus affect.
- **Strongest objections.** (i) The third term, "wakeful awareness", *is* phenomenality; the hard problem moved there, so "the hard question is sentience alone" is false by the repo's own Scenario 5. (ii) "+" is unspecified: additive, constitutive, or causal? (iii) Auto-activation patients were first cited as support (C11), then as the counterexample forcing a third term. A hypothesis that absorbs its counterexample by adding a term is degenerating.
- **Falsifiers to fix in advance.** Experience with intact report but abolished valence *and* thought (already found: amendment made post hoc). Remaining: valence-system lesions (PAG/hypothalamus) leaving wakeful perceptual report intact would kill "sentience is foundational"; a goal-directed devaluation with a sub-threshold reward would kill the interface refinement.

## 5. Method biases and fixes

1. **Streetlight.** Only simulable (hence functional) ideas get tested, then function wins. Fix: each scenario must include one test that could favour a non-functional option.
2. **Sims confirm their builder.** Fix: predictions and kill condition written before running; a second agent builds the rival sim.
3. **Report dependence** (Scenario 3 weakness 3). Fix: bridge-principle register: every function→feeling inference names its assumption.
4. **Elimination by absence or by definition.** Fix: "eliminated conditional on premise P"; a steelman file per dead option, written from its best published defence.
5. **Credence by renormalisation.** Fix: explicit likelihood ratios per update; a permanent residual row.
6. **LLM-compiled literature.** [R]/[S] items feed "strong" constraints. Fix: no constraint above "moderate" unless every supporting citation is [V] from a primary source.

## 6. New conjectures

1. **Analog-carrier.** Value is felt only where carried by slow volume transmission (opioid/peptide), not fast spikes. *Test:* literature check: does any manipulation change hedonic report without changing neuromodulator tone? One clean case kills it.
2. **Undischarged error.** Feeling is the integral term: evaluation that outlasts the action it triggers. *Test:* PID agents; does removing only the integral term reproduce asymbolia? Check whether withdrawal-resolved stimuli (<100 ms) are felt.
3. **Bottleneck count.** One subject per final arbitration bottleneck. *Test:* split-brain and octopus-arm literature: do hedonic conflicts double? If split-brain valence stays unitary, it fails.
4. **Compression residue.** Felt quality is what the self-model cannot represent of the valuation signal. *Test:* sim with self-models of varying capacity that emit reports; "ineffability" must shrink with capacity. Check expertise/meditation literature.
5. **Dissipation.** Sentience tracks irreversible metabolic work tied to evaluation. *Test:* calculation: generalised seizures are hypermetabolic and unconscious; ketamine is the reverse. Likely fails fast.
6. **Temporal gap.** Feeling exists to hold a token across a delay for credit assignment. *Test:* trace vs delay conditioning and awareness (Clark & Squire 1998 and its failed replications).
7. **Not a natural kind.** "Sentience" is a cluster with no single origin. *Test:* do pain, hunger, itch, pleasure vanish at one anaesthetic/PCI threshold or piecemeal? Piecemeal loss dissolves the project's question.
