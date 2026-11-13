# Architecture

## AD-1
status: accepted
source: 2026-11-06-scaffold-todo-guard

Scan raw text, not parsed fields. parse_simple_yaml skips block scalars and nested mapping headers, so notes and build.built_on never reach parsed meta. The guard reads PACK.yaml and LICENSE with read_text and scans lines.

## AD-2
status: accepted
source: 2026-11-06-scaffold-todo-guard

Keep three separate checks and three exact error strings, appended in built_on, notes, LICENSE order inside check_pack before return errors. Exact-list test asserts pin that order. No shared helper and no new module.

## AD-3
status: accepted
source: 2026-11-06-scaffold-todo-guard

build_pack behavior stays unchanged. Scaffolds still carry TODOs as author prompts. Rejection lives in validate_pack, so an unfilled scaffold fails validation instead of shipping silently.

## AD-4
status: accepted
source: 2026-11-06-scaffold-todo-guard

The test helper build_pack in tooling/test_validate_pack.py stays unchanged. New cases overwrite the helper-written PACK.yaml and LICENSE in place, so cases 1 to 21 keep their fixtures.

## AD-5
status: accepted
source: 2026-11-07-a01-btp-7-18-plc

Chapter files are the eight A-01 sketch topics with the filenames locked in spec 2026-11-07-a01-btp-7-18-plc. No ninth chapter. No rename that follows an unread BTP outline.

## AD-6
status: accepted
source: 2026-11-07-a01-btp-7-18-plc

PACK.yaml licence fields are license "Public Domain (US Government work, 17 U.S.C. 105)", license_tier 1, commercial_use true, share_alike false, attribution_required false. Scaffold TODO lines in PACK.yaml and LICENSE are replaced before validation.

## AD-7
status: accepted
source: 2026-11-07-a01-btp-7-18-plc

Orchestrator edits add routing rows for nrc-btp-7-18-plc only. Rows for A-02, A-03, and the A-04 package are not added. Files under packs/nrc-nuclear are not edited.

## AD-8
status: verified
source: 2026-11-10-a02-fork-guard

Guard mechanism is dual signal on the A-02 row only: status value deferred from the existing legend plus explicit DO-NOT-START guard text naming fork X1. No new status value and no legend edit. The row guard text carries the why, so the legend stretch from dependency or size to fork-blocked stays self-documenting on the row. Wave sequence item 2 at docs/PACK-BACKLOG.md:373 is not annotated in this package; the A-02 row is the status source of truth and the stale sequence listing is a documented residual owned by later routing or status-hygiene work.

## AD-9
status: verified
source: 2026-11-13-b09-routing-write

A terminal routing write is the routing or touch run earlier pack specs defer cross-pack staleness to. It may fix a stale deferral-tense line in a live pack body if the change is one line, names the now-live replacement in prose only with no slug link and no source-material URL, adds no substance or structure, and preserves named-only and pointer discipline. Everything beyond that narrow class stays owned by a future pack-touch run.

## AD-10
status: verified
source: 2026-11-13-ci-gate-probe-hardening

Snapshot, never mutate. Positive runs take cwd inside probe-private TemporaryDirectory. Input set is tracked file list from git ls-files -z at ROOT. Copies land in tree mirroring recorded relative paths with bytes copied, no links, so .git and untracked or gitignored inputs never enter.
Listing failure (no git, nonzero exit, empty listing, unparseable path) raises SystemExit naming cause and never falls back to running against ROOT.
Alternatives rejected: skip-on-sources, canonical move-aside with unique temp stash (still renames live checkout and needs restore protocol), allowlist parameter on consumer side (name collision class stays open).

## AD-11
status: verified
source: 2026-11-13-ci-gate-probe-hardening

Child decode in run_gate and check_release.py short-SHA call pinned encoding="utf-8", errors="replace" beside text=True. Child subprocess environment sets PYTHONIOENCODING="utf-8" so child stdout emits UTF-8 across all platforms. Never switch to raw bytes mode: text mode universal-newline translation preserved, so demo needles keep matching CRLF child output on Windows.

## AD-12
status: verified
source: 2026-11-13-ci-gate-probe-hardening

