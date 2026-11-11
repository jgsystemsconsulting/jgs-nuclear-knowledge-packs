<!--
Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Pack backlog (potential skills)

Maintainer work queue for **new knowledge packs** in this sector repo. Not the
tooling advisory list in `docs/superpowers/backlog.md` (gitignored pipeline
state). This file is product scope: what packs could exist, in what order, from
which sources.

**Status of this catalogue:** research draft **2026-11-05**. Wave 1 source
titles and current revisions checked against NRC Division 1 / SRP Chapter 7
listings that day. Accession (ML) numbers marked **VERIFY** must be pinned from
the PDF cover sheet before packaging. Nothing here is committed work until a
row moves to `in-progress` and a pack directory exists.

---

## How to use this file

1. Pick a **theme**, not a random row. Finish the theme's wave-1 packs before
 jumping themes (orchestrator routing stays coherent).
2. Before any build: run the **acceptance checklist** at the bottom.
3. Pin sources in `PACK.yaml` with title, revision, date, and ML (or eCFR
 citation). No `source_url` fields (fleet link policy).
4. After a pack ships: set status `live`, add orchestrator rows, update
 `catalog.json`, capability map, and this file.
5. Rows are never deleted. Status only: `idea` → `ready` → `in-progress` →
 `live` | `deferred` | `rejected`.

### Status legend

| status | meaning |
|--------|---------|
| live | shipped in `packs/` |
| ready | sources Tier 1/2 clear, chapter sketch stable, safe to start |
| idea | plausible; pin/revision/size still open |
| deferred | valid later; blocked on dependency or size |
| rejected | will not package (anti-scope or licence wall) |
| signpost-only | name + edition forever; no body text |

### Kind

| kind | meaning |
|------|---------|
| content | full pack under `packs/<slug>/` |
| signpost | designation table only |
| orchestrator-extend | routing map rows only (no new content) |

### Wave

| wave | intent |
|------|--------|
| 0 | already live |
| 1 | next builds: Tier 1 certain, adjacent to digital I&C or licensing root |
| 2 | core plant engineering after wave 1 patterns proven |
| 3 | large SRP slices, advanced reactors, lower frequency |
| later | optional / international / thin demand |
| never | hard anti-scope or permanent signpost |

---

## Hard walls (do not backlog as content packs)

### Never in catalogue

See also root `README.md` § Out of scope and `/nuclear` Scope & Limits.

| id | topic | reason |
|----|-------|--------|
| never-01 | Nuclear weapons, warheads, delivery, weapons-design physics | Outside civilian plant charter; often classified |
| never-02 | Classified / export-controlled / safeguards-sensitive beyond public civil NRC text | No redistribution path |
| never-03 | NNSA / defence nuclear programmes as content | Public civil NRC only |
| never-04 | Medical use (10 CFR Part 35 and clinical nuclear medicine) | Wrong sector; not power-plant safety systems |
| never-05 | Consumer/industrial gauge and sealed-source programmes as primary scope | Outside power-plant digital I&C / plant engineering cut |
| never-06 | Pure reactor-physics or radiation-transport textbooks | No licensing deliverable |
| never-07 | Full text of paywalled standards (IEEE, IEC, ASME, ANS, NFPA, …) | SOURCE-VETTING Excluded |
| never-08 | Legal, licensing, or compliance **advice** | Reference notes only |
| never-09 | Reconstructing IAEA SSG/SSR body text without written reuse grant | Citation-only until grant filed in SOURCE-VETTING |

### Signpost-only forever (extend `nuclear-signpost`, never body text)

| id | family | notes |
|----|--------|-------|
| sp-ieee | IEEE 603, 7-4.3.2, 828, 829, 830, 1008, 1012, 1028, 1074, … | Endorsed by NRC RGs; paywalled |
| sp-iec | IEC 60880, 61513, 62138, … | Same |
| sp-asme | ASME BPVC, NQA-1, OM, … | Paywalled; RG may discuss NRC view only |
| sp-ans | ANS standards | Paywalled |
| sp-nfpa | NFPA 805 / 804 / 57 | Fire path cites NFPA; text stays owner-side |
| sp-iaea | IAEA SSG-39 and peers | Free to read; no pack body until reuse grant |

