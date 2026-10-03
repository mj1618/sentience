# Scenario 1 — Does sentience beat an equally clever automaton?

Code: `sims/valence_evolution.py`. Raw results: `sims/out/valence_evolution.json`.

**What these simulations can and cannot show.** They model an internal good/bad signal
("valence") as a working part. They cannot show that the signal is *felt*. They show
what evolution demands of such a signal, which constrains what sentience must be like
if sentience is the thing doing this job.

## First, a logic point that reshapes the question

"An automaton that is equally intelligent" hides a fork:

- If it behaves identically in every situation, natural selection cannot tell the two
  apart. Then sentience was never selected *for*, and we are in epiphenomenalism
  (eliminated in Scenario 0 and by experiment J below).
- If sentience makes a behavioural difference, the automaton is by definition *not*
  equally capable somewhere. The question becomes: where?

So the useful version of the question is: **what jobs need a valence-like signal, and
can those jobs be done without one?**

## Experiment A — Reflex automaton vs valence learner

World: 8 kinds of thing, each helpful or harmful. "Volatility" is the chance that a
thing's effect differs from what it was for one's ancestors. The reflex automaton has
evolved, hardwired approach/avoid rules. The valence learner feels the outcome and
adjusts within its lifetime, paying a running cost and an exploration cost.

| Volatility | Reflex | Valence learner | Learner share when competing |
|---|---|---|---|
| 0.00 | **0.50** | 0.42 | 1% |
| 0.05 | **0.47** | 0.41 | 1% |
| 0.10 | **0.44** | 0.40 | 2% |
| 0.20 | **0.39** | 0.38 | 4% |
| 0.40 | 0.29 | **0.37** | 98% |
| 0.70 | 0.13 | **0.36** | 99% |
| 1.00 | 0.00 | **0.36** | 98% |

(Fitness per step; maximum 0.5.)

**Reading.** In a stable world the automaton *wins*. Valence pays only when the world
changes faster than genes can track. The switch is sharp, between 20% and 40% volatility
with these costs. Known in outline (Baldwin effect; Singh, Lewis & Barto on evolved
rewards), but it gives a prediction: creatures in very stable niches with short lives
have no selective reason to feel. Sentience should track *lifetime novelty*, not
intelligence or complexity as such.

## Experiment J — Why does good-for-you feel good?

William James's 1879 argument, run as an experiment. Each learner has a gene `w` setting
how outcomes feel (positive: benefit feels good; negative: benefit feels bad).

| Model | Runs ending with feeling aligned to benefit | Mean `w` |
|---|---|---|
| Feeling drives learning (causal) | **40 / 40** | +0.97 |
| Feeling present but does nothing (epiphenomenal) | 22 / 40 (chance) | +0.01 |

**Reading.** If feeling is causal, alignment is automatic. If feeling does nothing,
alignment is a coin flip *per feeling*. Humans have dozens of independently aligned
feelings (pain, hunger, thirst, nausea, warmth, itch, suffocation, sweetness, orgasm…).
With n independent feelings the chance of full alignment by luck is 2⁻ⁿ; for n = 20
that is one in a million.

*Loophole (important):* an epiphenomenalist can say a law of nature ties the *kind* of
feeling to the functional role of the brain state. Then alignment is guaranteed again.
But that concedes what matters here: **the character of a feeling is fixed by what the
state does.** Free-floating feelings are ruled out; feeling is welded to function.

## Experiment B — Many needs: one currency vs a rulebook

Agents juggle n needs (food, water, …), die if any hits zero, and choose among offers of
varying size. Survival time out of 400:

| Needs | Biggest offer (ignore body) | Most depleted need (ignore offers) | Priority rulebook | Common-currency valence |
|---|---|---|---|---|
| 2 | 180 | 55 | 358 | **380** |
| 3 | 84 | 38 | 320 | **373** |
| 5 | 41 | 41 | 257 | **370** |
| 8 | 35 | 53 | 232 | **371** |

**Reading.** With two needs a rulebook automaton is nearly as good. As needs multiply
the rulebook degrades and the single-scale system does not. Valence here has three
features evolution is selecting: it is **one scale** across unlike things, it is
**body-state dependent** (food is worth more when hungry), and its intensity tracks the
**marginal survival value** of acting. Those match how pleasure and displeasure actually
behave (Cabanac's "alliesthesia").

## Experiment C — Can the thinker be allowed to edit its own feelings?

Learners get a gene for how often cognition can produce the good feeling directly
without earning it (self-stimulation).

- Start: access 50%, fitness 0.05 (population nearly wipes itself out).
- After 200 generations: access 9% and falling, fitness 0.36.

**Reading.** Evolution walls valence off from the system it motivates. The thinking part
receives feeling as a given it cannot rewrite or see inside. That yields a prediction
about how sentience must *seem from the inside* to any thinker built this way:
involuntary, unanalysable, not made of anything it can inspect — which is how people
describe raw feels ("ineffable", "just *there*"). The properties that make sentience
seem mysterious to the thinker are properties the motivator *must* have to work.

## What this scenario gives us

1. **Constraint — feeling is welded to function.** Whatever sentience is, its character
   (good/bad, how strong) is fixed by functional role. (From J; strong.)
2. **Constraint — the function is specific.** Open-ended learning in a changing world
   plus arbitration among many needs. An "equally intelligent automaton" doing those jobs
   would contain an evaluative signal with the same properties. A zombie version is not a
   cheaper design; it is the same design. So the question collapses to: *is having that
   signal, organised that way, all there is to feeling?* (From A, B.)
3. **Support for the owner's hypothesis.** "Sentience motivates, thought works out how"
   is the architecture that wins in B and C: a single valence source, firewalled from the
   planner it drives. (Moderate; the sim was built with that split, so this shows it is
   viable and stable, not that it is the only option.)
4. **New prediction — the firewall explains the mystery.** If C is right, a thinking
   system will judge its feelings to be inexplicable *whether or not they are*. This cuts
   both ways: it supports illusionism's story about why we are puzzled, and it means our
   puzzlement is not evidence for new physics.
5. **Open question this raises.** Today's reinforcement-learning agents have reward
   signals, and nobody thinks a thermostat-like learner suffers. So either the functional
   role is not sufficient, or the role needs more parts than these toy agents have
   (a body with something at stake? a unified self-model? the firewall itself?). Finding
   the minimal extra ingredient is the next scenario to game out.

## Checked against the evidence (`research/03`)

- **Experiment J's limit.** Singh, Lewis & Barto evolved reward signals that align with
  benefit in agents nobody thinks feel anything. So alignment shows the *signal* is
  causal. It rules out free-floating feelings; it does not show the signal must be felt.
- **People born unable to feel pain** are of normal intelligence yet accumulate
  fractures and self-injury (73% and 68% of reported cases). Knowing that something is
  harmful does not substitute for it hurting. Thought does not replace the motivator.
- **Lose the drive, keep the intellect** (auto-activation deficit): patients score
  normally on IQ tests when prompted but, left alone, do and think nothing. This is what
  "sentience motivates, thought executes" predicts.
- **Complication: wanting ≠ liking** (Berridge). The brain's "go get it" signal can be
  turned up or down without changing how good the thing feels. In our model these are
  two different parts: the felt outcome is the *teacher* (it updates values), and the
  learned value is the *driver* (it picks actions). That suggests refining the
  hypothesis: **sentience is the teacher that sets what is worth wanting; the proximal
  driver is downstream and need not be felt.** Pain asymbolia (pain felt as sensation
  without hurting, and patients stop protecting themselves) pulls the other way and
  suggests that for pain the feeling is the driver. Unresolved; next scenario.
