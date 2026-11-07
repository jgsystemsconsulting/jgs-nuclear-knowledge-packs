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
