# Scenario 7 — Could a "chooser" ever be caught?

Evidence: `research/10-detecting-a-chooser.md`. Follows Scenario 4.
Status: **reviewed; see the red-team outcome at the end before relying on anything here.**

Round 2 left open a chooser that tilts quantum-random events inside an awake brain by
somewhere between 10⁻⁸ and 10⁻² per event. Question: what measurement could find it or
rule it out?

## 1. Counting events cannot reach the bottom of the window

To see a tilt ε at five standard deviations you need about (2.5/ε)² events.

| Method | Events obtainable | Smallest tilt detectable |
|---|---|---|
| Light-sensor imaging of single synaptic releases in a living mouse | ~10⁵ per session, ~10⁷ per 100 sessions | 8×10⁻⁴ |
| Multi-electrode probes (largest public dataset: 621,733 neurons) | ~10¹⁰ spikes | 2.5×10⁻⁵ |
| What 10⁻⁸ would need | 6×10¹⁶ | not achievable |

So only the top of the window (10⁻⁵ to 10⁻²) can be reached by counting at all.

## 2. Inside tissue there is no fixed baseline to compare against

A coin's fairness can be tested because physics says it should be 50:50. A synapse's
release probability is whatever biology has set it to, and brain chemistry shifts it by
far more than 10⁻³ from moment to moment. A chooser's tilt and an ordinary chemical
adjustment look the same. The subtler chooser (single events untouched, co-occurrences
changed) hides behind the fact that ordinary networks also create co-occurrences.

One published observation is worth flagging. In monkeys judging ambiguous images,
single neurons' random fluctuations predict the animal's choice slightly better than
chance ("choice probability", about 0.55). That is literally "noise correlated with the
decision". Network models explain it as ordinary feedback, and no anomaly is known, but
the feedback part has never been fully accounted for from measured brain state.
A null result from auditing this in public data would be informative; a positive would
not, because unmeasured ordinary signals mimic a chooser.

**Our conclusion:** a chooser confined to biological events is, in practice, not
testable by counting. That is a mark against it as science, not evidence for it.

## 3. Where physics does fix the odds

The only clean tests are ones where the expected odds come from physics and biology
cannot tune them.

| Test | What it would show | Reach | Feasibility |
|---|---|---|---|
| **Xenon isotopes.** Atoms identical in chemistry, differing only in the spin of the nucleus. One 2018 study in mice found the spinning kinds were ~30% weaker anaesthetics. | That a quantum property with no chemical effect reaches behaviour. Not a chooser test, but the precondition for every quantum theory of mind. | Decisive with ~13 mice per gas if the published error bars are standard errors (our power calculation; the original used 20) | High. Tens of litres of gas at roughly $250 per litre. **Never replicated in eight years.** |
| **Quantum link in the loop** (our design). Put a physics-fixed 50:50 quantum event inside an animal's own decision loop: recorded brain activity passes through a quantum coin before stimulating the next area, with reward depending on the outcome. | Whether a chooser acts on events that are functionally part of the brain but not biological. | 10⁹ events → 8×10⁻⁵ | Medium; all parts exist. A null leaves a "biology-only" chooser alive. |
| **Human-chosen settings in entanglement experiments.** 97 million human choices already recorded. | Faster-than-light signalling, which some chooser variants predict. | 2.5×10⁻⁴ on existing data | High for re-analysis |
| **A sensor beside an awake brain** that ignores electrical currents, cycling the animal between awake and anaesthetised. | A field produced by brain *organisation* instead of mass or charge. | Unknown | Medium; apparently never tried |

## 4. Verdict

- The chooser cannot be eliminated and, in its biology-only form, cannot presently be
  tested. It stays on the board at low weight as an idea with no evidence and no way in.
- The **xenon replication** is the most valuable cheap experiment we have found in this
  whole project. If it fails to replicate, every quantum route loses its only positive
  hint. If it replicates, the picture changes for everyone.

---

> **Red-team outcome (round 3).** Sections 1–2 and the xenon paragraph are withdrawn. A future-aimed or hidden-fact-aimed chooser is testable with a randomised read-out and is already closed by large precognition replications; a state-local chooser is indistinguishable from biology and is left unscored. Details: `reviews/round3-response.md`.
