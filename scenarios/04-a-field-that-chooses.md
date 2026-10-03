# Scenario 4 — A field that chooses instead of pushes

> **Superseded in part.** Claims in this file were withdrawn or weakened on review (rounds 2–8). Read `reviews/round2-response.md` and `LEDGER.md` first; do not rely on the verdicts below.

Code: `sims/chooser.py`. Evidence: `research/07-quantum-outcome-bias.md`.
Prompted by the owner's notes: Scenario 2 showed a weak field cannot *push* warm matter.
But when a quantum event can go two ways at equal energy, picking one costs no energy.

## Conjecture

> Sentience is (or acts through) something that biases which way quantum events in the
> brain fall. Not a force: a change to the rule that sets quantum probabilities
> (the Born rule).

## Step 1 — Is there anything to choose between? Yes.

The notes' first hurdle was that brain randomness is thermal, not quantum. That hurdle
is lower than it looks. Albrecht & Phillips calculate that in water at body temperature
quantum uncertainty takes over molecular motion within **0.6 collisions**: the thermal
jiggling of molecules is quantum uncertainty, amplified. Ion-channel openings are driven
by that jiggling. And cortex amplifies single events: one extra spike produces ~28 more
(London 2010). So every channel opening is, at root, a quantum outcome, and single
outcomes can cascade. (A plausibility estimate, not a measurement; no rebuttal found.)

This does not need delicate quantum coherence in the brain. It needs only that
*which* outcome happens is not fixed in advance.

## Step 2 — Choosing without bias does nothing

If the chooser picks outcomes but keeps the usual odds, behaviour is statistically
identical with or without it. Then it could not have been favoured by evolution and
could not be why we reliably say "pain hurts". It fails the same two tests as
"feeling does nothing" (Scenario 0; Scenario 1 J). So the conjecture must mean a
**bias**: probability ½ becomes ½ + ε.

## Step 3 — How big a bias would matter?

Model a decision as two pools of micro-events; the pool with more "on" wins.

| System | Events involved | Bias needed for a 75:25 result, every event nudged correctly | …if only 1 in 1000 is |
|---|---|---|---|
| One neuron near threshold | 10⁴ | 2×10⁻³ | impossible |
| Small circuit, 0.1 s | 10⁸ | 2×10⁻⁵ | 2×10⁻² |
| Whole brain, 1 s | 10¹⁵ | 8×10⁻⁹ | 8×10⁻⁶ |

Cost: at ε = 10⁻³ across the whole brain the entropy bookkeeping is ~10⁻⁸ W.
Thermodynamics cannot see it. To detect ε = 10⁻³ needs ~6 million observed events.

**So small biases are enough in principle, if they are aimed.**

## Step 4 — The aiming problem

The brain is chaotic: small differences grow. We built a chaotic network of noisy
units, gave the chooser a 5% nudge on every unit at one moment, and asked how often it
got the outcome it wanted.

| Steps before the decision | Chooser knows only the goal | Chooser knows the wiring (linear approx.) |
|---|---|---|
| 0 | 80% | 80% |
| 1 | 49% | 73% |
| 2 | 45% | 70% |
| 3 | 51% | 66% |
| 5 | 49% | 59% |
| 8 | 52% | 53% |

(50% = no steering.)

**Reading.** A nudge is useful only at the last instant and only on exactly the right
events. One step earlier, a chooser that knows merely what it wants gets nothing. Even
knowing the full wiring diagram, influence fades to chance within about eight steps
(tens of milliseconds in a brain). To steer, the rule would have to take the brain's
particular wiring and current state as input and effectively simulate it forward.

That is a strange kind of physical law. It would have to "read" which arrangement of
matter counts as which thought. Which lands us where Scenario 2 did: the chooser cannot
work without already containing the answer to "which organisation matters?"

## Step 5 — What experiments already say

| Where the bias would be | Tested? | Limit |
|---|---|---|
| Quantum devices a person is trying to influence | Yes, hundreds of studies | ε ≲ 3×10⁻⁵; effect shrinks as studies grow; the three largest point the wrong way; the cleanest preregistered study (12,571 people) supports zero |
| Devices wired to give animals heat or shocks (Schmidt 1970) | Small, old | ε ≈ 10⁻²: cats "lucky", cockroaches *unlucky*; unreplicated |
| The form of the quantum rule in the lab | Yes | holds to 3×10⁻⁵, but this tests interference, not choosing |
| Events inside living nerve tissue | Barely | agrees with ordinary statistics only to ~1–10%, in dishes or under anaesthesia |
| Awake vs anaesthetised comparison | **Never** | — |

Two further theoretical costs. A bias that can be aimed, applied to linked (entangled)
particles, permits faster-than-light signalling. And none of the existing proposals
(Stapp, Chalmers & McQueen, Kent, Hardy) states a size for ε.

## Step 6 — Our own stress test: why stop at the skull?

If feeling biases outcomes toward what feels better, it should also bias a quantum coin
wired to deliver pleasure or pain: same feeling, same stake. That is closed to 3×10⁻⁵.
A chooser that works on a channel opening inside the head but not on a photon that
decides whether the same head gets a reward needs a principled boundary. No proposal
supplies one. And if any aimable bias existed, evolution should have built amplifiers
for it, making animals measurably luckier wherever quantum events matter to them. Human
single-photon vision performs at 51.6% ± 1.0% (Tinsley 2016), no sign of help.

## Verdict

**Not eliminated.** A window remains: a bias of roughly 10⁻⁴ to 10⁻² per event, only
inside an awake brain. It survives because nobody has looked there, not because anything
points to it. To be real it needs three things nobody has explained: a rule that reads
brain organisation, a reason it stops at the skull, and an escape from faster-than-light
signalling.

**Experiments that would close or open it**
1. Vesicle-release or channel statistics in awake vs anaesthetised tissue, ≥10⁷ events
   (sensitivity ~5×10⁻⁴). Difficulty: the baseline odds are biologically adjusted.
2. A large preregistered test with a quantum coin delivering real pleasant/unpleasant
   outcomes (the modern version of Schmidt's animal experiments).
3. Single-photon vision with reward riding on detection: does detection exceed the
   known capture efficiency of the eye?

**Correction to round 1.** Scenario 2 said "new field: out". That holds for fields that
push. The honest statement is: *pushing fields are out; a choosing rule is open but
costly*.