### Slice rule for huge PD sources

- **One NUREG-0800 chapter or one BTP/Appendix ≈ one pack** (or one tight BTP pair).
- **Do not** package entire SRP, entire GALL report, or "all of 10 CFR" as one skill.
- Prefer **RG family packs** (3-8 related RGs) or **single fat NUREG** with clear chapter map.
- Cap ambition: if source set exceeds ~400 PDF pages, split before authoring.

---

## Live inventory (wave 0)

| id | slug | kind | sources (pinned) | status |
|----|------|------|------------------|--------|
| live-01 | `nrc-nuclear` | content | RG 1.168 r2; 1.169-1.173 r1 (Jul 2013); BTP 7-14 r6 (Aug 2016); RG 1.152 r4 (Jul 2023); App 7.1-D r1 (Aug 2016) | live |
| live-02 | `nuclear-signpost` | signpost | IEEE/IEC/IAEA/ASME/NFPA/ANS name-only rows | live |
| live-03 | `nuclear` | orchestrator | routes to live packs | live |
| live-04 | `nrc-btp-7-18-plc` | content | BTP 7-18 Rev. 6, August 2016 (ML16019A327); listing-page pin 2026-11-07 | live |
| live-05 | `nrc-10cfr-part50-licensing-basis` | content | 10 CFR Part 50 selected slices: 50.2 key definitions, 50.34, 50.36, 50.54, 50.59, App A index, App B pointer; eCFR pin-check 2026-11-08 | live |
| live-06 | `nrc-qa-rg-1-28` | content | RG 1.28 Rev 6, September 2023 (ML23177A002); FR notice 2023-19548 pin 2026-11-08; NQA-1 named only | live |
| live-07 | `nrc-risk-informed-rg-1-174` | content | RG 1.174 Rev. 3, 2018 (ML17317A256); listing-page pin 2026-11-08; RG 1.200 and NUREG-1855 named only | live |
| live-08 | `nrc-cyber-rg-5-71` | content | RG 5.71 Rev. 1, February 2023 (ML22258A204); listing-page pin 2026-11-08; 10 CFR 73.54 eCFR pin-check 2026-11-09; G-02 and G-03 named only | live |
| live-09 | `nrc-accident-monitoring-rg-1-97` | content | RG 1.97 Rev. 5, May 2019 (ML18136A762); dual-source pin 2026-11-09; IEEE Std 497-2016 and NUREG-0700 named only | live |
| live-10 | `nrc-10cfr-part52-col` | content | 10 CFR Part 52 selected slices (eCFR pin-check 2026-11-11); RG 1.206 Rev 1 (ML18131A181) pin 2026-11-10 | live |
| live-11 | `nrc-app-b-criteria` | content | 10 CFR Part 50 Appendix B eighteen criteria lookup (eCFR pin-check 2026-11-11); RG 1.28 and NQA-1 named only | live |

---

## Theme index (work thematically)

| theme | title | wave focus | pack count (candidates) |
|-------|-------|------------|-------------------------|
| A | Digital I&C extension | 1 | 4 |
| B | Licensing & regulatory framework | 1 | 5 |
| C | QA / SSC / Appendix B | 1 | 3 |
| D | PRA / risk-informed | 1-2 | 4 |
| E | Safety / accident analysis | 2 | 4 |
| F | Human factors / HSI | 1-2 | 2 |
| G | Cyber & physical security (civil plant) | 1-2 | 3 |
| H | Fire protection | 2 | 2 |
| I | External hazards / seismic | 2 | 3 |
| J | Radiation protection (occupational plant) | 2 | 3 |
| K | Operations / tech specs | 2-3 | 3 |
| L | Aging / license renewal | 2-3 | 3 |
| M | Fuel / criticality / spent fuel (civil) | 3 | 3 |
| N | Emergency preparedness | 3 | 2 |
| O | Decommissioning | 3 | 2 |
| P | Advanced / non-LWR / SMR licensing | 2-3 | 4 |
| Q | Environmental / siting | 3 | 2 |
| R | Standards signpost expansion | 1 | 2 |
| S | International (careful licence) | later | 2 |
| T | Orchestrator & map maintenance | continuous | 2 |

