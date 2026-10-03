# Scenario 6 — Five new conjectures, each given a chance to fail

Evidence: `research/08-bundle-and-unity.md`, `research/09-threshold-interrupt-bridge.md`.
Code: `sims/interrupt.py`. Status: **reviewed; see the red-team outcome at the end before relying on anything here.**

## 6.1 "Sentience is not one thing"

*Conjecture:* pain, hunger, thirst, itch, breathlessness and pleasure are unrelated
mechanisms. If so, "where does sentience come from" is several questions.

*Test:* do they fail separately or together?

- **Separately at the input end.** People born without the drive to breathe feel no
  discomfort holding their breath or breathing CO₂, yet feel breathless on hard exercise
  (Shea 1993). People with no amygdala feel no ordinary fear, yet panic on CO₂
  (Feinstein 2013). Single feelings can be deleted cleanly.
- **Together at the output end.** A small region deep in the brain (the ventral
  pallidum) is needed for "liking" across different pleasures, the same opioid hotspots
  serve them, and a frontal region carries one common value scale for unlike goods.
- **Surprise.** A patient whose insula and nearby cortex, the areas usually credited
  with bodily feeling, were destroyed on both sides still felt pain, itch, hunger,
  thirst and pleasure (Damasio 2013). The core of feeling is not where the textbooks
  put it, which favours deeper, older structures.
- **Not found:** the order in which feelings vanish under deepening anaesthesia. Nobody
  appears to have measured it.

*Verdict:* **weakened.** The evidence fits "many inputs, one valuer" better than
"many unrelated feelings". The project's question survives.

## 6.2 "One feeler per bottleneck"

*Conjecture:* a subject of feeling exists wherever all of a creature's competing wants
are finally settled in one place.

- Split-brain patient P.S.: the two hemispheres named different career wishes and gave
  different like/dislike ratings on one occasion, consistent ones a month later
  (LeDoux 1977). Modern reviews: perception splits, behaviour stays largely unified,
  and whether there are one or two subjects is "insufficient evidence".
- Octopus: learned avoidance of a place where it was hurt, and wound-tending, are
  whole-animal; severed arms only show reflexes (Crook 2021).

*Verdict:* **survives, untested.** Nothing contradicts it; nothing has tried to.
*Settling observation:* after split-brain surgery, give each hemisphere a different
stake in the same choice and see whether two conflicting sets of felt preference appear
and persist.

## 6.3 "There is one valuing system; 'felt' just means strong enough to notice"

This would dissolve round 2's crux (can the body value something without it being felt?)
by saying: no, weak valuation is weakly felt and goes unreported.

- The best-controlled studies of "unconscious" perception find the effects vanish when
  awareness is measured properly, and blindsight has been re-read as degraded conscious
  vision with a cautious reporting habit (Phillips 2021; Peters & Lau 2015).
- No study has shown feeling steering behaviour when awareness, measured without bias,
  is truly zero.

*Verdict:* **survives by default.** It also risks being unfalsifiable, since any
unfelt effect can be called "below threshold".
*Settling experiment (not yet run):* two intervals, one with a tiny dose of a reward or
a hidden emotional picture, one with placebo. If people's behaviour distinguishes the
intervals while their bets on "which felt different" stay at chance, the conjecture is
refuted.

## 6.4 "Feeling is an interrupt"

*Conjecture:* a planner that does one thing at a time needs a way for urgent matters to
break in. How strongly something is felt tracks how urgently to switch, not how much is
at stake.

*Our model.* A planner is partway through a chunk of work that pays only on completion.
Something turns up with a stake, a deadline, and a handling time. We compared break-in
signals that can see different things, each tuned as well as possible. Score = share of
the best achievable result:

| Chunk length | Stake | Sees stake only | Sees deadline only | Sees stake and deadline | Also sees own progress |
|---|---|---|---|---|---|
| 2 | low | 0.93 | 0.93 | 0.99 | 1.00 |
| 5 | medium | 0.87 | 0.89 | 0.95 | 1.00 |
| 10 | medium | 0.79 | 0.75 | 0.86 | 1.00 |
| 20 | medium | 0.65 | 0.58 | 0.67 | 1.00 |
| 20 | high | 0.76 | 0.54 | 0.76 | 1.00 |

*Reading.* A good break-in signal cannot be a property of the stimulus alone. It must be
discounted by what the planner would lose by dropping its current work. The longer the
commitments, the more this matters (up to a third of the achievable value).
**Prediction:** the same injury should hurt less the deeper one is in a committed task,
and should hurt less once the protective action is already under way.

*Evidence.* For: pain ratings fall under demanding tasks, trial by trial at fixed heat
(Buhle & Wager 2010; Bantick 2002). Self-controlled pain hurts less than identical
externally controlled pain (Wiech 2006). Thirst switches off within seconds of drinking,
long before the blood changes. Against: **chronic pain does not yield to distraction**
(meta-analysis, effect ≈ 0.10, not significant): an interrupt that keeps firing with
nothing to be done is what the idea says should not happen. And the supporting findings
are equally predicted by "pain needs attention to be felt at all".

*Verdict:* **weakened.** Good for acute pain and bodily urges, poor for chronic pain,
vague for pleasure.
*Settling experiment:* same injury signal, same threat, same task load; vary only
whether the protective response is already irrevocably done. Interrupt predicts less
pain when done; the attention account predicts no difference.

## 6.5 "Feeling bridges time"

*Conjecture:* a sustained felt state keeps an event "live" until its consequences
arrive, so the creature can learn what caused what.

*Evidence.* Learning across a gap is done by insect brains, by a rat brainstem with the
rest removed, and by an anaesthetised rat across two hours (taste aversion). The one
human study tying gap-learning to awareness (Clark & Squire 1998) has not replicated
cleanly.

*Verdict:* **refuted** as a requirement. Brains bridge time without feeling.

## Summary

| Conjecture | Verdict |
|---|---|
| Not one thing | weakened: one valuer, many inputs |
| One feeler per bottleneck | survives, untested |
| Felt = above a noticing threshold | survives by default; test specified |
| Interrupt | weakened: fits acute pain, fails chronic pain |
| Bridges time | refuted |

---

> **Red-team outcome (round 3).** Verdicts above were too strong. Corrected: 6.1 undecided, test not run · 6.2 not yet testable · 6.3 unfalsifiable as stated · 6.4 untested, simulation withdrawn · 6.5 not needed for short gaps, long gaps untested. Details: `reviews/round3-response.md`.
