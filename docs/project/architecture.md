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
