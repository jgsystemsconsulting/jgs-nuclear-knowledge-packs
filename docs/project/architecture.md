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
