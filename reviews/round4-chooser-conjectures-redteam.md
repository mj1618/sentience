# Round 4 red team — C19 (precognition bound) and scenario 9

2026-10-03. Tags: [V-full] full text read this session · [V-abs] abstract only · [R] recalled.
Full text was read through a fetch-and-summarise tool, so quoted wording is second-hand;
numbers were cross-checked against the abstract where possible. Pooled figures are mine,
from the paper's rounded percentages (binomial SE = 0.5/√N).

Sources:
Walleczek et al. 2025, PLoS One — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335330 (PMC12588471) [V-full]
Kekecs et al. 2023, R Soc Open Sci — https://pmc.ncbi.nlm.nih.gov/articles/PMC9890107 [V-full]
Hughes et al. thirst review — https://pmc.ncbi.nlm.nih.gov/articles/PMC5763530/ [V-full]
Habermann & Büchel 2025, Nat Commun — https://pmc.ncbi.nlm.nih.gov/articles/PMC12627469/ [V-full]

## What Walleczek 2025 actually did

- Task: guess which of two on-screen curtains hides a picture. A hit shows an erotic
  image (NAPS set); a miss shows grey. 18 erotic + 18 non-erotic trials per session;
  only erotic trials are "critical".
- Online panel (Bilendi), mean age 49.2, 40% female, paid ~0.1 EUR/min. No tailoring of
  images to sex or orientation was found in the text, and no rating of whether the
  images were liked.
- Target side drawn **after** the response by a **pseudo-random** generator (Alea).
  Seeding and timing-dependence not described. Kekecs: drawn after the guess; generator
  type not found.
- Four participant arms, not three: Study 1 pure 49.48% ± 0.26 (N = 37,836); Study 1
  mixed 50.10% ± 0.26 (N = 37,836); Study 2 49.65% ± 0.14 (N = 127,000, preregistered
  two-sided, p = 0.013); Study 3 50.07% ± 0.11 (N = 217,800). Sum = 420,472.
- The authors report no pooled estimate. Mine: fixed-effect 49.89%, 95% CI
  [49.74, 50.04]; heterogeneity Q = 8.96, df 3, p = 0.030; random-effects 49.84%
  [49.55, 50.14]; with a small-sample (Knapp–Hartung) interval [49.37, 50.31].
- Authors on Study 2: source "remains to be identified"; false positive "appears more
  plausible". Kekecs: 49.89%, 99.75% CI [49.11, 50.67], 37,836 trials, lab-based.

## Findings

