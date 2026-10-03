# Round 6 red team — Scenario 14 (lottery test)

Re-ran `sims/lottery.py` on a copy (output identical to `sims/out/lottery.json`); recomputed
from raw CSVs with an independent parser. Draw-method and popularity statements are from
memory (no web access).

## Findings

| # | Claim | Verdict | Why (my numbers) | Severity | Fix |
|---|---|---|---|---|---|
| 1 | Counts, shares, bonus balls excluded | HOLDS | All 17 game-periods reproduce to 4 d.p. Every bonus/special ball is excluded (Lotto Texas 5/44-era 6th column and Two Step 5th column confirmed as bonus: they sometimes repeat a main number). No main number repeats within a draw. | – | – |
| 2 | N periods correct | HOLDS | First number >52 in Mega Millions 2005-06-24, >56 2013-10-22, last >70 2017-10-20; Powerball >59 from 2015-10-10; Texas change dates 2000-07-19, 2003-05-07, 2006-04-26, 2002-07-29, 2018-09-24. No draw has a number above its N. No duplicate dates, no gaps >7 days in any file. | – | – |
| 3 | "Normal approximation … conservative" | HOLDS, but understates z | Hypergeometric variance is smaller by (N−k)/(N−1). Correct z: NY +2.06 (not 1.97), Texas +0.32, combined +1.87 (not 1.79). Exact convolution test, one-sided: NY p=0.020, Texas 0.377, combined 0.031. 20,000-draw simulation: NY one-sided 0.021, two-sided 0.040. | Low | Report hypergeometric z; say one-sided, since the prediction was directional. |
| 4 | "Most of the primary excess comes from two Mega Millions periods" | BROKEN | Surplus balls (O−E) in NY = +301.7. Mega Millions 2013–17 and 2017–now give +119 (40%). Take 5 alone gives +101 (34%), Cash4Life +54, NY Lotto +41, Powerball 2015–now −41. | Medium | Delete; no single game carries it. |
| 5 | "The borderline New York result did not replicate" | WEAKENED | Texas +0.04% ± 0.14% is compatible with zero *and* with +0.26% (NY−Texas difference z=1.15). Texas power to detect the NY effect was only ~41–59% (depending on whether tilt is additive or in odds). It is an inconclusive replication, not a failed one. | Medium | "Texas alone shows no effect but was too small to confirm or exclude the NY one." |
| 6 | Pooled estimator sensible | WEAKENED | The pooled z equals the score test for a common odds tilt, which is fine. The pooled *excess in share* is not: 61% of balls are from games with N≤39, where ≤31 covers 79–89% of the drum and the cut-off carries almost no popularity contrast. | Medium | Quote the tilt as an odds ratio: combined +1.05% ± 0.56% (95%: −0.05% to +2.15%). |
| 7 | "Rule out a tilt larger than about 0.4%" | WEAKENED | True only for the ball-weighted mix (95% upper +0.36%). In games with N≥44 the upper bound is +0.82%. As relative odds, upper bound is ~2.2%. | Medium | State the bound in odds, or per game class. |
| 8 | Homogeneity across games (implicit) | WEAKENED | ≤31: Q=26.6, df 16, p=0.046 overall; within Texas Q=16.4, df 7, p=0.021. Post hoc split: N≥44 games +0.47% ± 0.18%, z=+2.71 (NY +1.81, Texas +2.23); N≤39 games −0.01%, z=−0.14. **This split is mine and post hoc**, so not evidence, but a proponent will find it. | High | Disclose; pre-register the N≥44 subset for a third, fresh sample. |
| 9 | Secondary (≤12) flat "where the idea predicts a larger effect" | HOLDS | ≤12: combined +0.02%, z=+0.16; flat in every subset incl. N≥44 (+0.37). All of the ≤31 excess sits in 13–31 (N≥44: z=+2.56), 1–9 is nil. Number 7 (the most-chosen number in every study I know): z=+0.67. This is the wrong shape for a popularity-driven tilt. | – | Make this the lead argument against. |
| 10 | Multiple comparisons | HOLDS (minor) | One primary and one secondary were declared, so no correction is owed on the primary. Largest of 17 period z's is 2.47, Šidák p=0.11. | Low | – |
| 11 | Premise: players favour ≤31, "especially ≤12" | WEAKENED | From memory: conscious-selection studies (Clotfelter & Cook; Farrell, Hartley, Lanot & Walker on UK Lotto; Henze on German Lotto) agree that ≤31 is over-chosen and 7 is the favourite; "especially ≤12" is roughly right but 1 and 2 are not favourites. Not addressed: roughly 70–80% of US jackpot tickets are machine Quick Picks (uniform), so the imbalance in "wanting" is a few percent per number, not "far more often". | Medium | Tone down Part 1; note the dilution. |
| 12 | Draws are physical ball machines | UNCHECKED | From memory: Powerball and Mega Millions — mechanical throughout (high confidence). Texas Lotto Texas, Cash Five, Two Step — mechanical in Austin (fairly high). NY Lotto, Take 5, Cash4Life (drawn in New Jersey) — mechanical (moderate). I know of no computer-drawn period; not verified. | Medium | Verify from operator draw procedures before any positive claim. |
| 13 | No mundane explanation considered | WEAKENED | Balls are loaded in numerical order; incomplete mixing could give a number-correlated bias of unknown sign. Published audits (e.g. UK Lotto) found none but could not see 0.2–0.5%. A positive result would not separate chooser from machine. | Medium | State it; a chooser-specific signature (item 14) is needed. |
| 14 | Chooser-specific prediction | UNCHECKED | Effect should grow with sales/jackpot. Files have no jackpot or sales column. Weak proxy (higher-sales draw day): Mega Millions Friday z=+1.29 vs Tuesday +2.43; Powerball Saturday +0.16 vs Wednesday −0.54. No dose-response. | Medium | Obtain per-draw sales (Texas publishes them) and pre-register a slope test. |
| 15 | Replication scope | WEAKENED | Part 1b promised "any other national or state draw history we can download"; only Texas was used. Dropping change years is harmless (exact-date version, 77,464 balls: +0.04%, z=+0.31). | Low | Say why only Texas. |