---

## Theme A - Digital I&C extension

Closest to `nrc-nuclear`. Do these first after any tooling debt.

| id | slug | wave | kind | tier | status | primary sources (pin at build) | depends | user job |
|----|------|------|------|------|--------|--------------------------------|---------|----------|
| A-01 | `nrc-btp-7-18-plc` | 1 | content | 1 | live | NUREG-0800 **BTP 7-18 Rev. 6**, August 2016, ML16019A327. Listing-page pin 2026-11-07. PDF body not captured. | live-01 | Staff/applicant questions on PLCs in digital safety I&C |
| A-02 | `nrc-btp-7-19-d3` | 1 | content | 1 | deferred (fork-blocked, X1) | NUREG-0800 **BTP 7-19 Rev. 9**, May 2024, ML24005A077. Listing-page + FR pin 2026-11-08. Defense-in-depth and diversity / digital CCF. X15: out of pack body (P19 pointer) pending human fork. Do **not** start any A-02 pack body until fork X1 resolves: see "Carried fork" in docs/superpowers/packages/2026-11-10-pack-backlog-wave1-rest-packages.md. Guard marks the block only; it does not resolve X1 and does not amend X15. | live-01, A-01 | D3, CCF, coping analysis for digital upgrades |
| A-03 | `nrc-srp-ch7-ic-overview` | 2 | content | 1 | idea | NUREG-0800 **Chapter 7** intro + selected sections **excluding** 7-14/7-18/7-19/7.1-D already covered. Slice: 7.0, 7.1, App 7.0-A / 7.1-A only unless a later row takes more. | live-01 | What SRP Ch7 expects at system level |
| A-04 | `nrc-digital-ic-routing` | 1 | orchestrator-extend | n/a | deferred | No new sources. A-01 scope done: `nrc-btp-7-18-plc` is live and its Topics, NRC Agency, and Deliverables rows are in `packs/nuclear/SKILL.md`. Residual only: after the relevant A-02 or A-03 pack exists in `packs/` and is live, check its Topics and Deliverables routing and thin-pack step-down from `nrc-nuclear` (take the next pack on the row when the selected pack flags the question thin; at most six packs per Topics row). Add no row for a missing pack slug. T-01 continuous duty noted: after every live pack, update Topics, Agency, and Deliverables rows, thin-pack step-down, and anti-scope refuse paths; A-04 tracks only this Theme A residual. | A-02, A-03 | `/nuclear` finds digital packs |

**Chapter sketch A-01:** PLC role in safety I&C; software vs firmware boundary; life-cycle expectations vs BTP 7-14; commercial dedication touchpoints; failure modes staff eye; documentation set; anti-patterns; connects to RG 1.152 / 7.1-D.

**Chapter sketch A-02:** CCF concept for digital; D3 strategies; best-estimate plus uncertainty vs bounding; manual actions; diversity attributes; staff review focus; relationship to IEEE 7-4.3.2 (name-only); limits of the BTP.

**Risk A:** BTP 7-19 revision churn. Pin exact Rev + ML; state edition rule like `nrc-nuclear`.

---