| # | Claim | Verdict | Why | Severity | Fix |
|---|---|---|---|---|---|
| A1 | "26,483 participants, 420,472 trials" | HOLDS | Matches abstract and the four-arm sum. [V-full] | — | Say "four arms in three studies". |
| A2 | "No effect" | WEAKENED | True for the predicted direction (>50%). But the arms are heterogeneous (p = 0.03) and one preregistered confirmatory test came out significant below chance. "No effect in the predicted direction; one unexplained below-chance arm, not replicated" is what the paper says. [V-full] | Medium | Reword. |
| A3 | Study 2 "judged a false positive" | WEAKENED | Authors say "appears more plausible" and that the source "remains to be identified". The repo upgraded a hedge to a judgement. [V-abs, verbatim] | Low | Quote the hedge. |
| A4 | "Bounds effect on choices to about ±0.2%" | WEAKENED | No derivation given. Upward shift: < +0.04% (fixed-effect), < +0.14% (random-effects), < +0.31% (Knapp–Hartung). Downward: −0.26% to −0.63% is not excluded. So "±0.2%" is too loose upward under the model that ignores heterogeneity, and too tight on both sides under the model that respects it. Symmetric "±" is wrong either way. | Medium | State one-sided bound and which model. |
| A5 | This "in effect" runs the randomised read-out test for a **future-aimed** chooser | WEAKENED | Target came from a pseudo-random generator: once seeded, the "future" draw is a present fact in the computer. It is a hidden-fact test. A chooser steering genuinely undetermined future events (quantum-random target) is not tested by this paper. Bem's original and other replications using hardware generators would be needed; not cited, not checked. [V-full] | High | Split C19: hidden-fact bounded; future-quantum not addressed by this source. |
| A6 | The data test a chooser that tilts brain events **toward what will feel good** | **BROKEN** | The stake is a brief untailored erotic picture versus a grey screen, shown to paid panel members averaging 49 years old, with no measure that it was pleasant. For anyone who finds it neutral, the chooser predicts 50%. For anyone who finds it unwelcome, it predicts below 50%. A mixed population cancels: the mean signed shift is bounded, the size of the effect per person is not. Study 2's below-chance result is in the direction an aversive-stimulus reading predicts, which makes "null" the wrong word for this hypothesis. LEDGER C16 already concedes the same gap for device studies ("mostly tested without real pleasure/pain at stake"); C19 forgot it. | **High** | C19 status → "bounded only for trivial stakes of unmeasured sign". |
| A7 | Mapping to per-event tilt: z = 2√2·ε·√N, P = Φ(z), giving 2×10⁻⁵ … 6×10⁻¹¹ | WEAKENED | Arithmetic reproduces (0.2% → 1.8×10⁻⁵ at N = 10⁴, 5.6×10⁻¹¹ at 10¹⁵). The model does not hold. It assumes (a) the left/right choice sits exactly on a knife-edge decided only by the N quantum events; any ordinary determinant (side habit, alternation, previous trial) attenuates the shift by roughly √(quantum share of decision variance): a 1% share loosens the bound 10×, 0.01% loosens it 100×; (b) the N events are independent and equally weighted, which the round 3 review already rejected for spikes; (c) the chooser knows which events push which key (C17's own caveat); (d) N is known. A figure spanning six orders of magnitude on a free parameter is a model output, not a bound. | High | Report the behavioural bound only; give ε as "under model M, with assumptions listed". |
| A8 | "Closed across essentially the whole window" / LEDGER "is closed" | **BROKEN** | Follows from A5–A7. Also, even on the repo's own numbers, at N = 10⁴ the window 10⁻⁸–2×10⁻⁵ (C17) stays open. Escaping variants: stakes must be real pain or pleasure; chooser acts only on outcomes the brain can causally reach (a remote software draw is not one); chooser aims at present felt valence (this is C20, declared unscorable); chooser aims at genuinely undetermined futures. | **High** | Replace "closed" with the bound in the last section. |
| A9 | Selective citation | UNCHECKED | Positive Bem-style meta-analyses exist [R]; the repo cites only the null side. I could not fetch them. | Low | Note the literature is contested and why the preregistered studies are preferred. |
| B1 | Scenario 9 verdicts no stronger than brief | HOLDS (verdict words) / WEAKENED (evidence cells) | The four verdict labels match. The evidence cells drop the brief's caveats: see B2–B5. | Medium | Carry tags and caveats into the table. |
| B2 | "Thirst rises in step with blood concentration (12 trials, 167 people, r = 0.91)" | WEAKENED | r = 0.91 is the mean of 120 individual regressions, not 167 people. Eleven of twelve protocols are fixed-rate 2 h infusions (e.g. 5% saline at 0.05–0.1 ml/kg/min), about 20 mOsm/kg total; no trial held a plateau. Level, elapsed time, volume infused and expectancy are collinear; a monotonic ramp of a few points gives a high r almost regardless of mechanism. The review itself calls the trials "limited in their scope" and artificial. [V-full] | Medium | Report as "consistent with level under a constant-rate ramp". |
| B3 | Infusion data separate level from rate | HOLDS, narrowly | With the rate constant, a pure-derivative signal predicts flat thirst; it climbed, and only above a threshold (285 mOsm/kg). That is real evidence against a *pure instantaneous derivative*. It does not separate level from time-on-infusion, and "rate roughly constant" is the brief's inference, unchecked against plasma curves. The scenario omits the same review's finding that drinking abolishes thirst with osmolality unchanged, and the free-living r² = 0.09: level is not sufficient either. [V-full] | Medium | Add both omitted results. |
| B4 | "Rate, not level: refuted as the whole story" | WEAKENED | Rests on one inference from ramp data (B3) plus two abstracts. Constant 46.5 °C heat is not a constant need: tissue heating and summation continue. And the brief's own "deciding experiment" (hold a plateau, see if discomfort decays) admits the decisive test has not been run. "Refuted" and "the deciding experiment is still to do" cannot both stand. | Medium | "Pure-derivative form disfavoured; plateau test not done." |
| B5 | "Pain you can control was rated higher" (Habermann & Büchel) | **BROKEN** as evidence on the conjecture | (a) "Control" meant choosing the upcoming intensity, not having an escape or coping response; it does not manipulate "ready response" at all. (b) Half the result is omitted: controllable low-intensity pain was rated far *lower* (9.4 vs 18.5); the high-intensity difference is 3.1 points on SDs of 15–18 and is not individually tested (authors report only the interaction, β = 0.29, interval [0.23, 0.35]). (c) Authors' reading: ratings "biased towards the expected intensities", i.e. sharper expectation, not more pain. (d) Intensity was rated, not unpleasantness. [V-full] | **High** | Remove from the "against" column; the "weakened" verdict then rests on four divers [V-abs]. |
| B6 | "Feelings switch on and off within seconds of deep stimulation" | WEAKENED | Brief: latency [R] (no abstract) or "not given". Scenario states it flat. | Low | Tag [R]. |

## The bound the data support

**Hypothesis bounded:** something lets a person's left/right key press anticipate a
pseudo-random software draw made after the press, when the only consequence is a brief
erotic picture of unmeasured appeal.

**Bound:** mean upward shift in hit rate below about +0.15% (95%, random-effects;
+0.3% with the conservative interval; +0.04% only if the significant heterogeneity is
ignored). A downward shift of up to roughly 0.3–0.6% is not excluded, and one
preregistered arm found one.

**Not bounded:** a valence-aimed chooser at real stakes; a chooser aimed at genuinely
undetermined future events; any per-event tilt figure, which needs a decision model the
repo has not justified. C19 should read "weakened", not "closed".
