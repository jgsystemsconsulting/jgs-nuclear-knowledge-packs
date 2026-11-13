# Requirements

## req-1
status: accepted
source: 2026-11-06-scaffold-todo-guard

check_pack rejects a pack whose PACK.yaml raw text has a line whose stripped form equals built_on: "TODO" with the error PACK.yaml build.built_on is still "TODO" (record the build date/provenance).

## req-2
status: accepted
source: 2026-11-06-scaffold-todo-guard

check_pack rejects a pack whose PACK.yaml has a line whose stripped form starts with TODO: with the error PACK.yaml notes still contain the TODO placeholder (record licence condition carry-forward).

## req-3
status: accepted
source: 2026-11-06-scaffold-todo-guard

check_pack rejects a pack whose LICENSE has a line whose stripped form starts with TODO: with the error LICENSE still contains the TODO placeholder (reproduce the source's licence terms).

## req-4
status: accepted
source: 2026-11-06-scaffold-todo-guard

TODO scans are line-anchored. Only a line whose stripped form starts with TODO: triggers req-2 or req-3. Mid-sentence TODO text and the word TODOs do not trigger either error.

## req-5
status: accepted
source: 2026-11-06-scaffold-todo-guard

The PACK.yaml TODO checks apply to every pack kind. The LICENSE TODO check runs only when LICENSE exists. A missing LICENSE keeps only the existing missing-LICENSE error, and signpost and orchestrator packs without LICENSE gain no TODO error.

## req-6
status: accepted
source: 2026-11-06-scaffold-todo-guard

build_pack.py keeps writing scaffold TODOs unchanged. Only its step 5 print changes, to warn that validate_pack now rejects unfilled TODOs.

## req-7
status: accepted
source: 2026-11-06-scaffold-todo-guard

CONTRIBUTING.md build step 3 states the same warning: validate_pack rejects unfilled TODOs.

## req-8
status: accepted
source: 2026-11-06-scaffold-todo-guard

Regression cases 22, 23, and 24 in tooling/test_validate_pack.py cover the combined scaffold TODO failure, a filled pack pass, and a LICENSE-only TODO failure. Live packs keep passing validation.

## req-9
status: accepted
source: 2026-11-07-a01-btp-7-18-plc

The content pack at packs/nrc-btp-7-18-plc has one primary source. The listing-page pin is NUREG-0800 Branch Technical Position 7-18, title "Guidance on the Use of Programmable Logic Controllers in Digital Computer-Based Instrumentation and Control Systems", Rev. 6, August 2016, ML16019A327. That listing-page record is the pin. The PDF body was not captured. No second primary source is added.

## req-10
status: accepted
source: 2026-11-07-a01-btp-7-18-plc

Pack prose is synthesized orientation from the pin and the A-01 chapter sketch. It does not quote the BTP, cite unread BTP section numbers, or state acceptance criteria as BTP requirements. IEEE and IEC standards are designation and edition only. The pack is not legal or licensing advice. Shippable files carry no source-material URL.

## req-11
status: accepted
source: 2026-11-07-a01-btp-7-18-plc

The slug nrc-btp-7-18-plc is registered as a live catalog.json content entry, an SKILLS.md index row, a Topics target and an NRC agency target, a classification-rules assignment with a matching note for every chapter and support file, and a cursor plugin skill path. Landing catalogue counts show 2 content packs and 1 signpost. validate_pack and check_release pass on the filled tree.

## req-12
status: accepted
source: 2026-11-09-g01-cyber-rg571

Pack at packs/nrc-cyber-rg-5-71/ with 7 chapters, glossary, cheatsheet; registered across the full surface per the registration table (live catalog entry, SKILLS row, Topics targets, NRC agency target, Deliverables row, classification-rules assignments with notes, plugin path, PACK-BACKLOG G-01 status flip with Counts 7 to 8 and live-08, CHANGELOG bullet, EXPECTED_NOTES_COUNT 49 to 58 and THRESHOLDS refreshed from regen among them). validate_pack and check_release pass.

## req-13
status: accepted
source: 2026-11-09-g01-cyber-rg571

Content is synthesized orientation from RG 5.71 Rev. 1 pinned facts, carried nrc-nuclear SDOE-fence facts, and the closed list of RG 5.71 and 73.54 framework statements only. No security-control implementation guidance; no threat-actor or tactic detail; no DBT references; no force-on-force tactics beyond public RG/regulation text; no weapons content; no export-controlled or safeguards-sensitive content beyond public civil NRC text. G-02 and G-03 named-only (idea stage, no slugs). No legal advice. Not a plant-specific cyber security program. Zero quotations.

## req-14
status: verified
source: 2026-11-10-a02-fork-guard

The A-02 row at docs/PACK-BACKLOG.md:153 shows status deferred, not ready. The row states a DO-NOT-START guard naming fork X1 and the carried fork record. The guard marks the block only; it does not resolve fork X1, does not amend SOURCE-VETTING X15, and does not authorize any A-02 pack body.

## req-15
status: verified
source: 2026-11-10-a02-fork-guard

Only the A-02 row at docs/PACK-BACKLOG.md:153 changes. No other backlog row, chapter sketch, Risk A line, wave sequence item, Counts value, pack file, catalogue entry, SOURCE-VETTING line, orchestrator row, or tooling file changes in this package.

## req-16
status: verified
source: 2026-11-10-b06-part52-col

Pack at packs/nrc-10cfr-part52-col/ with 7 chapters, glossary, cheatsheet; registered across the full surface per the registration table (live catalog entry, SKILLS row, Topics targets, NRC agency target, Deliverables row, classification-rules assignments with notes, plugin path, PACK-BACKLOG B-02 status flip with Counts 9 to 10 and live-10, CHANGELOG bullet, EXPECTED_NOTES_COUNT 67 to 76 and Regulatory Framework THRESHOLDS 25 to 34 refreshed from regen among them). validate_pack and check_release pass.

## req-17
status: verified
source: 2026-11-10-b06-part52-col

Content is synthesized orientation from public 10 CFR Part 52 eCFR slices verified against the build-time eCFR As-of pin and RG 1.206 Rev. 1 (October 2018, ML18131A181) pin facts only. No wholesale verbatim; verbatim excerpts capped at two sentences; no unread RG section numbers stated as requirements; no source-material URLs in shippable files. Selected slices only, not all of Part 52. Not legal or licensing advice; not a plant-specific licensing basis. Part 53 and non-LWR principal design criteria out of scope, named only without slugs. Advice requests refused.

## req-18
status: verified
source: 2026-11-11-b07-app-b-criteria

Pack at packs/nrc-app-b-criteria/ with 6 chapters, glossary, cheatsheet; registered across the full surface per the registration table (live catalog entry, SKILLS row, Topics targets, NRC agency target, Deliverables row, classification-rules assignments with notes, plugin path, PACK-BACKLOG C-02 status flip with Counts 10 to 11 and live-11, CHANGELOG bullet, EXPECTED_NOTES_COUNT 76 to 84 and Quality Assurance Criteria THRESHOLDS 8 to 16 refreshed from regen among them). validate_pack and check_release pass.

## req-19
status: verified
source: 2026-11-11-b07-app-b-criteria

Content is a synthesized criterion lookup for the eighteen criteria I to XVIII of 10 CFR Part 50 Appendix B, built from the live eCFR Appendix B text at the build-time As-of pin only. Each criterion carries its roman numeral, its title, and its requirement substance in reference-note form. No wholesale verbatim; verbatim excerpts capped at two sentences; no source-material URLs in shippable files. RG 1.28 and NQA-1 named only, never slug-linked and never summarized. Not legal or licensing advice; not a plant-specific QA program. Advice requests refused.

## req-20
status: verified
source: 2026-11-11-b08-rg1200

Pack at packs/nrc-pra-adequacy-rg-1-200/ with 6 chapters, glossary, cheatsheet; registered across the full surface per the registration table (live catalog entry, SKILLS row, re-pointed PRA quality Topics target, NRC agency target, Deliverables row, classification-rules assignments with notes, plugin path, PACK-BACKLOG D-02 status flip with Counts 11 to 12 and live-12, CHANGELOG bullet, EXPECTED_NOTES_COUNT 84 to 92 and Risk-Informed Decisionmaking THRESHOLDS 8 to 16 refreshed from regen among them). validate_pack and check_release pass.

## req-21
status: verified
source: 2026-11-11-b08-rg1200

Content is synthesized orientation on PRA technical adequacy from the RG 1.200 Rev. 3 listing-page pin (December 2020, ML20238B871; pin 2026-11-08, listing re-checked at build) and the closed framework statements only. Zero quotations; verbatim excerpts capped at two sentences by licence policy; no source-material URLs in shippable files. ASME/ANS RA-Sa-2009 designation and endorsement fact only, no standard text. RG 1.174 named in prose as the decision-framework neighbour and never slug-linked; NUREG-1855 and SRP Chapter 19 named only, never summarized. No plant-specific adequacy verdict, no PRA quantification how-to, no legal or licensing advice. Advice requests refused.

## req-22
status: verified
source: 2026-11-13-b09-routing-write

Terminal b-09 write verifies the routing map in packs/nuclear/SKILL.md across nrc-10cfr-part52-col, nrc-app-b-criteria, and nrc-pra-adequacy-rg-1-200; runs check_capability_map and check_release; and updates PACK-BACKLOG dependency wording left stale by B-02 and D-01 going live (P-01 and P-02 depends cells annotated `B-02 (live)` / `P-01, D-01 (live)`; A-04 confirmed read-only, no edit). No status cell changes, no routing row edits, and T-01 and T-02 rows stay byte-identical. Two stale deferral-tense lines (D-01 ch06 and Part 50 ch07) become present-tense hook-sentences under the AD-9 exception in the same write; no other pack body changes.

## req-23
status: verified
source: 2026-11-13-ci-gate-probe-hardening

Importing tooling/test_ci_gate.py under python -W error::SyntaxWarning emits no SyntaxWarning. Module docstring has no invalid escape sequence; sources/ prose carries no backslash.

## req-24
status: verified
source: 2026-11-13-ci-gate-probe-hardening

run_gate in tooling/test_ci_gate.py passes encoding="utf-8", errors="replace" next to text=True and ensures child stdio uses UTF-8. Probe exits 0 on clean checkout under plain python, under python -I, and under python -I with PYTHONUTF8=1.

## req-25
status: verified
source: 2026-11-13-ci-gate-probe-hardening

Evidence artefact proves child decode fix covers cp1252 fault: pre-fix cp1252 decode of child output containing non-ASCII characters (such as section sign and middot) results in mojibake or decode error, whereas explicit UTF-8 decode cleanly reproduces the expected characters.

## req-26
status: verified
source: 2026-11-13-ci-gate-probe-hardening

Every text read and write in tooling/test_ci_gate.py and tooling/check_release.py names encoding= explicitly; second subprocess decode in check_release.py (git short SHA) pinned too. Strict kept where present; existing errors="ignore" sites kept; none added.

## req-27
status: verified
source: 2026-11-13-ci-gate-probe-hardening

Section 4 of tooling/test_ci_gate.py main() runs nine positive gates against probe-private snapshot under TemporaryDirectory: tracked file list from git ls-files -z, any listing failure aborts run, copied bytes only, snapshot contains no .git entry and no sources/ entry beyond tracked sources/.gitkeep.
With local sources/ inputs present probe exits 0 and sources/ tree hash before and after run equal.
Two probes run at once against one checkout both exit 0; killing probe mid snapshot leaves checkout byte-identical.

## req-28
status: verified
source: 2026-11-13-ci-gate-probe-hardening

.github/workflows/validate.yml unchanged. No gate logic, threshold, version, or heredoc literal moves. Every pinned parity pair in test_ci_gate.py still resolves; check_release.py edit, if any, touches decode arguments only.

## req-29
status: verified
source: 2026-11-13-ci-gate-probe-hardening

Local scratch trip notice in test_ci_gate.py docstring rewritten to describe probe-private snapshot mechanic; manual move-aside, fresh-clone or worktree precondition, and restore step no longer documented as run requirements.

## req-30
status: verified
source: 2026-11-13-build-provenance-guard

tooling/check_release.py main() SKIP_DIRS includes ".zcode" beside ".planning" and ".superpowers", and whole-repo leak sentinel and source-material link scans skip every path with a .zcode part. Comment above SKIP_DIRS states .zcode/ holds maintainer session working state and temporary research scratch, never ships in releases, and legitimately holds research URLs as working evidence, same precedent as .planning and .superpowers. Seeded scratch file under .zcode/ holding leak sentinel and source-material URL does not fail check_release.py; same seeded content outside .zcode/ still fails. No other SKIP_DIRS member and no scan logic changes.

## req-31
status: verified
source: 2026-11-13-build-provenance-guard

NRC listing-page provenance fallback is documented in docs/PACK-BACKLOG.md status catalogue note, docs/PACK-BACKLOG.md per-pack acceptance checklist item 3, and docs/SOURCE-VETTING.md cleared families note. Rule reads: NRC listing-page URL families are volatile post NRC site restructure and may return 404 (dead listing, not bot-wall); when listing re-check fails, verify title, revision, date, and ML accession number first from Federal Register publication notice of RG or NUREG (FR-first), and then ADAMS accession lookup if FR notice lacks any field. If a live listing resolves but conflicts with recorded pin values, stop for maintainer re-vetting; fallback does not overrule a live listing. Pin note records fallback used and FR notice number and citation or ADAMS lookup date. Already recorded listing-page pins stay valid without retroactive re-pin. If neither fallback confirms all four fields, VERIFY stays uncleared and packaging does not proceed. No listing, FR, or ADAMS URL is stored in any shippable file.

## req-32
status: verified
source: 2026-11-13-build-provenance-guard

Change surface is closed. Only tooling/check_release.py SKIP_DIRS literal and comment block above it, docs/PACK-BACKLOG.md status catalogue note and acceptance checklist item 3, docs/SOURCE-VETTING.md cleared families note, and test or probe additions proving req-30 seeded cases may change. No pack body, PACK.yaml, LICENSE, catalogue, routing, classification, backlog row, existing pin, validate_pack.py, build_pack.py, or test_ci_gate.py logic changes. docs/superpowers/backlog.md promotion closure for b07-app-b-criteria-1 and b08-rg1200-1 stays in backlog grooming, not this run.