## Theme B - Licensing & regulatory framework

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| B-01 | `nrc-10cfr-part50-licensing-basis` | 1 | content | 1 | live | **10 CFR Part 50** selected (domestic licensing of production and power reactor facilities). Slice: definitions, 50.34 contents of applications, 50.36 tech specs, 50.54 conditions, 50.59 changes, App A GDC overview, App B pointer only. eCFR pin date: check at build (pin-check 2026-11-08). | - | What is the Part 50 licensing basis shape |
| B-02 | `nrc-10cfr-part52-col` | 1 | content | 1 | live | **10 CFR Part 52** (ESP, DC, COL, ML). Pair with **RG 1.206 Rev 1** (Oct 2018) Applications for Nuclear Power Plants. eCFR pin date: check at build (pin-check 2026-11-08). | B-01 | COL / design cert application structure |
| B-03 | `nrc-part21-defect-reporting` | 2 | content | 1 | idea | **10 CFR Part 21** + **RG 1.234 Rev 1** (Mar 2024) Evaluating Deviations and Reporting Defects… | B-01 | Part 21 evaluation and reporting |
| B-04 | `nrc-srp-intro-review-process` | 2 | content | 1 | idea | NUREG-0800 **Introduction** and review process material only (not whole SRP). | B-01 | How staff use the SRP |
| B-05 | `nrc-operator-licensing-part55` | 3 | content | 1 | idea | **10 CFR Part 55** + related operator licensing NUREGs/RGs (**VERIFY** set). | B-01 | Operator licence requirements (civil plant) |

**Anti-scope touch:** B-05 is civil power reactor operators, not DoD.

**Chapter sketch B-01:** Regulation vs RG vs SRP; FSAR role; 50.59 change process; GDC map (index, not essay); tech spec role; App B as hook to Theme C; what this pack refuses (advice, plant-specific basis).

---

## Theme C - QA / SSC / Appendix B

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| C-01 | `nrc-qa-rg-1-28` | 1 | content | 1 | live | **RG 1.28 Rev 6** (Sep 2023) Quality Assurance Program Criteria (Design and Construction). NRC discussion of NQA-1 only; **NQA-1 text signpost-only**. | B-01 | QA program criteria staff accept |
| C-02 | `nrc-app-b-criteria` | 1 | content | 1 | live | **10 CFR 50 Appendix B** eighteen criteria (eCFR pin). eCFR pin date: check at build (pin-check 2026-11-08). Keep short; cross-link C-01. | C-01 | App B criterion lookup |
| C-03 | `nrc-qa-signpost-nqa1` | 1 | signpost | excluded | excluded (fold closed) | ASME NQA-1 editions commonly endorsed by RG 1.28 path: designation + edition + owner only. Folded into nuclear-signpost R-01 row expansion; no separate slug. | C-01 | Where to buy NQA-1 |

---

## Theme D - PRA / risk-informed

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| D-01 | `nrc-risk-informed-rg-1-174` | 1 | content | 1 | live | **RG 1.174 Rev. 3**, 2018, ML17317A256. Listing-page pin 2026-11-08. Approach for using PRA in risk-informed decisions on plant-specific licensing-basis changes. | B-01 | ΔCDF / ΔLERF style risk-informed change |
| D-02 | `nrc-pra-adequacy-rg-1-200` | 1 | content | 1 | ready | **RG 1.200 Rev. 3**, Dec 2020, ML20238B871. Listing-page pin 2026-11-08. PRA technical adequacy. | D-01 | Is the PRA good enough for this application |
| D-03 | `nrc-pra-nureg-1855` | 2 | content | 1 | idea | **NUREG-1855** (guidance on treatment of uncertainty in risk-informed decisionmaking) - **VERIFY** current Rev/ML. | D-01 | Uncertainty treatment |
| D-04 | `nrc-srp-ch19-pra` | 2 | content | 1 | idea | NUREG-0800 **Chapter 19** PRA and severe accident slices only. | D-01 | Staff review of PRA in applications |

**Risk D:** RG 1.174/1.200 revision pins drift. Always record ML + date.

---

