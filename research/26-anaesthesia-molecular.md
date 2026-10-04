# 26 — Anaesthesia, molecular level: evidence brief for Scenario 32

Neutral evidence gathering for `scenarios/32-what-switches-it-off.md` (Amendment governs).
Accounts covered: L-classical, L-modern, P, Q, M, S. Predictions covered: 1, 2, 3, 4a, 4b, 7.
No scoring here. Gathered 2026-10-04.

**Access key** used for every source:
- **[FT]** full text read (methods/results extracted by a fetch tool, not by eye)
- **[AB]** abstract only
- **[SN]** search-result snippet or secondary citation only
- **[MEM]** recalled from background knowledge, not retrieved this session — treat as unverified

**Standing caveat.** Almost every in-vivo endpoint below is loss of righting reflex (LORR,
"hypnosis" surrogate) or immobility to a noxious stimulus (MAC, a spinal endpoint). Both are
responsiveness measures. None of the molecular-level sources connects its endpoint to
experience. PubMed Central and several publisher sites blocked automated access; where that
forced reliance on abstracts this is marked.

---

## 1. Prediction 1 — Meyer–Overton correlation and its exceptions

### 1.1 The correlation, and a lipid-free protein that reproduces it
- **Franks & Lieb 1984, Nature** [AB]. Pure soluble firefly luciferase (no lipid) is inhibited
  50% at concentrations "essentially identical" to those anaesthetising animals, over a
  100,000-fold potency range, across inhalational agents, alcohols, ketones, ethers, alkanes.
  Inhibition is competitive with luciferin; the site takes one large or more than one small
  molecule. In vitro enzyme assay; n not in abstract. Widely cited; a 1998 crystal structure
  of luciferase with bound anaesthetic is reported [SN]. Bearing: shows the solubility
  correlation does not by itself discriminate lipid from protein sites (relevant to L, P and
  Q.1 alike, since Q also relies on non-polar pockets).

### 1.2 Non-immobilizers / non-anaesthetics
- **Koblin, Chortkoff, Laster, Eger, Halsey, Ionescu 1994, Anesth Analg** [AB]. Rats; 14
  polyhalogenated/perfluorinated compounds; MAC by tail electrical stimulation, with desflurane
  additivity where needed. 9 of 14 had measurable MAC but MAC x oil/gas partition coefficient
  of 3.7–24.8 atm versus 1.8 atm for conventional agents (i.e. 2–14x less potent than
  predicted). 5 of 14 (including 1,2-dichlorohexafluorocyclobutane, "F6"/"2N") produced no
  anaesthesia, were excitatory/convulsant, and tended to raise desflurane MAC, despite lipid
  solubility and brain penetration sufficient to predict anaesthesia. Group sizes not in
  abstract. Replication: the non-immobilizer class has been used by multiple labs since.
- F6 follow-up [SN]: F6 did not change MAC up to its convulsant ED50, and raised MAC 25% and
  36% at 1.3x and 1.7x that dose; F6 does not potentiate GABA-A receptors but does block
  nicotinic receptors. F6 is reported to impair learning/memory while not immobilising [MEM;
  Kandel et al. 1996 — not retrieved].
- Structural pair [SN]: F3 (1-chloro-1,2,2-trifluorocyclobutane) is a potent anaesthetic; the
  close analogue F6 is not.

### 1.3 Cut-off effect
- n-alkanols in tadpoles (LORR): potency rises with chain length to about decanol; dodecanol
  is no more potent than decanol; cut-off at about C12–C13 [SN, from secondary sources citing
  Alifimoff, Firestone & Miller 1989 and Franks & Lieb]. The cut-off chain length differs
  between organisms and between individual receptors [SN].
- Luciferase shows a matching cut-off although it contains no lipid [MEM; Franks & Lieb 1985].
- Counter-point for L: long-chain alcohols continue to partition into bilayers past the
  cut-off [MEM]; lipid-side explanations offered include limited aqueous solubility and
  changing bilayer perturbation per molecule [MEM]. Not retrieved this session.

### 1.4 Direct test of bilayer perturbation at clinical concentrations
- **Herold, Sanford, Lee, Andersen, Hemmings 2017, PNAS** [AB]. Gramicidin-based fluorescence
  assay of bilayer properties; chemically diverse anaesthetics and related non-anaesthetics.
  "None of the compounds tested altered bilayer properties sufficiently to produce meaningful
  changes in ion channel function at clinically relevant concentrations"; minimal even at
  supra-anaesthetic concentrations; only toxic concentrations of some agents altered the
  bilayer. Authors conclude effects on channels "are not bilayer-mediated". Limitation: the
  assay reports bulk bilayer elasticity/thickness in synthetic vesicles, not raft/domain
  organisation in cell membranes (the L-modern claim). Single lab; earlier work from the same
  group with the same assay is consistent [SN].

