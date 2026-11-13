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
status: accepted
source: 2026-11-13-ci-gate-probe-hardening

Snapshot, never mutate. Positive runs take cwd inside probe-private TemporaryDirectory. Input set is tracked file list from git ls-files -z at ROOT. Copies land in tree mirroring recorded relative paths with bytes copied, no links, so .git and untracked or gitignored inputs never enter.
Listing failure (no git, nonzero exit, empty listing, unparseable path) raises SystemExit naming cause and never falls back to running against ROOT.
Alternatives rejected: skip-on-sources, canonical move-aside with unique temp stash (still renames live checkout and needs restore protocol), allowlist parameter on consumer side (name collision class stays open).

## AD-11
status: accepted
source: 2026-11-13-ci-gate-probe-hardening

Child decode in run_gate and check_release.py short-SHA call pinned encoding="utf-8", errors="replace" beside text=True. Child subprocess environment sets PYTHONIOENCODING="utf-8" so child stdout emits UTF-8 across all platforms. Never switch to raw bytes mode: text mode universal-newline translation preserved, so demo needles keep matching CRLF child output on Windows.

## AD-12
status: accepted
source: 2026-11-13-ci-gate-probe-hardening

Module docstring stays plain string, no raw prefix. sources\ becomes sources/ and backslash leaves docstring entirely. Section-marker and catalogue prose survive verbatim, so native triple-quote literals need no rewrite.
