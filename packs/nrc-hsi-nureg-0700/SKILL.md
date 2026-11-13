---
name: nrc-hsi-nureg-0700
description: "Orientation notes on human-system interface design review guidelines, synthesized from NRC NUREG-0700 Revision 4, January 2026, ML26022A094 (full guideline body not captured; individual guideline items and numeric design values not reproduced; NUREG-0800 Chapter 18 and NUREG-0711 named relationship depth only). Seven topics: scope, purpose, and HFE review process; basic HSI elements and displays; control and automation systems including alarms and soft controls; computer-based procedures and communications; workstations and workplace design; maintainability, degraded HSI conditions, and integration; cross-pack interfacing, accident monitoring boundary, and limits. SCOPE LIMITS: orientation depth only; no guideline items or numeric values; not advice. LICENCE: Public Domain (US Government work, 17 U.S.C. 105)."
---

<!-- argument-hint: [HSI design review question, named chapter topic, or chapter number] -->

# NUREG-0700 Revision 4 human-system interface design review orientation

**Source**: NRC NUREG-0700 Revision 4, Human-System Interface Design Review Guidelines, January 2026, ML26022A094 (manuscript completed August 2025; authors O'Hara, Fleger, Hughes Green, Morrow); Gate 1 verification 2026-11-13; full guideline body not captured; NUREG-0800 Chapter 18 and NUREG-0711 named relationship depth only. | **Licence**: Public Domain (US Government work, 17 U.S.C. 105) | **Chapters**: 7

## When to use

**Prerequisites:** basic vocabulary of human factors engineering, control room operations, and NRC design review, plus awareness that the guideline document itself, not this pack, carries the review criteria a real HSI design is judged against.

Use this skill for orientation questions about how NRC HSI design review guidance hangs together: scope and purpose of the guidelines, the HFE review process they support, basic HSI elements and displays, control and automation systems including alarms and soft controls, computer-based procedures and communications, workstations and workplace design, maintainability and degraded HSI conditions, and where accident monitoring and neighbour packs sit. Pin-backed only.

Do not use it for guideline item text, numeric design values, plant-specific HSI verdicts, or neighbour-owned material (accident monitoring criteria, digital I&C platform design, cyber security program content, post-fire safe shutdown capability).

Supporting files: `glossary.md`, `cheatsheet.md`. There is no `patterns.md`.

## How to Use This Skill

1. Name the question class: foundation and pin, framework overview, one HSI topic (displays, controls and automation, procedures, communications, workstations, maintainability, degraded conditions), or neighbour boundary.
2. Open the matching chapter in the Chapter Index. Stay inside that chapter's slice.
3. If the question needs guideline item text, numeric design values, plant-specific HSI findings, or neighbour-owned method, stop at the pack boundary and state the thin class under Scope and Limits.
4. Never invent guideline numbers, display values, reach or viewing dimensions, lighting or acoustic values, alarm setpoints, or procedure wording. The full guideline body is not captured here.

## Core Frameworks & Mental Models

### Guidelines support review, they are not the design

NUREG-0700 gives reviewers criteria for judging whether a human-system interface supports safe operation. The guidelines describe what good review coverage looks like; they do not design any plant's control room, and nothing in this pack is a design finding.

### Review principles before guideline items

This pack works at the level of architectural categorization and review principles: which HSI topics exist, how they relate, and what a reviewer checks in each area. Individual guideline items and their numeric bases live in the guideline document and are never reproduced here.

### Pin rule

This pack pins NUREG-0700 Revision 4, January 2026, ML26022A094, verified via the official NRC publication page and ADAMS accession record on 2026-11-13. Manuscript completed August 2025. Authors: O'Hara, Fleger, Hughes Green, Morrow.

### Related guidance named only

NUREG-0800 Standard Review Plan Chapter 18 and NUREG-0711 appear here only as named related guidance showing where HSI review sits in the wider NRC review structure. Their text, criteria, and methods are not reproduced or summarized at any depth here.

### Not source and not advice

Notes are synthesized orientation notes keyed to the recorded pin and a closed statement set. This pack is not the guideline document, not NUREG-0711, not SRP Chapter 18, not regulation, and not counsel. This pack quotes nothing; verbatim excerpts are capped at two sentences by licence policy and this pack uses none.

## Chapter Index

| Ch | File | Coverage | Cluster |
|----|------|----------|---------|
| 01 | [ch01-nureg-0700-scope-purpose-and-hfe-review-process](chapters/ch01-nureg-0700-scope-purpose-and-hfe-review-process.md) | NUREG-0700 scope, purpose, and HFE review process; pin facts and pack map | Human Factors and HSI |
| 02 | [ch02-basic-hsi-elements-displays-and-interaction](chapters/ch02-basic-hsi-elements-displays-and-interaction.md) | Basic HSI elements, displays, and interaction | Human Factors and HSI |
| 03 | [ch03-control-and-automation-systems-alarms-and-soft-controls](chapters/ch03-control-and-automation-systems-alarms-and-soft-controls.md) | Control and automation systems including alarms and soft controls | Human Factors and HSI |
| 04 | [ch04-computer-based-procedures-and-communications](chapters/ch04-computer-based-procedures-and-communications.md) | Computer-based procedures and communications | Human Factors and HSI |
| 05 | [ch05-workstations-local-control-stations-and-workplace-design](chapters/ch05-workstations-local-control-stations-and-workplace-design.md) | Workstations, local control stations, and workplace design | Human Factors and HSI |
| 06 | [ch06-maintainability-degraded-hsi-conditions-and-integration](chapters/ch06-maintainability-degraded-hsi-conditions-and-integration.md) | Maintainability, degraded HSI conditions, and integration | Human Factors and HSI |
| 07 | [ch07-cross-pack-interfacing-accident-monitoring-boundary-and-limits](chapters/ch07-cross-pack-interfacing-accident-monitoring-boundary-and-limits.md) | Cross-pack interfacing, accident monitoring boundary, and limits | Human Factors and HSI |

## Topic Index

- NUREG-0700 scope, HFE review process, and pack map, ch01
- Guideline architecture across HSI topics, ch01 and ch07
- Basic HSI elements, display design review principles, ch02
- Controls, automation, alarm philosophy, and soft control concepts, ch03
- Computer-based procedures and communication systems, ch04
- Workstations, local control stations, and workplace design, ch05
- Maintainability, degraded HSI conditions, and integration, ch06
- Accident monitoring presentation boundary; live neighbour packs in prose, ch07
- Honest fallback when guideline text, plant analysis, or neighbour method is required, ch07

## Supporting Files

- `glossary.md`
- `cheatsheet.md`

## File Structure

Pack root holds `PACK.yaml` (identity and pin), `LICENSE` (content licence), and `SKILL.md` (this index). Chapters live in `chapters/` as `ch01` through `ch07` files listed above. Cluster for all chapters is Human Factors and HSI. Supporting files are `glossary.md` and `cheatsheet.md`; there is no `patterns.md`.

## Scope & Limits

HSI design review orientation per NUREG-0700 Revision 4 pin facts. This pack is not the guideline document, not NUREG-0711, and not SRP Chapter 18.

- Guideline architecture and review principles at orientation depth only. No guideline items, item numbers, anthropometric tables, or numeric display, reach, viewing, lighting, or acoustic values are packaged here.
- Accident monitoring variable criteria (RG 1.97) belong to the live accident monitoring pack; this pack covers presentation and interaction design review only, and names that neighbour in prose.
- Digital I&C platform design, cyber security program content, and post-fire safe shutdown capability are neighbour-owned and named only. No platform method, program control, or shutdown analysis is packaged here.
- Not HFE review, not usability evaluation, and not control room design instruction for any real plant. No design finding, alarm scheme, procedure text, or layout is produced here.
- Zero quotations. Synthesized notes keyed to the recorded pin (Revision 4, January 2026, ML26022A094); verbatim excerpts capped at two sentences by licence policy and this pack uses none. No source-material URLs in pack files.
- Not legal, licensing, HFE review, or design advice. Advice requests are refused.
- Three question classes are thin in this pack and stop at the pack boundary: (1) guideline level (guideline item text, item numbers, figures, tables, or any numeric design value); (2) plant or design specific (HSI verdicts for a named design, control room evaluation, staffing or workload analysis, procedure or alarm design for a real plant); (3) neighbour-owned material (accident monitoring criteria, digital I&C design questions, cyber security controls, fire protection or safe shutdown analysis, HFE program review method).
- Honest fallback: when the question needs guideline body text, plant-specific analysis, or neighbour-owned method, stop and name the guideline document itself (NRC NUREG-0700 Revision 4) or the owning neighbour as the text source; this pack does not invent missing content.
- No slug links to any sibling pack. Neighbours are named in prose only, per repo discipline.
- Sector anti-scope still applies: weapons and weapons-design physics, classified or export-controlled or safeguards-sensitive material, 10 CFR Part 35 and other non-power-plant isotope programmes, paywalled standard text.
