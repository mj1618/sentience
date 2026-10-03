# Scenario 3 — Engine, teacher, or interface?

Code: `sims/interface.py`, `sims/imagination.py`. Evidence: `research/04-hedonic-interface.md`.

## Conjecture

Round 1 left a tension: the owner's hypothesis says feeling is the motivator, but the
brain's "go get it" signal (wanting) and its pleasure signal (liking) can be pulled
apart. And a plain reward signal exists in thermostats and learning algorithms that
presumably feel nothing. Conjecture:

> **Feeling is not the body's valuation as such. It is that valuation at the point
> where it is handed to the flexible, planning part of the mind.** Automatic systems
> (reflexes, habits, cue-triggered urges) run on valuation that need not be felt.

Borrowed in part from Dickinson & Balleine's "hedonic interface" idea.

## Test 1 — Which wiring reproduces the laboratory record?

Four wirings of the same body valuation:

| Wiring | Idea |
|---|---|
| direct | One system. Action follows how the outcome would feel right now. (Feeling = engine.) |
| cached | One system. Action follows stored values of actions, learned from past feelings. (Feeling = teacher.) |
| interface | Two systems. An automatic one re-values cues live. A planner stores outcome values that update only when the outcome is experienced. |
| readout | Two systems, but the planner can look up the body's current valuation of anything it thinks of. |

Seven findings, and whether each wiring reproduces them:

| Finding | direct | cached | interface | readout |
|---|---|---|---|---|
| 1a. A rat trained hungry, then fed, keeps pressing the lever at the same rate (Balleine 1992, verified) | ✗ | ✓ | ✓ | ✗ |
| 1b. …until it tastes the food once while full; then pressing drops | ✓ | ✗ | ✓ | ✓ |
| 2. A cue for disgustingly salty water becomes attractive at once when the rat is salt-starved, before it tastes anything (Robinson & Berridge 2013, verified) | ✓ | ✗ | ✓ | ✓ |
| 3. Dopamine loss: no seeking, pleasure reactions intact | ✓ | ✓ | ✓ | ✓ |
| 4. Sensitisation: wanting up, liking unchanged | ✓ | ✓ | ✓ | ✓ |
| 5. A hidden mood nudge changes how much people drink, not how they say they feel (Winkielman 2005, verified, unreplicated) | ✗ | ✗ | ✓ | ✓ |
| 6. Lost self-activation: no spontaneous action, normal when prompted | ✓ | ✓ | ✓ | ✓ |
| **Score** | 5/7 | 4/7 | **7/7** | 6/7 |

**Caveat.** The interface wiring was written with these findings in mind, so 7/7 is not
a prediction. The informative part is the failures: *no single-system wiring fits*, and
"the planner can read the body directly" is contradicted by finding 1a. A rat's planner
does not know what its body currently wants until it tastes.

## Test 2 — Why isn't the planner simply given direct access?

Direct readout is strictly better for choosing: in our comparison it scores 1.00 against
0.82 for the interface wiring and 0.72–0.82 for the single cached system (the interface
advantage over cached grows with the number of routes to each outcome). So why did
evolution not build it? Round 1's firewall result suggests an answer: a planner that can
call up real feelings at will can reward itself for free.

`sims/imagination.py` evolves how vivid a *previewed* feeling is (0 = none, 1 = as
strong as the real thing):

| Effort of acting (vs typical payoff ≈ 1.3) | Best preview vividness | Fitness at best | at full vividness | with no preview |
|---|---|---|---|---|
| 0.1 | 0.7 | 0.91 | 0.80 | −0.01 |
| 0.3 | 0.6 | 0.61 | 0.47 | −0.02 |
| 0.6 | 0.8 (flat) | 0.16 | 0.15 | −0.03 |

**Reading.** No preview is useless; a full-strength preview loses 12–24% to daydreaming.
The optimum is a pale copy. **Prediction: imagined feelings should be systematically
fainter than experienced ones, by design and not by limitation**, and daydreaming should
take over when real rewards become costly relative to their payoff. (Not yet checked
against the literature.)

Humans do have some readout: told that an outcome is now worthless, people stop working
for it immediately (de Wit 2018, Gillan 2011). But those were symbolic points; whether
being *told* your body no longer wants something works the same way is untested.

## Where the conjecture is weak

1. **"Experienced" has only been shown to mean "contacted".** Nothing in the rat work
   shows the taste must be *felt*. Brain-stem-only animals and anencephalic infants make
   pleasure and disgust faces. Robinson & Berridge's rats even showed "liking" reactions
   to the cue itself before retasting.
2. **Unfelt value can drive effortful action.** Lamb 1991: people pressed a lever 3,000
   times per injection for a morphine dose they could not tell from placebo (n = 5,
   unreplicated, never tested for goal-directedness). If that was planned action, the
   conjecture is wrong.
3. **Risk of circularity.** "Felt" is measured by report; report is produced by the
   planner. So "feeling = what reaches the planner" could be true by definition of our
   measurement and tell us nothing about whether the automatic system also feels.
4. **The comparative test is nearly empty.** Goal-directed devaluation has been shown
   only in rats and humans.

## What this scenario gives us

- **Solid:** valuation runs through at least two separable systems, and the planning
  one is blind to the body's needs until an outcome is experienced. (Published.)
- **Conjecture, moderately supported:** the felt/unfelt line falls at that hand-over.
- **The crux, now named:** *is valuation that never reaches the planner felt?* If yes,
  feeling is ancient and widespread (worms). If no, feeling needs a planner and is much
  rarer. Everything about which animals and machines can feel turns on this.
- **Decisive experiments that have not been done:** (i) a devaluation test with a
  reward dose too small to feel; (ii) devaluation tests in bees, crabs, octopus, fish.
- **Refined hypothesis:** thought does not just serve feeling. Feeling is how the
  body's needs become visible to thought at all, and thought can ask for a pale preview.
