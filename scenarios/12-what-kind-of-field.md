# Scenario 12 — If sentience were a field, what would be its source?

Code: `sims/field_sources.py`. Our own analysis. Status: **reviewed; read the red-team outcome at the end first.**

The owner's original question included: *if it is a field, what kind could it be, and
can any kinds be eliminated?* Rounds 1–3 dealt with how a field could act on a brain.
This scenario asks the other half: what would produce it.

## Conjecture

> Brains produce a "sentience field" because of something they have a lot of.

In physics a field is produced by the local amount of some quantity, added up over
space: mass produces gravity, charge produces the electric field. So the conjecture
needs a quantity. We try each candidate and ask who else has it.

## Test — who else has it?

Amount of each candidate quantity, relative to one human brain (order of magnitude):

| | Mass | Energy being dissipated | Energy stored in electric fields | Irreversible switching events per second |
|---|---|---|---|---|
| Your brain | 1 | 1 | 1 | 1 |
| Your liver | 1 | 1 | 1 | 0 |
| Laptop processor | 0.04 | 1.5 | 0.002 | 1,000 |
| Phone battery and capacitors | 0.04 | 0.1 | 17 | 10 |
| Boiling kettle | 1 | 100 | 0 | 0 |
| Car engine | 100 | 2,500 | 0 | 0 |
| Data centre | 700,000 | 1,500,000 | 17,000 | 100,000,000 |
| The Sun | 10³⁰ | 10²⁵ | — | — |

For a long-range field, what matters at your head is each source's amount divided by
its distance. On that measure the Sun out-contributes your own brain by 10¹⁷ for mass
and 10¹² for energy dissipation; the Earth by 10¹⁶ and 10⁴.

**Reading.** Whatever additive quantity is chosen, brains are unremarkable. Livers
match them on everything except signalling. Kettles beat them on energy flow, phones on
stored electric energy, processors on switching. A field produced by any of these would
be produced far more strongly by things nobody takes to be sentient, and a long-range
one would be swamped at your own head by the Sun.

So if there is a sentience field in the ordinary physical sense, either

1. kettles, phone batteries and stars are its main sources (a form of panpsychism with
   odd consequences: the feeling-field at your head would be mostly the Sun's), or
2. its source is not an amount of anything but a *pattern*: how the activity is
   arranged.

## The pattern option and why it is not an ordinary field

"How activity is arranged" is not a local density that can be added up point by point.
It depends on relations between distant parts at one moment, and "at one moment" is not
well defined across space in relativity. A fundamental field cannot take that as its
source without giving up locality.

There is a kind of field in physics that *is* about arrangement: an **emergent** one.
Magnetisation in a magnet is a field. It is not a new fundamental thing; it is the
collective alignment of atoms, and it appears suddenly at a phase transition (iron
becomes magnetic below a certain temperature). Temperature and pressure are fields of
this kind too.

## Refined conjecture

> If sentience is a field, it is an emergent one: a collective state of brain activity
> that switches on at a phase transition, the way magnetisation does.

This one makes checkable predictions, because phase transitions have signatures:

| Signature | What it would look like | Status |
|---|---|---|
| Hysteresis | Consciousness is lost at a higher anaesthetic dose than the dose at which it returns | Reported ("neural inertia"); **to be verified** |
| Critical slowing | Brain activity recovers more slowly from small disturbances just before the switch | Reported for anaesthesia and for mood switches; **to be verified** |
| Peak responsiveness at the edge | Response to a small prod is largest near the transition | To be checked against brain-stimulation complexity measures |
| Universality | The same transition in a different material would produce the same collective state | Untestable now; this is where "function is enough" and "the material matters" would part ways |

And for feeling specifically, a bolder version: **good and bad are the two directions of
one such collective state** (approach and withdraw), the way a magnet can point up or
down, with neutral as the unaligned state. That predicts mood should be sticky, should
show slowing before it flips, and that strong good and strong bad should not coexist.
The last is doubtful: people report mixed feelings.

## Verdict (provisional, unreviewed)

- Fundamental field produced by an additive quantity: **eliminated on our numbers**,
  unless one accepts that stars and kettles are the main sources.
- Fundamental field produced by a pattern: **not available without breaking locality.**
- Emergent collective state: **live, and testable.** It is not a rival to "organisation
  of ordinary matter"; it is a specific, physics-style version of it.

## To be attacked by reviewers

Frequency-selective sources (a field that responds only to rhythms in a certain band:
then mains electricity dominates?). Sources defined by correlation rather than amount.
Whether "pattern cannot source a local field" is actually true (order parameters are
local). Whether the phase-transition signatures are specific to consciousness or are
found in any drug-receptor system.

---

> **Red-team outcome (round 5).** All three verdicts above are withdrawn. What stands: four crude quantities do not single out brains. See `reviews/round5-response.md`.