## Theme E - Safety / accident analysis

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| E-01 | `nrc-transient-analysis-rg-1-203` | 2 | content | 1 | idea | **RG 1.203 Rev 0** Transient and Accident Analysis Methods (listing). | B-01 | Evaluation model / analysis method expectations |
| E-02 | `nrc-srp-ch15-accident-analysis` | 2 | content | 1 | idea | NUREG-0800 **Chapter 15** (split if huge: 15.0 overview pack, then event-class packs). | E-01 | FSAR Ch15 staff review topics |
| E-03 | `nrc-srp-ch4-reactor` | 3 | content | 1 | idea | NUREG-0800 **Chapter 4** reactor slice. | E-02 | Core/fuel design review interface |
| E-04 | `nrc-srp-ch6-esf` | 3 | content | 1 | idea | NUREG-0800 **Chapter 6** engineered safety features slice. | E-02 | ESF review topics |

---

## Theme F - Human factors / HSI

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| F-01 | `nrc-hsi-nureg-0700` | 1 | content | 1 | ready | **NUREG-0700 Revision 4** Human-System Interface Design Review Guidelines (NRC staff listing 2026-11-05). ML **VERIFY**. Large: chapter-map carefully; may ship as multi-chapter pack. | - | Control-room / HSI design review criteria |
| F-02 | `nrc-accident-monitoring-rg-1-97` | 1 | content | 1 | live | **RG 1.97** Criteria for Accident Monitoring Instrumentation, Rev. 5, May 2019, ML18136A762 (DG-1335 issued as final Rev. 5; provenance correction recorded 2026-11-09). | none | Post-accident monitoring instrumentation |

---

## Theme G - Cyber & physical security (civil plant)

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| G-01 | `nrc-cyber-rg-5-71` | 1 | content | 1 | live | **RG 5.71 Rev. 1**, Feb 2023, ML22258A204. Listing-page pin 2026-11-08. Pair **10 CFR 73.54**. | live-01 (SDOE contrast) | Cyber program vs RG 1.152 SDOE |
| G-02 | `nrc-part73-physical-security-overview` | 2 | content | 1 | idea | **10 CFR Part 73** selected civil power-reactor requirements (high-level map, not safeguards details that are sensitive). Stay on public eCFR text only. | G-01 | Physical security regulatory shape |
| G-03 | `nrc-security-rg-family` | 3 | content | 1 | idea | Additional Div 5 RGs as needed (**VERIFY** set; exclude anything non-public). | G-02 | Specialist security RG lookup |

**Anti-scope:** No classified DBT details, no weapons, no force-on-force tactics beyond public RG/regulation text.

---

## Theme H - Fire protection

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| H-01 | `nrc-fire-rg-1-189` | 2 | content | 1 | ready | **RG 1.189 Rev 5** (Oct 2023) Fire Protection for Nuclear Power Plants. | D-01 optional | Fire protection program / safe shutdown |
| H-02 | `nrc-fire-nfpa805-signpost` | 2 | signpost | excluded | ready | NFPA 805 / 804 designation rows only; NRC RG carries agency position. | H-01 | Where NFPA text lives |

---

## Theme I - External hazards / seismic

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| I-01 | `nrc-seismic-rg-1-208` | 2 | content | 1 | idea | **RG 1.208 Rev 0** Performance-Based Approach to Define Site-Specific Earthquake Ground Motion (Mar 2007; periodic reviews noted). | B-01 | Site seismic hazard / GMRS style topics |
| I-02 | `nrc-seismic-rg-1-60-family` | 2 | content | 1 | idea | **RG 1.60** and related seismic design RGs - **VERIFY** current set and revs from Div1 1.41-1.60. | I-01 | Design response spectra / seismic design input |
| I-03 | `nrc-external-hazards-srp-ch2-slice` | 3 | content | 1 | idea | NUREG-0800 **Chapter 2** site characteristics slice (flooding, nearby facilities, etc.). | I-01 | Site / external hazard review |

---

## Theme J - Radiation protection (occupational, power plant)

**Not medical.** No Part 35.

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| J-01 | `nrc-10cfr20-standards` | 2 | content | 1 | idea | **10 CFR Part 20** Standards for Protection Against Radiation (power-plant occupational focus). | - | Dose limits / program shape |
| J-02 | `nrc-rp-rg-8-family` | 2 | content | 1 | idea | Selected **Division 8** RGs (ALARA, instruction to workers, etc.) - **VERIFY** numbers/revs on Div 8 listing. | J-01 | ALARA and RP program guides |
| J-03 | `nrc-rp-not-medical-boundary` | 2 | orchestrator-extend | n/a | idea | Routing: Part 35 / medical → refuse per anti-scope. | J-01 | Hard stop medical questions |