---

## 2. Prediction 2 — Stereoselectivity

| Agent | Finding | Ratio | Source / access |
|---|---|---|---|
| Isoflurane, ion channels | Molluscan neurons: (+)-isomer about 2x more effective on anaesthetic-activated K current and on nicotinic current at human ED50; (−) marginally more potent on I_A; **both isomers equally effective at disrupting lipid bilayers** | ~2x | Franks & Lieb 1991 Science [AB] |
| Isoflurane, in vivo (LORR, i.v. dosing) | Rats: S(+) ED50 23.3 ± 0.8 µl/kg vs R(−) 32.7 ± 1.5 µl/kg | ~1.4x (reported elsewhere as S(+) "53% more potent") | Lysko et al. 1994 [SN] |
| Isoflurane, in vivo (MAC, inhaled) | Rats: S 1.44 ± 0.12% vs R 1.69 ± 0.20%; 17% difference, **P = 0.06, not significant** | 1.17x, n.s. | Eger et al. 1997 Anesth Analg [AB]; n not in abstract |
| Etomidate | Mice and tadpoles LORR: R(+) about 10-fold more potent than S(−); GABA-A potentiation shows parallel enantioselectivity | ~10x | Belelli et al. 2003 Neuropharmacology [AB] |
| Ketamine | S(+) about 3x more potent than R(−) at the NMDA PCP site; clinical anaesthetic potency ratio usually given as 2–4x | ~3x | [SN]; clinical ratio [MEM] |
| Neurosteroids | Enantioselectivity of neuroactive steroids at GABA-A correlates with tadpole anaesthetic potency | qualitative here | [SN]; Covey/Evers work [MEM] |
| Secondary alcohols (2-butanol to 2-octanol) | Tadpoles: **no significant potency difference** between enantiomer pairs | 1x | Alifimoff et al. 1987 [SN] |

Notes for the adjudicator: the two in-vivo isoflurane studies disagree in size and
significance and use different endpoints and routes. The large ratios are for intravenous
agents; volatile-agent stereoselectivity in vivo is small (≤ ~1.5x) and not consistently
significant; simple chiral alcohols show none. Whether chiral lipids (cholesterol,
phospholipids) could generate a 10-fold difference was not tested in any source retrieved.

---

## 3. Prediction 7 (P form) — single-residue and single-gene genetics in live animals

### 3.1 GABA-A β3 N265M knock-in
- **Jurd et al. 2003, FASEB J** [AB]. Mice with point mutation N265M in GABA-A β3. Suppression
  of noxious-evoked movement by **etomidate and propofol "completely abolished"**; "only
  slightly decreased" for enflurane and halothane. LORR duration "profound reduction" for the
  i.v. agents (reduced, **not abolished**) and not for volatiles. Group sizes not in abstract.
- **Follow-up, β3(N265M) on congenic backgrounds (PMC1810244; Mol Pharmacol/BMC Pharmacol
  c. 2007)** [FT via Europe PMC]. Loss of hindlimb withdrawal to etomidate/propofol absent on
  129X1/SvJ and C57BL/6J backgrounds (phenotype replicated across three backgrounds, same
  group). Volatile immobilising EC50 shifts in the mutant: enflurane +16%, halothane +21%,
  isoflurane +24%. LORR to i.v. agents shortened but present. β3-independent: anterograde
  amnesia from propofol.
- **β2 N265S knock-in (Reynolds et al. 2003)** [SN within the above]: retains immobilising and
  hypnotic responses to etomidate, loses sedation at low dose.
- Replication status: an independent anaesthesia-lab replication of the β3 knock-in was not
  located this session.

### 3.2 TREK-1 (K2P) knockout — conflicting
- **Heurteaux et al. 2004, EMBO J** [AB; numbers SN]. Trek1−/− mice "resistant to anesthesia
  by volatile anesthetics". Secondary summary (Yost et al. 2008 [FT]): MAC increased 7–48%
  depending on agent. Mice still became anaesthetised. Pentobarbital reported unaffected
  [MEM]. Group sizes not obtained.