## Recomputed table (hypergeometric SE; one-sided exact p)

| Sample | Balls | ≤31 excess | z | p | ≤12 excess | z |
|---|---|---|---|---|---|---|
| New York | 116,394 | +0.259% ± 0.126% | +2.06 | 0.020 | 0.000% ± 0.121% | 0.00 |
| Texas | 72,851 | +0.044% ± 0.139% | +0.32 | 0.377 | +0.041% ± 0.160% | +0.25 |
| Combined | 189,245 | +0.176% ± 0.094% | +1.87 | 0.031 | +0.015% ± 0.097% | +0.16 |

Combined 95% interval for ≤31: −0.01% to +0.36%. As a common odds tilt: +1.05% ± 0.56%.

## Additional test (reviewer's; NOT pre-registered by the authors)

Cut-off-free: mean drawn number per draw against (N+1)/2, exact without-replacement
variance, pooled. A popularity tilt predicts a lower mean. Result: NY z=−1.26, Texas
z=−0.70, combined z=−1.42 (one-sided p=0.08). Same direction, weaker than the ≤31 test,
i.e. the ≤31 result depends on where the cut is placed.

Best next test, to be written down before any new download: ≤31 share in games with N≥44
only, on operators not yet used, with per-draw sales as a dose variable.

## Suggested Reading paragraph

> Combined, drawn numbers ≤31 exceed chance by +0.18% ± 0.09% (z=+1.87, one-sided p=0.03):
> suggestive, not established; Texas alone shows nothing but was too small to confirm or
> exclude the New York figure. Against a wanting-driven tilt, the excess is absent for 1–12
> and for 7, where popularity is highest, and does not rise on higher-sales days; it is
> also uneven across games (p≈0.05), concentrated in large-drum jackpot games in a split we
> did not pre-specify. The data neither show a tilt nor exclude one below about 2% in odds;
> a third, pre-registered sample of large-drum games with sales data is needed.