Module docstring stays plain string, no raw prefix. sources\ becomes sources/ and backslash leaves docstring entirely. Section-marker and catalogue prose survive verbatim, so native triple-quote literals need no rewrite.

## AD-13
status: verified
source: 2026-11-13-build-provenance-guard

Mechanism is one name, ".zcode", added to existing SKIP_DIRS set literal in check_release.py main(), matched by path part like every other member. No allowlist parameter, no .gitignore parsing, no glob rule, and no per-scan exemption. Any directory named .zcode at any depth is skipped, matching .build and .planning semantics; tracked-tree check (git ls-files, zero .zcode paths, .gitignore line .zcode/) boundary keeps skip from hiding shippable content. Explanation extends comment block already above SKIP_DIRS; no new document.

## AD-14
status: verified
source: 2026-11-13-build-provenance-guard

Provenance fallback is a maintainer procedure in existing docs only, Federal Register first and ADAMS second. No tooling fetches, parses, or validates Federal Register or ADAMS records, and no fallback URL is stored. Enforcement is pin-note review plus existing VERIFY gate in docs/PACK-BACKLOG.md acceptance checklist. Alternatives rejected: waiting for new NRC listing URL family (volatile, blocks re-checks), PDF cover sheet only (PDF body often not captured for pin-only packs), and automated listing fetch (network dependency and bot-wall variance for four metadata fields).
## AD-15
status: verified
source: 2026-11-13-nrc-non-lwr-pdc-rg-1-232

Contents provenance is fixed as first pin: RG 1.232 Rev 0 (April 2018) verified via Federal Register notice 83 FR 15178 (April 9, 2018), ADAMS ML17325A611, with no prior on-record listing pin and no on-record captured RG 1.232 body. PACK.yaml follows the live single-RG tier-1 pattern: license "Public Domain (US Government work, 17 U.S.C. 105)" (the Public Domain prefix satisfies check_release licences parity and the test_ci_gate P17 pin), license_tier 1, commercial_use true, share_alike false, attribution_required false. The pack LICENSE carries the standard public domain notice for US Government work, mirroring packs/nrc-risk-informed-rg-1-174/LICENSE, naming one source. Repository tooling stays under the repository MIT licence; dispatch wording "PACK.yaml license MIT" rejected because every tier-1 RG pack records Public Domain and check_release.py licences rule 6 exempts only licences starting with "Public Domain". A live NRC listing that resolves at build but conflicts with the FR pin stops the build for maintainer re-vetting per req-31; a dead or absent listing never blocks on the FR pin alone.

## AD-16
status: verified
source: 2026-11-13-nrc-non-lwr-pdc-rg-1-232

All nine new notes (seven chapters, glossary.md, cheatsheet.md) sit in the existing cluster "Regulatory Framework & Staff Review"; no new cluster is created despite the dispatch allowing one. The pack subject is design-criteria formulation under 10 CFR 50.34 and 10 CFR Part 52 application-content rules, the same licensing-frame family as packs/nrc-10cfr-part50-licensing-basis/ and packs/nrc-10cfr-part52-col/, and one-cluster placement keeps capability-map retrieval with those neighbours and limits THRESHOLDS edits to one cluster value (34 to 43) plus EXPECTED_NOTES_COUNT (92 to 101). A new cluster (for example Advanced Reactors & Non-LWR Licensing) is deferred until a second non-LWR pack (nrc-non-lwr-ticap-rg-1-233) ships; that later run re-clusters as one documented move. Rejected: Risk-Informed Decisionmaking (the pack is PDC development, not PRA adequacy) and a new nine-note cluster (single-pack clusters fragment retrieval and add threshold-key churn for no retrieval gain).

## AD-17
status: verified
source: 2026-11-13-nrc-non-lwr-ticap-rg-1-233

