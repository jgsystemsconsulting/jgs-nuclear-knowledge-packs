---
name: nrc-btp-7-18-plc
description: "Orientation notes for programmable logic controllers in digital safety instrumentation and control, pinned to NUREG-0800 Branch Technical Position 7-18 Rev. 6, August 2016, ML16019A327, listing-page title Guidance on the Use of Programmable Logic Controllers in Digital Computer-Based Instrumentation and Control Systems. Eight sketch topics: PLC role in safety I&C, software versus firmware boundary, life-cycle expectations versus BTP 7-14, commercial dedication touchpoints, failure modes as a staff-eye question, documentation set, pack-use anti-patterns, and pointers to RG 1.152 and Appendix 7.1-D. SCOPE LIMITS: not the BTP 7-14 body, not BTP 7-19, not IEEE or IEC text, not legal advice, not a later revision, PDF body not captured. LICENCE: Public Domain (US Government work, 17 U.S.C. 105)."
---

<!-- argument-hint: [PLC question, BTP 7-18 topic, or chapter number] -->

# NUREG-0800 BTP 7-18 PLC orientation

**Source**: U.S. Nuclear Regulatory Commission, NUREG-0800 Branch Technical Position 7-18, Rev. 6, August 2016 (ML16019A327); listing-page pin 2026-11-07. PDF body was not captured. | **Licence**: Public Domain (US Government work, 17 U.S.C. 105) | **Chapters**: 8

## When to use
**Prerequisites:** basic I&C vocabulary (PLC, firmware, safety system), and the fact that the plant licensing basis, not this pack, decides which revision binds. Software life-cycle method detail lives in `nrc-nuclear`.

Use this skill for orientation questions about programmable logic controllers in digital safety instrumentation and control: which chapter owns the question, which questions are thin here and belong in `nrc-nuclear`, and which pack rules keep notes from being treated as the BTP.

## How to Use This Skill

- **Without arguments**: read Core Frameworks, then the chapter index.
- **With a topic**: use the topic index, then open that chapter.
- **With a chapter number**: open that chapter file.

Supporting files: `glossary.md`, `cheatsheet.md`. There is no `patterns.md`.

## Core Frameworks & Mental Models

### Edition rule

This pack pins Rev. 6, August 2016, ML16019A327. Later agency actions are out of scope. The plant licensing basis, not this pack, decides which revision binds a given plant.

### Name-only rule

IEEE and IEC standards are designation and edition only. IEEE Std 603 and IEEE Std 7-4.3.2 are named, not quoted. Their text is not in this pack.

### Split labour

This pack orients PLC questions. `nrc-nuclear` holds the BTP 7-14 software-review method, RG 1.152 criteria, and Appendix 7.1-D.

### Not source and not advice

Notes are synthesized. They are not the BTP, not a licensing basis, and not counsel.

## Chapter Index

| Ch | File | Coverage | Cluster |
|----|------|----------|---------|
| 01 | [ch01-plc-role-in-safety-ic](chapters/ch01-plc-role-in-safety-ic.md) | PLC role in safety I&C | Regulatory Framework & Staff Review |
| 02 | [ch02-software-vs-firmware-boundary](chapters/ch02-software-vs-firmware-boundary.md) | software versus firmware boundary | Life Cycle & Requirements |
| 03 | [ch03-life-cycle-vs-btp-7-14](chapters/ch03-life-cycle-vs-btp-7-14.md) | life-cycle expectations versus BTP 7-14 | Life Cycle & Requirements |
| 04 | [ch04-commercial-dedication-touchpoints](chapters/ch04-commercial-dedication-touchpoints.md) | commercial dedication touchpoints | Regulatory Framework & Staff Review |
| 05 | [ch05-failure-modes-staff-eye](chapters/ch05-failure-modes-staff-eye.md) | failure modes as a staff-eye question | Regulatory Framework & Staff Review |
| 06 | [ch06-documentation-set](chapters/ch06-documentation-set.md) | documentation set | Life Cycle & Requirements |
| 07 | [ch07-anti-patterns](chapters/ch07-anti-patterns.md) | pack-use anti-patterns | Regulatory Framework & Staff Review |
| 08 | [ch08-rg-1-152-and-app-7-1-d](chapters/ch08-rg-1-152-and-app-7-1-d.md) | pointers to RG 1.152 and Appendix 7.1-D | Regulatory Framework & Staff Review |

## Topic Index

- PLC role in safety I&C, ch01
- Software versus firmware, ch02
- Life cycle versus BTP 7-14, ch03
- Commercial dedication question, ch04
- Failure-mode question, ch05
- Documentation-set question, ch06
- Pack-use anti-patterns, ch07
- RG 1.152 and Appendix 7.1-D handoff, ch08

## Supporting Files

- `glossary.md`
- `cheatsheet.md`

## Scope & Limits

This pack pins Rev. 6, August 2016, ML16019A327. Later revisions are out of scope.

- BTP 7-14 software life-cycle method, plan acceptance, and design-output scoring: thin here, use `nrc-nuclear` ch02 and ch07.
- RG 1.152 criteria and secure development and operational environment: thin here, use `nrc-nuclear` ch09.
- Appendix 7.1-D evaluation of IEEE Std 7-4.3.2: thin here, use `nrc-nuclear` ch10.

BTP 7-19 is not this pack. Sector anti-scope still applies: weapons and weapons-design physics, classified or export-controlled or safeguards-sensitive material, 10 CFR Part 35 and other non-power-plant isotope programmes, paywalled standard text. No legal or licensing advice. PDF body was not captured. IEEE and IEC text is not in this pack.
