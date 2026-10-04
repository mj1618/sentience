# Rating rubric for sleep mentation reports

Each row is a transcript of what a person said immediately after being woken, describing
what was going through their mind just before waking. Rate ONLY what the report says
about the experience before waking, not the person's state while speaking.

For each report give:

- `content` : 0 = no experience reported (nothing, blank, or could not recall anything);
  1 = some experience reported.
- `emotion` : how much felt emotion the experience contained, as far as the report shows.
  0 = none stated or implied; 1 = mild or implied (e.g. "it was kind of nice", mild worry);
  2 = clear emotion (explicitly afraid, annoyed, happy, embarrassed, sad…);
  3 = intense emotion (terror, rage, elation, grief).
- `valence` : overall felt tone of the experience. −2 = clearly unpleasant; −1 = mildly
  unpleasant; 0 = neutral or mixed or no emotion; +1 = mildly pleasant; +2 = clearly pleasant.
- `bodily` : 1 if the report mentions a bodily feeling as part of the experience (pain,
  falling, pressure, warmth, hunger, movement sensations…), else 0.

Rules: rate from the text only. Hesitations and filler words are not emotion. If
`content` is 0, set the other three to 0. Do not skip rows. Be consistent.