Contents provenance is fixed as first pin: RG 1.233 Rev 0 (June 2020) verified via Federal Register notice 85 FR 35339 (June 9, 2020), ADAMS ML20091L698, with no prior on-record listing pin and no on-record captured RG 1.233 or NEI 18-04 body. PACK.yaml follows the live single-RG tier-1 pattern: license "Public Domain (US Government work, 17 U.S.C. 105)" (the Public Domain prefix satisfies check_release licences parity and the test_ci_gate P17 pin), license_tier 1, commercial_use true, share_alike false, attribution_required false. The pack LICENSE carries the standard public domain notice for US Government work, mirroring packs/nrc-risk-informed-rg-1-174/LICENSE, naming one source. Repository tooling stays under the repository MIT licence; MIT never governs pack content. NEI 18-04 is a copyrighted industry document named only and never a pack source. A live NRC listing that resolves at build but conflicts with the FR pin stops the build for maintainer re-vetting per req-31; a dead or absent listing never blocks on the FR pin alone.

## AD-18
status: verified
source: 2026-11-13-nrc-non-lwr-ticap-rg-1-233

All nine new notes (seven chapters, glossary.md, cheatsheet.md) sit in the existing cluster "Regulatory Framework & Staff Review" and all nine notes of packs/nrc-non-lwr-pdc-rg-1-232/ stay put; no new cluster is created and no note moves cluster in this run. One-cluster placement keeps capability-map retrieval with the Part 50, Part 52, and RG 1.232 licensing-frame neighbours and limits THRESHOLDS edits to one cluster value (43 to 52) plus EXPECTED_NOTES_COUNT (101 to 110). The new cluster AD-16 anticipated "until a second non-LWR pack ships" is declined at that trigger in this run: dispatch fixes cluster counts 43 to 52 (52 equals 43 plus this pack alone, which requires zero moves), re-clustering two packs would touch 18 note assignments and two threshold keys for no retrieval gain before any retrieval evidence exists, and a later run may re-cluster as one documented move. Rejected: Risk-Informed Decisionmaking (the pack is licensing-basis and application-content methodology, not PRA adequacy) and a new eighteen-note non-LWR cluster (no retrieval evidence, contradicts the dispatched count).

## AD-19
status: accepted
source: 2026-11-13-nrc-fire-rg-1-189

Contents provenance is fixed as first pin: RG 1.189 Rev 5, Fire Protection for Nuclear Power Plants (October 2023; published November 2023), verified via Federal Register notice 88 FR 76989 (November 8, 2023; notice 2023-24621), ADAMS ML23214A287, with no prior on-record listing pin and no on-record captured RG 1.189 PDF body. PACK.yaml follows the live single-RG tier-1 pattern: license "Public Domain (US Government work, 17 U.S.C. 105)" (the Public Domain prefix satisfies check_release licences parity and the test_ci_gate P17 pin), license_tier 1, commercial_use true, share_alike false, attribution_required false. The pack LICENSE carries the standard public domain notice for US Government work, mirroring packs/nrc-risk-informed-rg-1-174/LICENSE, naming one source. Repository tooling stays under the repository MIT licence; MIT never governs pack content. NFPA standards are copyrighted paywalled documents and are never a pack source; NFPA 805 and NFPA 804 appear only as signpost designations in packs/nuclear-signpost/. A live NRC listing that resolves at build but conflicts with the FR pin stops the build for maintainer re-vetting per req-31; a dead or absent listing never blocks on the FR pin alone.

## AD-20
status: accepted
source: 2026-11-13-nrc-fire-rg-1-189

All nine new notes (seven chapters, glossary.md, cheatsheet.md) sit in a new cluster "Fire Protection Programs" with THRESHOLDS 9; no existing note moves cluster in this run. EXPECTED_NOTES_COUNT moves 110 to 119. A dedicated cluster is taken this run rather than reusing Regulatory Framework & Staff Review or Risk-Informed Decisionmaking because fire protection program, fire hazards analysis, and post-fire safe shutdown queries form a distinct retrieval family from licensing-frame and PRA-adequacy queries, and the dispatch allows a new cluster. Rejected: Regulatory Framework & Staff Review (the pack is a plant fire protection program guide, not licensing-frame machinery) and Risk-Informed Decisionmaking (the pack covers deterministic fire protection and safe shutdown orientation with the performance-based NFPA 805 path named at framework depth only, not PRA adequacy).
