# Sentience

Where does sentience (raw feeling: pain, pleasure, hunger — that something feels like
anything at all) come from? Working hypothesis from the owner: **consciousness =
sentience + thought**, sentience being the motivator and thought working out how to
satisfy it. If so, the hard question is sentience alone.

## Method

1. **Compile** what is known → `research/` (every claim tagged verified / recalled).
2. **Conjecture and test**: propose an answer, then stress-test it → `scenarios/` (argument + simulation or calculation) to find
   constraints that make theories more or less likely.
3. **Red-team**: a fresh reviewer tries to break each conclusion → `reviews/`. Nothing is
   treated as reliable until it has survived this.
4. **Record** what moved → `LEDGER.md` (constraints, credences, open questions).
5. **Report** in plain language → `updates/` (HTML pages, no background assumed).

## Layout

| Path | What |
|---|---|
| `LEDGER.md` | Running list of constraints, theory scores, next scenarios |
| `research/` | Literature briefs with sources |
| `scenarios/` | One file per stress test |
| `sims/` | Code; results in `sims/out/` |
| `reviews/` | Red-team reports, independent adjudications, and our responses |
| `experiments/` | Sketches of real-world experiments that would move the question |
| `updates/` | Plain-language progress pages (source); `docs/` is the built site |

Current method (from round 5): write each rival account's predictions and commit them; a separate agent gathers evidence without scoring; an independent adjudicator scores; an auditor checks each update page against the reviews before it is published.

## Standing caveats

- No simulation in this repo has survived review as evidence. They are kept as worked
  attempts and are useful for finding holes in ideas, not for supporting them.
- Summaries have repeatedly been stronger than the reviews behind them. When a summary
  and a file in `reviews/` disagree, the review is right.