---

## Theme K - Operations / tech specs

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| K-01 | `nrc-tech-specs-50-36` | 2 | content | 1 | idea | **10 CFR 50.36** + STS NUREG pointers (**NUREG-1430/1431/1432** family - **VERIFY** which editions are PD staff NUREGs vs plant-specific). | B-01 | What tech specs are for |
| K-02 | `nrc-operability-guidance` | 3 | content | 1 | idea | Public NRC operability guidance documents (**VERIFY** current IMC/RIS set and licence). | K-01 | Operability determination concepts |
| K-03 | `nrc-maintenance-rule-50-65` | 3 | content | 1 | idea | **10 CFR 50.65** Maintenance Rule + related RGs (**VERIFY**). | K-01 | Maintenance Rule scope |

---

## Theme L - Aging / license renewal

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| L-01 | `nrc-part54-license-renewal` | 2 | content | 1 | idea | **10 CFR Part 54** requirements for renewal of operating licenses. | B-01 | LR application shape |
| L-02 | `nrc-gall-slice` | 3 | content | 1 | idea | **NUREG-1801 GALL** (or successor) - **must slice** by system family; never one god-pack. First slice: electrical/I&C aging only if digital fleet priority. | L-01 | Aging management program templates |
| L-03 | `nrc-slr-guidance` | 3 | content | 1 | idea | Subsequent license renewal public guidance (**VERIFY** NUREG/RG set). | L-01 | SLR differences |

---

## Theme M - Fuel / criticality / spent fuel (civil)

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| M-01 | `nrc-criticality-safety-civil` | 3 | content | 1 | idea | Civil criticality safety RGs / NUREGs for fuel facilities and plant fuel handling (**VERIFY** Div 3 set). | - | Criticality safety program shape |
| M-02 | `nrc-part72-spent-fuel-storage` | 3 | content | 1 | idea | **10 CFR Part 72** spent fuel storage. | M-01 | ISFSI / storage licensing |
| M-03 | `nrc-part70-fuel-cycle-overview` | 3 | content | 1 | idea | **10 CFR Part 70** high-level map for fuel cycle facilities (civil). | M-01 | Fuel cycle facility licensing shape |

**Anti-scope:** No weapons-usable material process detail beyond public Part 70/72 text; no classified enrichment tech.

---

## Theme N - Emergency preparedness

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| N-01 | `nrc-ep-part50-47-app-e` | 3 | content | 1 | idea | **10 CFR 50.47** and **Appendix E** emergency planning. | B-01 | EP regulatory requirements |
| N-02 | `nrc-ep-nureg-0654` | 3 | content | 1 | idea | **NUREG-0654/FEMA-REP-1** current Rev (**VERIFY** ML and joint FEMA terms). | N-01 | EP evaluation criteria |

---

## Theme O - Decommissioning

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| O-01 | `nrc-decom-50-82` | 3 | content | 1 | idea | **10 CFR 50.82** and related decommissioning requirements. | B-01 | Permanent shutdown / decom process |
| O-02 | `nrc-decom-rg-family` | 3 | content | 1 | idea | Decommissioning RGs (**VERIFY** Div1/Div4 set). | O-01 | Decom planning guidance |

---

