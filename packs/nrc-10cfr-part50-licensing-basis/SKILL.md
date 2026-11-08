---
name: nrc-10cfr-part50-licensing-basis
description: "Orientation notes on the licensing-basis shape of 10 CFR Part 50, Domestic Licensing of Production and Utilization Facilities, synthesized from eCFR public-domain text (title 10 current as of 2026-11-05; pin-check 2026-11-08). Seven topics: Part 50 structure and key 50.2 definitions, 50.34 contents of applications including the safety analysis report, 50.36 technical specifications and their five categories, 50.54 conditions of licenses, 50.59 changes tests and experiments, Appendix A General Design Criteria as an index, and Appendix B as a pointer to the QA criteria body. SCOPE LIMITS: selected slices only, not all of 10 CFR Part 50; Appendix B is a pointer only, the criteria body belongs to the QA pack; Appendix A is an index, not an essay; not legal advice; not a plant-specific licensing basis; regulation text, not NRC staff guidance. LICENCE: Public Domain (US Government work, 17 U.S.C. 105)."
---

<!-- argument-hint: [Part 50 licensing question, section number, or chapter number] -->

# 10 CFR Part 50 licensing basis orientation

**Source**: 10 CFR Part 50, Domestic Licensing of Production and Utilization Facilities; eCFR public-domain text, title 10 current as of 2026-11-05; pin-check 2026-11-08. | **Licence**: Public Domain (US Government work, 17 U.S.C. 105) | **Chapters**: 7

## When to use
**Prerequisites:** basic regulatory vocabulary (licensee, license amendment, regulation versus guidance), and awareness that the plant licensing basis, not this pack, states what binds a given facility. Staff guidance material such as the Standard Review Plan and Regulatory Guides lives in `nrc-nuclear`.

Use this skill for orientation questions about the Part 50 licensing basis shape: what Part 50 regulates, what an application must contain, what technical specifications are, what conditions attach to licenses, when a licensee may make changes without an amendment, and how the appendices hook in. The pack answers with synthesized regulation notes, cited by chapter.

## How to Use This Skill

- **Without arguments**: read Core Frameworks, then the chapter index.
- **With a topic**: use the topic index, then open that chapter.
- **With a section number**: match it to a chapter in the index, then open that chapter file.

Supporting files: `glossary.md`, `cheatsheet.md`. There is no `patterns.md`.

## Core Frameworks & Mental Models

### Regulation versus guidance

Part 50 is regulation: it binds through the Atomic Energy Act and the license itself. Regulatory Guides and the Standard Review Plan are guidance: they describe one acceptable path and staff review expectations. This pack covers regulation text. It carries no staff positions and no staff guidance text; the guidance layer is `nrc-nuclear`.

### The licensing basis stack

One mental model orders the slices: an application describes the facility and its safety analysis (50.34); the issued license carries technical specifications derived from that analysis (50.36); the license sits under standing conditions (50.54); the licensee may make bounded changes without an amendment under 50.59; the principal design criteria hang on Appendix A; the quality program hangs on Appendix B. A question lands at one layer, and the chapter index maps layers to chapters.

### Pin rule

This pack pins eCFR title 10 current as of 2026-11-05, checked 2026-11-08. Later amendments are out of scope. The Federal Register amendments history, not this pack, tells which amendment text a given license incorporated at a given date.

### Not source and not advice

Notes are synthesized. They are not the regulation, not a licensing basis, and not counsel. Verbatim excerpts are capped at two sentences.

## Chapter Index

| Ch | File | Coverage | Cluster |
|----|------|----------|---------|
| 01 | [ch01-part50-overview-and-definitions](chapters/ch01-part50-overview-and-definitions.md) | Part 50 structure and key 50.2 definitions | Regulatory Framework & Staff Review |
| 02 | [ch02-50-34-contents-of-applications](chapters/ch02-50-34-contents-of-applications.md) | 50.34 contents of applications, PSAR and FSAR | Life Cycle & Requirements |
| 03 | [ch03-50-36-technical-specifications](chapters/ch03-50-36-technical-specifications.md) | 50.36 technical specifications | Life Cycle & Requirements |
| 04 | [ch04-50-54-conditions-of-licenses](chapters/ch04-50-54-conditions-of-licenses.md) | 50.54 conditions of licenses | Regulatory Framework & Staff Review |
| 05 | [ch05-50-59-changes-tests-experiments](chapters/ch05-50-59-changes-tests-experiments.md) | 50.59 changes, tests, experiments | Regulatory Framework & Staff Review |
| 06 | [ch06-appendix-a-gdc-overview](chapters/ch06-appendix-a-gdc-overview.md) | Appendix A General Design Criteria overview (index) | Regulatory Framework & Staff Review |
| 07 | [ch07-appendix-b-pointer](chapters/ch07-appendix-b-pointer.md) | Appendix B pointer to the QA criteria body | Regulatory Framework & Staff Review |

## Topic Index

- Part 50 structure and licensing classes, ch01
- Definitions (design bases, safety-related, RCPB, exclusion area, low population zone), ch01
- Contents of applications, PSAR and FSAR, ch02
- Technical specifications, safety limits, limiting conditions for operation, surveillance requirements, ch03
- Conditions of licenses, ch04
- Changes, tests, and experiments without an amendment, ch05
- Departure from a method of evaluation, ch05
- General Design Criteria groups, ch06
- Appendix B quality assurance pointer, ch07

## Supporting Files

- `glossary.md`
- `cheatsheet.md`

## Scope & Limits

This pack pins eCFR title 10 current as of 2026-11-05 (pin-check 2026-11-08). Later amendments are out of scope.

- Selected slices only: 50.2 (key definitions), 50.34, 50.36, 50.54, 50.59, Appendix A as an index, Appendix B as a pointer. This is not all of 10 CFR Part 50; sections outside the slices are out of scope.
- Appendix B is a pointer only. The criteria body belongs to the QA pack (theme C-02), not this pack.
- Appendix A is an index, not an essay: criteria titles and group structure only, no criterion bodies.
- No thin-pack handoffs: each slice this pack owns is owned fully; questions outside the slices are out of scope rather than half-covered.
- Regulation text only. NRC staff guidance (Regulatory Guides, the Standard Review Plan, BTPs) is `nrc-nuclear` material and carries no staff positions here.
- Not legal advice. Not a plant-specific licensing basis: a plant's actual licensing basis is the license, the technical specifications, and the FSAR as updated, not these notes. Sector anti-scope still applies: weapons and weapons-design physics, classified or export-controlled or safeguards-sensitive material, 10 CFR Part 35 and other non-power-plant isotope programmes, paywalled standard text.
