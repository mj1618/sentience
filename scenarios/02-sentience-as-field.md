# Scenario 2 — Is sentience a field?

Code: `sims/field_constraints.py`. Sources and numbers: `research/02-physics-constraints.md`.

A field is something with a value at every point in space (like the magnetic field).
"Sentience is a field" can mean six different things. We take each and ask what it
implies and whether anything rules it out.

## The test every version must pass

From Scenario 0: sentience has to affect neurons (we talk about it). A neuron's
switches are ion channels. To flip or bias one, an influence must shift its energy by
something comparable to thermal jostling, **kT ≈ 27 meV** at body temperature. We are
generous and ask only for 1% of kT, on the theory that networks amplify small nudges.

## F1 — A new field that pulls on ordinary matter

A field's reach and the mass of its particle are tied together: reach = ħ/(mc). To span
a synapse the particle must be lighter than ~10 eV; to span the brain, lighter than
~2 µeV. Light fields that pull on ordinary matter are exactly what "fifth-force"
experiments hunt for.

Result of the calculation (strength in units of gravity; "shortfall" = how many powers
of ten too weak the strongest *allowed* force is):

| Reach | Brain structure | Strength needed (generous) | Strength allowed | Set by | Shortfall (generous) | Shortfall (realistic) |
|---|---|---|---|---|---|---|
| 1 nm | one protein | 4×10²³ | 2×10¹³ | stars | 10¹⁰ | 10¹² |
| 10 nm | synaptic cleft | 4×10²¹ | 2×10¹³ | stars | 10⁸ | 10¹¹ |
| 100 nm | synapse | 4×10¹⁹ | ~10¹¹ | Casimir-type lab tests | 10⁹ | 10¹³ |
| 1 µm | dendrite | 4×10¹⁷ | ~10⁷ | same | 10¹¹ | 10¹⁶ |
| 10 µm | neuron | 4×10¹⁵ | 1.4×10⁴ | Stanford cantilever | 10¹¹ | 10¹⁷ |
| 0.1 mm | cortical column | 4×10¹³ | ~10⁻¹ | torsion balance | 10¹⁵ | 10²² |
| 1 mm | cortical thickness | 4×10¹¹ | ~10⁻³ | torsion balance | 10¹⁵ | 10²³ |
| 1 cm | brain region | 4×10⁹ | 2×10⁻⁴ | torsion balance | 10¹³ | 10²² |
| 10 cm | whole brain | 10⁸ | ~10⁻³ | torsion balance | 10¹¹ | 10²¹ |

("Realistic" uses the work the force does over the ~1 nm an ion-channel sensor moves,
not the whole potential. Allowed values are order-of-magnitude; the 0.1 mm lab figure is
an unsourced estimate bracketed by exact values either side.)

**Reading.** At every reach from a single protein to the whole brain, the strongest
new matter-coupled force still permitted is too weak by at least **eight powers of ten**
(a hundred million times) even on generous assumptions, and typically by eleven to
twenty-two. Laboratory tests alone leave a gap below ~10 nm; stars close it, because a
light particle coupling to atomic nuclei that strongly would let stars cool faster than
they do. What remains is fields whose reach is smaller than an atom (cannot connect
anything) or exotic "screened" fields that hide in dense matter (would hide in a brain
too).

A light field that couples to electrons specifically is squeezed harder still: stellar
limits leave it ≲5×10⁻³⁰ the strength of ordinary electric force. Even with every
electron in the brain pulling together on one channel, the nudge is < 0.001 kT.

**Loopholes that remain** (Carroll's argument and ours cover fields of the ordinary
kind): changes to quantum mechanics itself (F5), laws that depend on the whole
configuration non-locally, and inner-nature views (F6).

**Verdict: F1 eliminated for any brain-spanning or cell-spanning role.** (Strong.)

## F2 — A field matter writes to but that never pushes back

