# Draft note to the DREAM database maintainers (not sent)

Subject: "Multiple awakenings" (De Gennaro) recordings appear to continue past the awakening

While analysing the DREAM dataset "Multiple awakenings" (Set ID 9;
https://doi.org/10.6084/m9.figshare.22086266) we found that most recordings do not end
at the awakening. In 422 of 455 files the chin EMG (EMG1 − EMG2, 20–100 Hz) rises
several-fold in the last 40 s; the rise begins a median of 16–18 s before the end of the
file, and 450 of 455 files end on a 20-second boundary. Posterior EEG in that stretch is
dominated by movement artefact. Other datasets we checked (Noreika DATA1, Aamodt evening
and morning, Tononi serial awakenings, REM_Turku) show no such rise before the final
second or two.

Consequence: analyses that take "the last N seconds before awakening" from these files
will mostly sample waking. In our pipeline 34% of the files failed a 500-microvolt
amplitude check for this reason.

Suggestion: add a note to the dataset description, or an annotation of the awakening
time per file. A simple EMG-onset rule recovers it for most files.

Also noticed: the O1 channel is labelled "01" (zero-one) in this dataset; and one
Ratings row in REM_Turku ("case123_s27") probably refers to "case132_s27".

Details and code: reviews/round13-study1-redteam.md and reviews/round13-study4-redteam.md
in https://github.com/mj1618/sentience.