- **Spencer, Woods, Worstman, Johnson, Ramirez, Morgan, Sedensky 2023, Anesthesiology 139:63**
  [AB]. Title: "TREK-1 and TREK-2 knockout mice are not resistant to halothane or isoflurane."
  Two independent Trek-1 knockout lines, Trek-2 knockout, double knockout. WT halothane MAC
  1.30% (SD 0.10), isoflurane 1.40% (0.11); Trek-1 knockout e.g. 1.27%; P 0.188–0.482, no
  significant differences. Isoflurane-induced currents in spinal neurons persisted in
  knockouts but became norfluoxetine-insensitive ("other channels may function in this role
  when TREK channels are deleted" — i.e. compensation proposed). **A failed replication of
  Heurteaux 2004.** Group sizes not in abstract.
- KCNK7 knockout: no change in volatile sensitivity (Yost et al. 2008 [FT]).

### 3.3 HCN1
- Global HCN1 knockout: potency of ketamine and propofol for LORR "strongly reduced";
  etomidate (no HCN1 effect in vitro) unaffected (Chen et al. 2009 J Neurosci [SN]).
- **Zhou et al. 2013, Anesthesiology** [AB]: forebrain-restricted HCN1 knockout shifts
  ketamine LORR EC50 up by ~31%. Same lab as the 2009 paper.

### 3.4 NMDA receptor and xenon
- Armstrong et al. 2012 [SN]: GluN1 F758W/F758Y remove xenon's competitive inhibition at the
  glycine site in recombinant receptors without altering glycine binding. In vitro only; no
  knock-in animal anaesthesia data located.
- Xenon also activates TREK-1 at clinical concentrations (Gruss et al. 2004 [SN]); in spinal
  lamina IX neurons xenon reduced AMPA- but not NMDA-mediated excitation [SN].

### 3.5 What remains unexplained (stated in sources)
- No single mutation abolishes immobility or LORR for a volatile agent; best shifts are
  16–24% (β3) and a contested 7–48% (TREK-1). Jurd: volatiles "act via a broader spectrum of
  molecular targets" [AB].
- For xenon, no in-vivo genetic test of any target was found.
- The largest single-gene shifts for volatiles in mammals are for a mitochondrial protein
  (section 6), not an ion channel.

---

## 4. L-modern — membrane-mediated mechanism and prediction 7 (L form)

### 4.1 Pavel, Petersen, Wang, Lerner, Hansen 2020, PNAS 117:13757
[FT via PMC before access was blocked.]
- Cells (super-resolution imaging): chloroform 1 mM and isoflurane 1 mM increased apparent
  diameter/area of GM1 raft clusters (P < 0.0001; raw sizes are in figures, not extracted).
  1 mM is described by the authors as clinically relevant; isoflurane 1 MAC aqueous is about
  0.3 mM [MEM], so 1 mM is roughly 3x MAC. Xenon tested at 4.9 mM (saturated).
- TREK-1 in HEK cells: chloroform gave ~2-fold current increase (n = 11, P < 0.05);
  co-expressing catalytically dead PLD2 (K758R) **abolished** chloroform activation ("no
  detectible chloroform-specific current").
- Purified TREK-1 reconstituted in liposomes (flux assay): unaffected by chloroform or
  isoflurane — offered as evidence against direct binding being sufficient.
- Drosophila: PLD-null flies needed "almost twice the exposure" to chloroform (2.8 mmol/L air
  volume) for sedation, ~600 s vs ~350 s, P < 0.0001. **All flies were eventually
  anaesthetised**; authors: PLD "helps set a threshold, but it is not the only pathway".
  Endpoint is latency at a single concentration, not a concentration–response shift.
- Authors' stated limitations: chloroform concentration is vapour, not tissue; anaesthetic
  application latency exceeded theoretical PLD2 activation speed.

### 4.2 Published criticism and reply
- **van Swinderen & Hines 2020, PNAS letter, "Turning to Drosophila for help in resolving
  general anesthesia"** [FT via Europe PMC]. Points: a single induction experiment, chloroform
  only, no error bars or sample sizes; unnamed wild-type control strain; raft imaging of
  ">16,000 data points extracted from an unstated number of fly brains of unknown genotype
  exposed to an undetermined concentration of chloroform"; no test of non-anaesthetic
  analogues, which might also disrupt rafts; cite syntaxin1A trapping as an alternative
  convergent mechanism.
- **Hansen et al. reply** [SN only; full text blocked]: state that n of fly brains had been
  inadvertently omitted — **two treated and two control brains**; fly work was part of a
  larger study. Further content of the reply not verified.

### 4.3 Evidence bearing against the membrane-first reading
- **Wague et al. 2020, eLife** [AB]: photoaffinity isoflurane analogue (azi-isoflurane) labels
  TREK-1 at G182 and K194 on TM2 (per [SN]); functional relevance supported by mutagenesis and
  chemical modification. This is direct binding to the channel, and mutating the site alters
  modulation — the opposite of the L-modern clause "mutating a channel's binding site does not
  abolish the drug's effect".
- Herold 2017 (section 1.4): no meaningful bulk-bilayer change at clinical concentrations.
- Spencer 2023 (section 3.2): removing TREK-1, the effector in the Pavel pathway, did not
  change MAC or LORR in mice.

### 4.4 Evidence bearing for it
- PLD2 catalytic dependence of TREK-1 activation in cells (4.1); a companion line from the
  same lab on mechanical activation of TREK-1 via PLD2 (Petersen et al., eLife 2023/24 [SN]).
- Franks & Lieb 1991 also shows the other side: bilayers were disrupted equally by both
  isoflurane isomers, so a raft mechanism would predict little stereoselectivity for
  isoflurane — compatible with the small/non-significant in-vivo isoflurane ratio (section 2),
  not with etomidate's 10x.

### 4.5 Lateral-pressure theory (Cantor 1997)
- Theoretical/thermodynamic proposal that anaesthetics shift the bilayer lateral pressure
  profile and thereby channel conformational equilibria; offers accounts of cut-off and
  non-immobilizers [MEM]. No direct experimental test was located this session. The Herold
  2017 gramicidin result is the nearest functional test and was negative at clinical
  concentrations.

### 4.6 Direct tests of prediction 7 (L form), summary
- "Deleting the lipid-sensing enzyme reduces sensitivity": one study, flies, chloroform only,
  latency ~1.7x, reporting criticised in print, **no independent replication found**. No
  PLD2-knockout mouse anaesthesia study found.
- "Mutating the channel site does not abolish the drug's effect on that channel": for TREK-1,
  Wague 2020 reports the contrary; for GABA-A β3 N265M, i.v.-agent effects on the receptor
  and on immobility are lost.

---

## 5. Q — quantum / microtubule

### 5.1 Prediction 4b: nuclear spin (xenon isotopes)
- **Li N, Lu D, Yang L, Tao H, Xu Y, Wang C, Fu L, Liu H, Chummum Y, Zhang S. 2018,
  Anesthesiology 129:271** [AB; full text paywalled, not read].
  - 80 male C57BL/6 mice, 7 weeks, randomised to four groups (so n = 20/group): 132Xe
    (spin 0), 134Xe (spin 0), 131Xe (spin 3/2), 129Xe (spin 1/2).
  - LORR ED50 with 0.50% isoflurane background: 15 ± 4% (132Xe), 16 ± 5% (134Xe),
    22 ± 5% (131Xe), 23 ± 7% (129Xe).
  - "Xenon alone" ED50: 70 ± 4%, 72 ± 5%, 99 ± 5%, 105 ± 7% atm. A value of 105% cannot be
    delivered at normobaric pressure, so these appear to be extrapolated from the isoflurane
    combination rather than measured directly — **inference, not verified**.
  - Polarisability identical for all four (3.60 Å^3 as reported), so polarisability does not
    explain the difference (this also bears on the original scenario's Q.1 wording).
  - Relative size: spin isotopes need ~40–50% more xenon. Group difference of ~7 percentage
    points against SDs of 4–7.
  - **Not verified:** isotopic enrichment/purity, supplier, how chamber xenon concentration
    was measured, whether observers were blinded to isotope, exact P-values. One retrieval
    tool returned the isotope/ED50 pairing in a scrambled order; the pairing above is the one
    consistent with the paper's title and with two other secondary sources.
  - Mass does not track the effect (131 and 129 are lighter than 132 and 134, but 131 vs 132
    differ by 1 amu); the two spin-bearing isotopes with very different spin (1/2 vs 3/2,
    131Xe quadrupolar) gave near-identical ED50s — noted in one theoretical paper as needing
    "less uncertainty" [SN].
- **Replication status: none found.** Searches for replication, failed replication, or other
  species returned only theory papers built on the result: Smith et al. 2021 Sci Rep
  (radical-pair model) [SN]; Zadeh-Haghighi & Simon 2022 J R Soc Interface review [SN]; a
  2023 Frontiers in Physiology perspective on magnetic isotope effects, which reports the
  result with no replication or critique and reports no independently replicated isotope
  effect in biology [FT]; Wang & Ozturk, arXiv 2605.19395, May 2026 (chiral-induced spin
  selectivity model; theoretical; mentions no replication) [AB]. Hameroff's accompanying 2018
  editorial is supportive [SN]. A Duke thesis "Investigating the Fundamental Physics of
  Anesthetic Action" appeared in search results and may contain relevant experiments — **not
  opened**.
- Cited count ~33 (Europe PMC). Eight years, no published in-vivo replication located.

### 5.2 Other spin-bearing isotopes (lithium) and Fisher's Posner proposal
- **Sechzer et al. 1986** [SN]: rats; 6Li-treated dams showed more grooming/nursing/nest
  building, 7Li dams less, than controls. n not obtained. A later review notes interpretation
  "hampered by several methodological deficiencies" [SN].
- **Ettenberg, Ayala, Krug, Collins, Mayes, Fisher 2020, Pharmacol Biochem Behav** [AB + SN]:
  male rats, 16 per isotope group [SN], 2.0 mEq/kg/day lithium in diet for 30 days;
  ketamine-induced hyperlocomotion. "By the fourth trial" 6Li animals showed significantly
  greater and more prolonged reduction than 7Li or natural Li. Effect size not obtained.
  Different behaviour and opposite-sign logic from Sechzer; not a replication of it. Co-author
  is the proposer of the hypothesis.
- Null: a University of Waterloo thesis found no 6Li/7Li difference in GSK-3β activity,
  GSK-3β phosphorylation, or HT22 neuronal cell viability [SN].
- **Deline et al. 2023, Front Physiol** [SN]: isolated mitochondria; 7Li more potent on
  calcium capacity, 6Li more effective at delaying permeability transition; isotope-dependent
  calcium-phosphate colloid size in vitro.
- **Straub, ..., Fisher, Helgeson 2025, PNAS** [AB]: in vitro, 7Li gave more observable
  amorphous calcium phosphate particles than 6Li under identical preparation. From the
  proposer's group; titled "possible quantum effect". Ordinary mass-dependent isotope effects
  are large for 6Li/7Li (17% mass difference), unlike xenon (<1–4%) — a confound the lithium
  work must exclude and the xenon work largely avoids.
- No test of Posner-molecule spin entanglement in vivo was found. None of the lithium work
  concerns anaesthesia.

### 5.3 Prediction 4a: microtubule stabilisers/destabilisers and anaesthetic sensitivity
- **Khan, ..., Wiest 2024, eNeuro 11(8) ENEURO.0291-24.2024** [FT]. (The scenario's
  "Kalra/Wiest" paper; first author as indexed is Khan.)
  - 12 male Long-Evans rats: 8 in the main within-subject group, 4 in a separate
    tolerance-control group. Epothilone B 0.75 mg/kg s.c. (vehicle 50% DMSO/saline), given
    after the LORR measurement on a session. 4% isoflurane in O2; endpoint = latency to LORR.
  - Result: mean latency **+69 s** after epothilone B vs before; 7 of 8 rats increased;
    permutation test **P = 0.0016; Cohen's d = 1.9**.
  - Blinding: the two observers "could not know" whether an injection was drug or vehicle, but
    authors concede blinding was insufficient because all rats received conditions in the same
    order. No randomisation of order; no video scoring.
  - Tolerance to repeated isoflurane is a competing explanation; authors estimate tolerance at
    ~40 s at most and argue it cannot account for 69 s. Males only. Peripheral neuropathy,
    respiratory or pharmacokinetic effects of epothilone B were discussed but not tested.
    Induction-latency at one high concentration is not an EC50/MAC shift.
- **Li N, You Z, ..., Mao J, Martyn JAJ 2025, BMC Anesthesiology, "Microtubule-modulating
  drugs alter sensitivity to isoflurane in mice"** [AB]. Independent group (MGH). Mice;
  prolonged administration of epothilone D (stabiliser), paclitaxel (stabiliser), vinblastine
  (destabiliser); isoflurane LORR concentration–response. Epothilone D EC50 0.75 [95% CI
  0.73–0.77] vs saline 0.97 [0.96–0.98]; vinblastine 0.74 [0.73–0.75] vs saline 0.98
  [0.97–0.99]. That is, **both a stabiliser and a destabiliser made mice MORE sensitive
  (~23–24% lower EC50)** — sensitivity shifted, but the stabiliser effect is in the opposite
  direction to Khan/Wiest. Paclitaxel result, n per group, and blinding not obtained from the
  abstract. Design differs (chronic dosing, EC50 not latency, mice not rats, epothilone D not
  B), so it is not a direct replication attempt.
- **Emerson, ..., Eckenhoff, Dmochowski 2013, JACS** [AB]. Tadpoles. Photoactive
  1-azidoanthracene immobilised tadpoles on UV irradiation and labelled β-tubulin near the
  colchicine site; aminoanthracene-crosslinked tubulin inhibited polymerisation in vitro.
  Pre-incubation with stabilisers epothilone D or discodermolide "significantly increased" the
  1-aminoanthracene concentration needed for immobility; epothilone D also mitigated
  allopregnanolone. Authors' conclusion is limited to anthracene anaesthetics "and may also
  represent functional targets for some neurosteroid" anaesthetics. No claim for volatile
  agents or propofol in the abstract; numbers and n not in abstract. Direction matches Khan.
- **Linganna, Levy, Dmochowski, Eckenhoff, Speck 2015, J Clin Anesth 27:481** [AB].
  Retrospective cohort, women having breast-cancer surgery; neoadjuvant taxane vs no prior
  taxane. Taxane group: larger blood-pressure response to incision (P = 0.03) and more
  morphine (26.3 vs 15.5 mg, P = 0.02); **inhaled anaesthetic concentrations similar
  (P = 0.15)**. n not in abstract. Endpoints are analgesic/haemodynamic, not hypnosis or
  awareness; taxane neuropathy and chemotherapy-related differences between groups are
  uncontrolled confounds. This study is cited both as support for 4a (resistance) and can be
  read as not showing a change in anaesthetic requirement; I found no study of awareness or
  MAC in taxane patients.
- Older genetics: no C. elegans or Drosophila tubulin mutant with altered volatile-anaesthetic
  sensitivity was found in the searches run; forward genetic screens in worms and flies
  returned syntaxin, complex I, and channel genes (sections 6–7). Absence of a hit in my
  searches is not proof none exists — **not exhaustively checked**.
- Classic observation that high halothane concentrations depolymerise microtubules (Allison &
  Nunn 1968) [MEM]; said to require supra-clinical concentrations — not retrieved.

### 5.4 Do anaesthetics bind tubulin at clinical concentrations, and is it specific?
- **Pan, Xi, Tobias, Eckenhoff, Eckenhoff 2007, J Proteome Res** [AB]. Halothane photolabelling
  of human temporal cortex; of >300 membrane and >400 soluble protein spots, **23 membrane and
  34 soluble proteins (57 total)** were labelled, spanning carbohydrate metabolism, protein
  folding, oxidative phosphorylation, nucleoside triphosphatases, dimer/kinase activity.
  Tubulin is among halothane-labelled proteins in this line of work [SN]. So tubulin binds,
  as do dozens of other proteins including mitochondrial ones; binding does not establish
  function. Photolabelling concentration relative to clinical not verified.
- **Craddock et al. 2017, Sci Rep** [SN]. Computational only (docking, quantum chemistry,
  dipole modelling): 8 anaesthetic gases shift a modelled 613 THz tubulin collective
  oscillation downward in proportion to potency; non-anaesthetics shift slightly upward. No
  wet experiment. Craddock 2012 (computational binding-site prediction on tubulin) [MEM].
- Wiest 2026, Med Gas Res — commentary restating the case [title only].
- Decoherence critiques (Tegmark 2000 etc.) do not use anaesthesia data and are omitted per
  the brief.

---

## 6. M — mitochondrial (complex I)

- **Kayser, Morgan, Sedensky 1999, Anesthesiology** [AB]: C. elegans gas-1(fc21) is a missense
  (conserved Arg→Lys) in the 49-kDa subunit of complex I; mutant is hypersensitive to all
  volatile anaesthetics [SN]. EC50 fold-change not retrieved.
- **Falk et al. 2006, Curr Biol** [SN]: across several complex-I-deficient worm strains,
  anaesthetic sensitivity increased as complex-I-dependent oxidation rate decreased
  (dose–response relation across alleles).
- **Quintana et al. 2012, PLoS One** [FT earlier via search extraction]: Ndufs4 knockout mice.
  Isoflurane EC50 **0.44 ± 0.07% vs WT 1.23 ± 0.13%**; halothane **0.52 ± 0.11% vs 1.28 ±
  0.07%** — roughly 2.5–3x more sensitive, the largest single-gene shift for volatiles found
  in mammals in this brief. n not obtained.
- **Zimin et al. 2016, Curr Biol** [SN]: restricting Ndufs4 loss to glutamatergic neurons
  reproduces the hypersensitivity; loss in GABAergic or cholinergic neurons does not.
- **Ramadasan-Nair et al. 2017, PLoS One** [AB]: knockdown of Ndufs4 in parietal association
  cortex alone gave about half the global-knockout shift; implicates a central-thalamus to
  parietal-cortex circuit.
- **Morgan, Hoppel, Sedensky 2002, Anesthesiology 96:1268** [AB] and a later multi-centre
  study of children having muscle biopsy for suspected mitochondrial disease [SN]: end-tidal
  sevoflurane to reach BIS 60 was **0.98% (95% CI 0.5–1.4) with complex I defects vs 2.2%
  (1.8–3.0)** in other complex defects/controls, p < .001. BIS is an EEG index, not a report
  of experience. n not obtained.
- Spencer 2023 [AB]: Ndufs4;Trek-1 double mutants were no different from Ndufs4 alone
  (halothane EC50 0.58% (0.07)).
- All from one research group (Morgan/Sedensky) across worms, mice and humans; independent-lab
  replication of the mouse result was not located. Open issue: whether hypersensitivity
  reflects complex I as the anaesthetic target, or a generally energy-compromised glutamatergic
  synapse that fails sooner whatever the target. Volatiles do inhibit complex I directly
  [MEM]. The effect is one of hypersensitivity; there is no complex-I manipulation shown to
  confer resistance in the sources retrieved. Not tested for i.v. agents or xenon in what I
  read (Ndufs4 mice reportedly not hypersensitive to propofol, and resistant to ketamine
  [MEM] — not verified).

---

## 7. S — presynaptic

- **van Swinderen, Saifee, Shebester, Roberson, Nonet, Crowder 1999, PNAS** [AB]: C. elegans
  syntaxin unc-64. md130 (a truncating/neomorphic allele) semidominantly confers "high-level
  resistance" to isoflurane and halothane; other hypomorphic alleles are hypersensitive;
  **33-fold range of isoflurane sensitivity** across syntaxin alleles (md130 20–30x higher
  EC50 than md1259/js21 [SN]). Authors: "inconsistent with nonspecific membrane-perturbation
  theories". Endpoint: coordinated movement. n not in abstract.
- Drosophila syntaxin1A H3-C (14-residue deletion): isoflurane resistance; preserved release
  at larval NMJ under isoflurane (Troup, Zalucki, Kottler, van Swinderen et al.,
  Anesthesiology 2019 [SN]). Cross-species consistency, but from an overlapping set of
  investigators.
- **Bademosi et al. 2018, Cell Reports** [SN]: single-molecule imaging; clinically relevant
  propofol and etomidate restrict syntaxin1A mobility (trapping in nanoclusters);
  non-anaesthetic analogues do the opposite. Isoflurane also restricts mobility; **ketamine
  and sevoflurane have little effect** (Hines et al. 2023 preprint [SN]) — i.e. not universal
  across agents.
- **Hemmings lab** [SN]: isoflurane at clinical concentrations inhibits Na-channel-dependent
  release of glutamate, GABA, ACh, dopamine and noradrenaline from isolated nerve terminals,
  glutamate most sensitive; attributed to presynaptic Na and Ca channel/exocytosis coupling.
  Westphalen et al. 2007 [SN title]: halothane inhibition of cortical glutamate and GABA
  release was reduced in Trek1−/− mice (links S to a K2P target; note Spencer 2023 found no
  behavioural phenotype in such mice).
- Morgan/Sedensky also report isoflurane inhibition of synaptic vesicle endocytosis in
  Ndufs4-deficient terminals [SN title] — a bridge between M and S.
- Mammalian in-vivo SNARE manipulation that shifts MAC or LORR: not found.

---

## 8. Prediction 3 — cross-kingdom action, and whether a target is identified

| Organism | Finding | Target identified? | Source |
|---|---|---|---|
| Plants (Mimosa, pea tendril, Venus flytrap, sundew, Arabidopsis root, cress seed) | Anaesthetics (diethyl ether, xenon, lidocaine among those used; exact concentrations not verified — ether doses in this literature are ~15% vapour [MEM], far above animal MAC of ~2–3%) reversibly stop touch-evoked and autonomous movements; ether abolishes flytrap action potentials; endocytic vesicle recycling and ROS balance altered | **No.** Authors propose membrane/vesicle-trafficking effects; no protein named | Yokawa et al. 2018 Ann Bot [AB] |
| Venus flytrap | Ether blocks propagation of the touch-evoked Ca2+/electrical signal from trigger hair into trap; a glutamate-receptor-like channel (GLR3.6) is proposed as a candidate | Candidate only (not confirmed by mutation) | Scherzer et al. 2022 Sci Rep [SN]; GLR detail [MEM] |
| Venus flytrap | Ether blocks jasmonate accumulation and JA-responsive genes; exogenous JA bypasses the block (i.e. block is upstream, at electrical signalling) | No | Pavlovič et al. 2020 Ann Bot [SN] |
| Paramecium | Isoflurane, sevoflurane, enflurane, ether alter swimming in a concentration-dependent way | No | [SN] |
| Tetrahymena | Long-chain alkanols impair growth with a cut-off pattern | No | [SN] |
| Firefly luciferase / luminous bacteria | Light output inhibited at animal EC50s | **Yes — luciferase (a soluble protein)** | Franks & Lieb 1984 [AB] |
| C. elegans | Sensitivity set by syntaxin, complex I, others | Yes (proteins) | sections 6–7 |
| Drosophila | Sensitivity altered by syntaxin1A, PLD (contested), complex I | Yes (proteins; PLD result is the membrane-pathway one) | sections 4, 7 |

Points for the adjudicator. (a) Plants have membranes and microtubules and also conserved
ion channels and SNAREs, so plant sensitivity does not discriminate L, Q or P. (b) No
organism with membranes or microtubules was identified as *insensitive*; I did not find a
systematic search for one. (c) Where a non-neural target has been pinned down (luciferase),
it is a protein. (d) Concentration matching between plant and animal studies was not
verified. (e) Kelz & Mashour 2019 Curr Biol review "from Paramecium to Primate" exists
[SN title] — not read.

---

## 9. Items by account — for and against, at a glance (no verdicts)

**L-classical.** For: Meyer–Overton across ~5 orders of magnitude; no enantioselectivity for
secondary alcohols; cross-kingdom action. Against: non-immobilizers and 2–14x deviations
(Koblin 1994); cut-off; 10x etomidate stereoselectivity; lipid-free luciferase reproduces the
correlation; single residue abolishes etomidate/propofol immobility; minimal bilayer change
at clinical doses (Herold 2017).

**L-modern.** For: PLD2-dependent TREK-1 activation in cells; raft changes at 1 mM; PLD-null
flies slower to sedate (~1.7x latency); purified TREK-1 in liposomes insensitive. Against /
open: fly result unreplicated, n = 2 brains per condition for imaging, criticised in print;
direct isoflurane binding site on TREK-1 with functional mutagenesis (Wague 2020); TREK-1/2
knockout mice not resistant (Spencer 2023); Herold 2017; concentrations ~3x MAC; no
non-anaesthetic controls.

**P.** For: β3 N265M abolishes etomidate/propofol immobility (replicated across backgrounds,
same group); HCN1 knockout reduces ketamine/propofol hypnosis (31% for forebrain knockout);
stereoselectivity paralleling receptor pharmacology; syntaxin alleles giving 33x range.
Against / open: no mutation abolishes any endpoint for volatiles (≤ 24%); hypnosis by i.v.
agents only reduced in β3 mice; TREK-1 result failed replication; xenon untested in vivo;
dozens of proteins bind halothane, so binding alone is weak evidence.

**Q.** For: xenon spin isotopes ~40–50% less potent (n = 20/group; unreplicated);
epothilone B delays isoflurane LORR by 69 s (d = 1.9, n = 8; unreplicated); epothilone D /
discodermolide raise anthracene-anaesthetic EC50 in tadpoles; tubulin is photolabelled;
computational THz correlation. Against / open: no replication of the xenon result in 8 years;
Li 2025 found a stabiliser and a destabiliser both *increase* isoflurane sensitivity in mice;
Khan 2024 unblinded order, latency endpoint, tolerance confound; Emerson's claim is restricted
to anthracene/some neurosteroids; taxane patients received similar inhaled concentrations
(P = 0.15); tubulin is one of ≥57 halothane-binding proteins; no tubulin mutant found in
anaesthesia screens (not exhaustively checked); lithium-isotope behavioural effects are from
two non-matching studies plus in-vitro work by the proposer's group, and concern no
anaesthetic.

**M.** For: complex I mutants hypersensitive in worms, mice (EC50 about one third), and
children (0.98% vs 2.2% sevoflurane at BIS 60); graded with complex I activity; cell-type and
region specific. Against / open: essentially one research group; hypersensitivity only;
target-versus-vulnerability ambiguity; agent coverage limited to volatiles.

**S.** For: syntaxin alleles shift volatile sensitivity up to 33x in worms and confer
resistance in flies; clinical concentrations inhibit transmitter release and syntaxin
mobility; non-anaesthetic analogues do not. Against / open: ketamine and sevoflurane have
little effect on syntaxin mobility; no mammalian in-vivo genetic test; overlapping
investigators.

---

## 10. Could not verify — flagged

1. Li 2018 full methods: isotopic purity, gas analysis, blinding, exact P-values, and whether
   the "xenon alone" ED50s were measured or extrapolated. Abstract only.
2. Isotope-to-ED50 pairing in Li 2018 was returned inconsistently by tools; pairing given is
   the one matching the title's conclusion.
3. Heurteaux 2004 per-agent numbers, n, and pentobarbital control (abstract + one secondary
   range of 7–48%).
4. Hansen reply to van Swinderen & Hines: only a snippet (n = 2 + 2 brains).
5. Li 2025 BMC Anesthesiol: paclitaxel result, n, dosing schedule, blinding (abstract only).
6. Linganna 2015 n; Emerson 2013 numerical EC50 shifts; Jurd 2003 group sizes.
7. gas-1 EC50 fold change; n for Quintana 2012 and the paediatric complex I study.
8. Cut-off primary sources, Cantor's lateral-pressure papers, Allison & Nunn 1968, Kandel 1996
   (F6 amnesia), neurosteroid enantiomer ratios, ketamine clinical potency ratio: from memory
   or snippets only.
9. Yokawa 2018 concentrations and n (abstract only); GLR3.6 as flytrap candidate target.
10. Duke thesis on "fundamental physics of anesthetic action" and Kelz & Mashour 2019 — seen
    in results, not opened; either could contain a xenon-isotope or cross-kingdom test.
11. Statement that no tubulin mutant alters anaesthetic sensitivity rests on absence in my
    searches only.
12. All "[FT]" extractions were made by an automated reader of the page, not checked line by
    line against the PDF.
