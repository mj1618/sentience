# Response to the round 2 red team

Three independent reviewers attacked rounds 1 and 2 (`round2-physics-redteam.md`,
`round2-function-redteam.md`, `round2-logic-redteam.md`). "Re-run" = we reproduced it
ourselves; "accepted" = accepted on argument; "disputed" = did not reproduce or we disagree.

## Withdrawn

| Claim | Why | Status |
|---|---|---|
| "Chaos defeats a chooser; it would have to simulate the brain" (S4) | Artefact of nudging once. Nudging at every step: goal-only chooser holds 75–80% at any lead; wiring-aware chooser rises to 99.8%. Chaos *amplifies* a sustained bias. | re-run, confirmed |
| "Choosing without bias does nothing" (S4) | False dichotomy. A chooser can leave every single-event frequency at 50% and still steer by changing which events go together (+ε in one pool, −ε in the other). | accepted |
| "Open window is 10⁻⁴–10⁻²" (S4) | Our own table shows 10⁻⁸ suffices if widely pooled. Window is ~10⁻⁸–10⁻². No proposed experiment closes it. | accepted |
| "A one-way field is impossible" (S2 F2) | Only exactly zero back-action is forbidden. Very lopsided coupling is ordinary. F2 now rests on the report argument alone. | accepted |
| Experiment A as "feeling vs automaton" (S1) | It is learning vs no learning. The sim's own unfelt learner scores the same (0.364 vs 0.367). Crossover point moves 0.05–0.6 with cost, lifespan, exploration. | accepted (matches our own epi run) |
| Experiment J as evidence feeling is causal; the 2⁻ⁿ figure (S1) | Shows only "a gene with an effect is selected". Feelings share circuitry, so n is perhaps 1–3, not 20. | accepted |
| "The firewall explains why feelings seem ineffable" (S1 C) | The sim models *write* access. Ineffability is about *read* access, never modelled. People do regulate feelings (reappraisal, placebo, meditation). | accepted |
| "No single-system wiring fits the lab record" (S3) | One store keyed by (outcome, body state) with an innate salt prior passes 7/7. Adding three findings from our own brief (habits, instructed devaluation, reward-proximal responses) the interface wiring scores 7/10, same as readout. | accepted (not re-run) |
| "Imagined feelings should be fainter by design" (S3) | One gene set both how informative and how rewarding a preview is. Split them and evolution wants informative previews that are simply not credited as reward. Literature is mixed (people over-predict future feelings; anticipation is itself enjoyed). | accepted |
| "Lifetime novelty" prediction "corrected" (S5a) | The model does predict lifespan matters and the data refute it. Our rescue ("relative to the genome") cannot fail. Recorded as **failed**. | accepted |

## Weakened

| Claim | Change |
|---|---|
| Pushing-field shortfall "≥10⁸" (S2) | That used a 1%-of-kT-on-one-channel criterion while S4 let the chooser pool across the brain. Same generosity for both: shortfall is 10⁵·⁵–10¹³ by our pooling (re-run); reviewer's most extreme pooling gives ~10³. Still excluded. Below 10 nm it is closed by stellar cooling alone, which published models can evade. |
| Electron-coupled figure (S2) | Used the wrong bound; with the right one the conclusion is stronger, but the published number was wrong. |
| MRI and split-brain arguments against EM-field theories (S2 F4) | Fields add linearly, so a scanner does not erase the brain's own pattern; endogenous fields fade over millimetres, so they barely span the hemispheres anyway. Neither argument is fair to the actual theories. |
| "Why stop at the skull" (S4) | A chooser confined to the events that make up the experiencing system has a principled boundary. The single-photon result has no power. |
| The pincer as an elimination of epiphenomenalism (S0) | It is an argument about evidence, not a proof. Standard replies (direct acquaintance; common cause) were not addressed. It also bites inner-nature monism, which we did not penalise. |
| "Every surviving option hands back to organisation" | True of every option including the eliminated ones; "organisation" slides between function, causal structure and substance. Not a finding. |
| Option table A–F | Not exhaustive: missing emergentism, idealism, biological naturalism, integrated-information as its own class, higher-order theories, and "the question is mis-framed". |
| Experiment B | Our shared-slope scalar reaches 386–394 (re-run). Reviewer reports a 3-threshold rulebook at 392–398 and a 12-cell table at 381; our own 2-threshold rulebook reached only 320 at 5–8 needs (**disputed, unresolved**). Safe claim: what matters is combining body state with offer size; one scale is a compact way, not the only way. |
| Experiment C | Self-reward must be discounted *or* blocked; residual access is nearly free. |
| Third ingredient (S5b) | One of three live options, not forced. The depersonalisation study was a non-clinical online sample. |
| Scoreboard | Movements were mostly renormalisation. Reset below. |

## Holds

- No new *pushing* field (thinner margin).
- Arithmetic of the field table and bias table (independently recomputed).
- Albrecht–Phillips reading (thermal noise in water is quantum in origin).
- Readings of Balleine 1992 and Robinson & Berridge 2013 (at abstract level).
- A uniform potential on a whole neuron does no work on any switch.

## Lesson

Every simulation result that carried a conclusion was either true by construction or
reversed under a fairer baseline. From now on a sim result is not written into the
ledger until a reviewer has tried a stronger opponent and at least one parameter sweep.