Attractive because it dodges F1. Two problems. In the mathematics of field theory the
same term that lets matter disturb a field lets the field disturb matter; a one-way
coupling is not available. And a field that never pushes back cannot cause our talk
about feelings, so it fails Scenario 0. **Eliminated.** (Strong.)

## F3 — A universal field the brain "tunes into" (receiver theory)

A receiver needs an antenna, which is a coupling, which is F1 again. Separately: brain
injuries remove *specific* feelings (the hurt of pain while leaving the sensation; see
`research/03`). So the content of every feeling is fixed by brain organisation and the
field would supply only a contentless "glow". Nothing we could ever observe would differ
if the glow were absent. **Not eliminated outright, but does no work.** (Moderate.)

## F4 — Sentience is the brain's electromagnetic field

No new physics: neurons make electric fields (about 1–5 mV/mm) and are slightly
sensitive to them. Game out the identity claim:

- **MRI.** A scanner adds a static field ~100,000× Earth's, plus radio-frequency fields
  whose electric component is far larger than the brain's own. Experience barely
  changes. Defence: neurons do not respond at those frequencies. But that defence says
  the only part of the field that counts is the part *neurons can read*.
- **One field, many minds.** There is one electromagnetic field in the universe and it
  runs continuously through everyone's head. What draws the boundary of a mind? Again:
  what each brain's neurons can read.
- **Split brain.** Cutting the fibres between hemispheres splits certain aspects of
  experience although the field still spans the cut.

**Reading.** Each defence hands the real work back to neural organisation. The field
may be part of the mechanism (a fast, wireless way for neurons to coordinate), but
"which bits of the field count" is settled by function. **F4 survives only as a
functional theory in disguise.** (Moderate; our own argument.)

## F5 — Not a new field but new quantum behaviour (collapse theories)

Penrose–Hameroff "Orch-OR": experience is tied to the collapse of quantum
superpositions in microtubules (protein scaffolding inside neurons). This is the one
family with real experiments. Status:

- **Against.** Quantum states in warm wet tissue should fall apart in ~10⁻¹³ s, ten
  powers of ten faster than neurons work (Tegmark). Defenders compute 10⁻⁵–10⁻¹ s;
  nobody has measured it. The simplest, parameter-free version of the collapse physics
  was **ruled out** underground at Gran Sasso in 2021 (predicted radiation not seen).
  Surviving versions have an adjustable parameter and make no firm prediction.
- **Hints for (all single-lab, unreplicated).** Xenon isotopes that differ only in
  nuclear spin were reported to differ ~45% in anaesthetic potency (Li 2018). A
  microtubule-stabilising drug delayed anaesthesia in 8 rats by 69 s (Wiest 2024).
  Anaesthetics shortened energy transport along microtubules by 12–15% in a dish
  (Kalra 2023). Lithium isotope results are mixed.

**Verdict: unlikely, but the only door physics leaves ajar, and cheap to test.** The
xenon result is the one to watch: chemistry says isotopes should behave identically.

## F6 — Field as inner nature (Russellian monism / panpsychism)

Every physical field already has an experiential inner aspect; physics only describes
its outward behaviour. Adds no forces, so nothing above touches it, and no physics
experiment ever can. Its whole burden moves to: why is a brain one big feeling and a
rock not? That is, once more, a question about organisation.

## What this scenario gives us

1. **A new matter-coupled field cannot be the carrier of sentience** at any scale that
   connects neurons. Our numbers put the shortfall at 10⁸–10²².
2. **Convergence.** F3, F4 and F6 all survive only by passing the question to "which
   organisation of the brain?" Combined with Scenario 0, every surviving route leads to
   the same place.
3. **Where an experiment could still surprise us.** Only F5. The cleanest probes are
   isotope experiments: swap an atom for a chemically identical one with different
   nuclear spin and see whether anaesthesia or behaviour changes. Ordinary neuroscience
   predicts no difference; any solid difference would be a crack in the wall.