## Theme P - Advanced / non-LWR / SMR licensing

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| P-01 | `nrc-non-lwr-pdc-rg-1-232` | 2 | content | 1 | ready | **RG 1.232 Rev 0** (Apr 2018) Developing Principal Design Criteria for Non-Light Water Reactors. ML **VERIFY**: pin title, Rev, date, and ML from listing page at build. | B-02 | Non-LWR PDC development |
| P-02 | `nrc-non-lwr-ticap-rg-1-233` | 2 | content | 1 | ready | **RG 1.233 Rev 0** (Jun 2020) Technology-Inclusive, Risk-Informed, Performance-Based Methodology… non-LWR. ML **VERIFY**: pin title, Rev, date, and ML from listing page at build. | P-01, D-01 | TICAP / LMP-style licensing basis content |
| P-03 | `nrc-part53-framework` | 3 | content | 1 | idea | **10 CFR Part 53** if/when final and in eCFR (**VERIFY** rule status before start). Drafts are weak pins. | P-02 | Risk-informed advanced reactor framework |
| P-04 | `nrc-smr-col-delta` | 3 | content | 1 | idea | SMR-specific public guidance deltas vs RG 1.206 / Part 52 (**VERIFY** set). | B-02 | SMR COL differences |

---

## Theme Q - Environmental / siting

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| Q-01 | `nrc-nepa-part51-overview` | 3 | content | 1 | idea | **10 CFR Part 51** environmental protection regulations for domestic licensing. | B-01 | ER / EIS process shape |
| Q-02 | `nrc-siting-div4-rg-slice` | 3 | content | 1 | idea | Selected **Division 4** environmental and siting RGs (**VERIFY**). | Q-01 | Siting guidance lookup |

---

## Theme R - Standards signpost expansion

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| R-01 | `nuclear-signpost` expand | 1 | signpost | excluded | live | Add rows: IEEE 7-4.3.2-2016; ASME NQA-1 editions cited by RG 1.28 r6; NFPA 805; ANS common cites. Still name-only. | live-02 | Broader designation lookup |
| R-02 | `nuclear-signpost-owners-map` | 2 | signpost | excluded | idea | Owner → catalogue URL pattern only (no standard text). | R-01 | Where to purchase/read |

---

## Theme S - International (later, licence-gated)

| id | slug | wave | kind | tier | status | primary sources | depends | user job |
|----|------|------|------|------|--------|-----------------|---------|----------|
| S-01 | `iaea-ssg39-signpost` | later | signpost | excluded until grant | idea | IAEA SSG-39 designation row (already partly in live signpost). | live-02 | IAEA I&C guide cite |
| S-02 | `intl-regulator-signpost` | later | signpost | case-by-case | idea | CNSC / ONR / WENRA **public** page designations only after SOURCE-VETTING row. | - | Non-US regulator name map |

Do **not** start S until US wave 1-2 is stable. Sibling-sector rule still applies if a full non-US catalogue grows large.

---

## Theme T - Orchestrator & map maintenance

| id | slug | wave | kind | tier | status | notes |
|----|------|------|------|------|--------|-------|
| T-01 | `nuclear` map bump | continuous | orchestrator-extend | n/a | idea | After every live pack: Topics, Agency, Deliverables rows; thin-pack step-down; anti-scope refuse paths |
| T-02 | capability-map regen | continuous | tooling | n/a | idea | `generate_capability_map.py` + classification-rules for each new content pack |

---

## Recommended work order (thematic)

Execute top-down. Do not skip licensing/QA if digital extension is the only itch: routing needs B/C for half of real questions.

### Wave 1 sequence (suggested)

1. **A-01** BTP 7-18 PLC 
2. **A-02** BTP 7-19 D3/CCF 
3. **A-04** (deferred, residual only) + **T-01** (continuous) orchestrator rows for digital, gated on the relevant A-02/A-03 pack existing
4. **R-01** signpost row expansion (cheap) 
5. **B-01** Part 50 licensing-basis map (licensing root; C-01 and D-01 depend on B-01, so the licensing pair precedes the QA spine and the risk-informed pair)
6. **B-02** Part 52 + RG 1.206 
7. **C-01** + **C-02** + **C-03** QA spine 
8. **D-01** + **D-02** risk-informed pair 
9. **F-02** RG 1.97 (built before F-01; F-01 NUREG-0700 not built) 
10. **G-01** cyber RG 5.71 + 73.54 
11. **P-01** + **P-02** non-LWR pair (if advanced-reactor demand is live)

