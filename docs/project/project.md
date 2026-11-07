# Project

## goals
status: accepted
source: 2026-11-06-scaffold-todo-guard

Knowledge packs carry faithful, legally redistributable reference notes for one vetted source each, with provenance and licence terms on record before content ships.

## scope
status: accepted
source: 2026-11-06-scaffold-todo-guard

Scope covers pack scaffold tooling in tooling/build_pack.py, structural and licence validation in tooling/validate_pack.py, the release gate, and packs under packs/. Tier judgement stays a maintainer decision; tooling records and checks it but does not decide it.

## glossary
status: accepted
source: 2026-11-06-scaffold-todo-guard

scaffold: the PACK.yaml, LICENSE, and chapters skeleton build_pack.py writes for a new pack. TODO marker: an unfilled placeholder line left by the scaffold for the pack author. fail-closed: validation returns an error and exit 1 when a required fill is missing. content pack: a pack with PACK.yaml, LICENSE, SKILL.md, and chapters. signpost and orchestrator packs carry no LICENSE or chapters by design.