### Wave 2

H-01 fire; E-01/E-02 accident analysis; I-01 seismic; J-01/J-02 RP; L-01 Part 54; A-03 SRP Ch7 overview.

### Wave 3

M/N/O fuel-EP-decom; K ops; P-03 Part 53 when final; Q environmental; remaining SRP chapter slices.

---

## Per-pack acceptance checklist

Before `packs/<slug>/` exists:

1. [ ] Topic is **not** on Never list and not medical/weapons/classified. 
2. [ ] Every source is Tier 1 or Tier 2 per `docs/SOURCE-VETTING.md`; Excluded material is signpost-only. 
3. [ ] Each PDF/NUREG has **title, Rev, date, ML** (or eCFR generation date) recorded; VERIFY cleared. 
4. [ ] Slice is small enough (prefer &lt; ~400 pages source or a clean chapter cut). 
5. [ ] Chapter list (5-12) drafted; no invented frameworks beyond source. 
6. [ ] `PACK.yaml` licence fields match source; pack `LICENSE` is source terms. 
7. [ ] Orchestrator Topics/Deliverables rows drafted. 
8. [ ] Capability-map / classification-rules impact noted. 
9. [ ] Anti-scope lines written into pack `## Scope & Limits`. 
10. [ ] `validate_pack.py` + `check_release.py` plan includes the new slug.

---

## Research log (2026-11-05)

| check | result |
|-------|--------|
| NRC Div 1 listing (new URL shape `regulatory-guides-by-division/division-1---power-reactors/…`) | Reachable; range pages omit dots in path (`regulatory-guides-1161---1180`) |
| RG 1.28 | **Rev 6, Sep 2023**, Quality Assurance Program Criteria (Design and Construction) |
| RG 1.189 | **Rev 5, Oct 2023**, Fire Protection for Nuclear Power Plants |
| RG 1.152 | **Rev 4, Jul 2023** (already live) |
| RG 1.97 | Accident monitoring; Rev. 5, May 2019, ML18136A762 (DG-1335 issued as final Rev. 5; provenance correction 2026-11-09) |
| RG 1.174 | Risk-informed PRA decisions; pin current Rev/ML at build (DG-1285 history present) |
| RG 1.203 | Rev 0 transient/accident analysis methods |
| RG 1.206 | **Rev 1, Oct 2018**, Applications for Nuclear Power Plants |
| RG 1.208 | Rev 0 site-specific earthquake ground motion |
| RG 1.232 | **Rev 0, Apr 2018**, non-LWR PDC |
| RG 1.233 | **Rev 0, Jun 2020**, non-LWR TICAP methodology |
| RG 1.234 | **Rev 1, Mar 2024**, Part 21 deviations/defects |
| SRP Ch7 | BTP 7-14 r6 08/2016; BTP 7-18 r6 08/2016; BTP 7-19 present (pin latest Rev/ML at build); App 7.1-D r1 08/2016 |
| NUREG-0700 | **Revision 4** listed on staff NUREG page |
| Wave-1 pin gate (P9) | BTP 7-19 R9 ML24005A077; RG 1.174 R3 ML17317A256; RG 1.200 R3 ML20238B871; RG 5.71 R1 ML22258A204; all VERIFY cleared 2026-11-08 |
| Div 5 cyber RGs | Listing reachable; **5.71 Rev/ML VERIFY** on range page at build |
| Part 53 | Do not package until final eCFR text exists |

Offline domain knowledge filled chapter sketches and theme cuts. ML accessions for new packs are intentionally **VERIFY** except where already pinned in live `nrc-nuclear` / catalog.

---

## Counts

| bucket | count |
|--------|-------|
| Live packs/skills | 11 |
| Content candidates | ~45 |
| Signpost candidates | ~6 |
| Orchestrator-extend | ~4 |
| Never rows | 9 |
| Themes | A-T (20) |

When a theme finishes wave 1, add a one-line **Theme completion** note under Research log with date and commit SHA.
