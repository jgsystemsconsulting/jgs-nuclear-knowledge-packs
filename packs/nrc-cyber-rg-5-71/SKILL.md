---
name: nrc-cyber-rg-5-71
description: "Orientation notes on civil-plant cyber security programs, synthesized from NRC Regulatory Guide 5.71 Rev. 1, February 2023, ML22258A204, and 10 CFR 73.54 public eCFR slices. Seven topics: the role and scope of RG 5.71, the 10 CFR 73.54 regulation at orientation level, the graded defense-in-depth program shape, defensive architecture and mutually reinforcing layers, the cyber security versus SDOE contrast with the live nrc-nuclear pack, program lifecycle and periodic review, and the Part 73 shape and staff review framing. SCOPE LIMITS: orientation only; no security-control implementation guidance; no threat-actor or tactic detail; no DBT references; G-02 and G-03 named only, never linked; not legal advice; not a plant-specific cyber security program. LICENCE: Public Domain (US Government work, 17 U.S.C. 105)."
---

<!-- argument-hint: [cyber security program question, regulation section, or chapter number] -->

# RG 5.71 Rev. 1 cyber security program orientation

**Source**: NRC RG 5.71 Rev. 1, February 2023, ML22258A204; P9 listing-page pin 2026-11-08; 10 CFR 73.54 eCFR pin-check 2026-11-09. | **Licence**: Public Domain (US Government work, 17 U.S.C. 105) | **Chapters**: 7

## When to use

**Prerequisites:** basic regulatory vocabulary (regulatory guide, licensee, cyber security program) and awareness that the guide and the regulation, not this pack, carry the requirement text and the method detail a real program reads against.

Use this skill for orientation questions about civil-plant cyber security programs: what RG 5.71 Rev. 1 covers, what 10 CFR 73.54 requires at orientation level, the graded defense-in-depth program shape, the defensive architecture frame, which side of the SDOE fence a question belongs to, the program lifecycle, and the Part 73 staff-review framing. The pack answers with synthesized, pin-backed orientation notes, cited by chapter.

## How to Use This Skill

- **Without arguments**: read Core Frameworks, then the chapter index.
- **With a topic**: use the topic index, then open that chapter.
- **With a regulation section or chapter number**: match it to a chapter in the index, then open that chapter file.

Supporting files: `glossary.md`, `cheatsheet.md`. There is no `patterns.md`.

## Core Frameworks & Mental Models

### Graded, defense-in-depth program

The cyber security program RG 5.71 describes is graded and uses a defense-in-depth approach: defensive layers and controls that reinforce one another across the systems and networks 10 CFR 73.54 covers. Its lifecycle elements run from establishing and implementing the program through monitoring, sustaining, and reassessing it over the plant life. Controls are named as categories only in this pack; no product, configuration, detection-logic, or tuning guidance appears anywhere in it.

### Two sides of the SDOE fence

RG 1.152 Rev 4 covers PDD criteria and SDOE and does not address control-of-access features meant to stop malicious cyberattacks; that topic sits under 10 CFR 73.54 and the separate cybersecurity regulatory guide the RG names. The nrc-nuclear pack carries RG 1.152 criteria and SDOE; malicious-cyberattack protection sits here, under 10 CFR 73.54 and RG 5.71. Sort each question by which side of the fence it lands on.

### Pin rule

This pack pins RG 5.71 Rev. 1, February 2023, accession ML22258A204, pin date 2026-11-08 (P9 VERIFY cleared: Rev 1 is current; Rev 0, January 2010, carried ML090340159), and 10 CFR 73.54 eCFR pin-check 2026-11-09 (title 10 latest amendment 2026-11-03; section unchanged since 2017-01-01). Later revisions of the guide are out of scope. The guide and regulation texts, not this pack, state the method detail and the requirements themselves.

### Not source and not advice

Notes are synthesized. They are not the guide, not the regulation, and not counsel. This pack quotes nothing; verbatim from eCFR text is capped at two sentences by licence policy. G-02 and G-03 are named only as idea-stage neighbours, never linked, and their text is never reproduced here. Program specifics for any named site are beyond public text and beyond this pack.

## Chapter Index

| Ch | File | Coverage | Cluster |
|----|------|----------|---------|
| 01 | [ch01-rg-5-71-role-and-scope](chapters/ch01-rg-5-71-role-and-scope.md) | RG 5.71 role and scope | Cyber Security Programs |
| 02 | [ch02-10-cfr-73-54-the-regulation](chapters/ch02-10-cfr-73-54-the-regulation.md) | 10 CFR 73.54, the regulation | Cyber Security Programs |
| 03 | [ch03-cyber-security-program-shape](chapters/ch03-cyber-security-program-shape.md) | Cyber security program shape | Cyber Security Programs |
| 04 | [ch04-defensive-architecture-and-defense-in-depth](chapters/ch04-defensive-architecture-and-defense-in-depth.md) | Defensive architecture and defense in depth | Cyber Security Programs |
| 05 | [ch05-cyber-security-versus-sdoe-contrast](chapters/ch05-cyber-security-versus-sdoe-contrast.md) | Cyber security versus SDOE contrast | Cyber Security Programs |
| 06 | [ch06-program-lifecycle-and-periodic-review](chapters/ch06-program-lifecycle-and-periodic-review.md) | Program lifecycle and periodic review | Cyber Security Programs |
| 07 | [ch07-the-part-73-shape-and-staff-review](chapters/ch07-the-part-73-shape-and-staff-review.md) | The Part 73 shape and staff review | Regulatory Framework & Staff Review |

## Topic Index

- Role of RG 5.71 Rev. 1 and its scope: cyber security programs for nuclear power reactors, the pin, the revision history, ch01
- The guide character: a method NRC staff consider acceptable, not a substitute for the regulation, ch01 and ch07
- What 10 CFR 73.54 requires: protection of digital computer and communication systems and networks associated with safety-related and important-to-safety functions, ch02
- The eCFR pin facts for 73.54 and the named-out boundary on site program specifics, ch02
- The graded, defense-in-depth program shape and controls named as categories only, ch03
- The defensive architecture of mutually reinforcing layers and controls across the covered systems and networks, ch04
- The SDOE fence: RG 1.152 Rev 4 coverage and where malicious-cyberattack protection sits, ch05
- Side-of-the-fence sorting for development-environment versus cyber-attack questions, ch05
- The program lifecycle: establish, implement, monitor, sustain, reassess over the plant life, ch06
- Change and emerging-threat handling as lifecycle concerns without tactic detail, ch06
- Documentation and NRC staff review at framework level, and the Part 73 neighbour topics, ch07

## Supporting Files

- `glossary.md`
- `cheatsheet.md`

## Scope & Limits

This pack pins RG 5.71 Rev. 1, February 2023, ML22258A204, pin date 2026-11-08, and 10 CFR 73.54 eCFR pin-check 2026-11-09 (title 10 latest amendment 2026-11-03; section unchanged since 2017-01-01). Later revisions of the guide are out of scope.

- No classified DBT details.
- No weapons content.
- No export-controlled or safeguards-sensitive content beyond public civil NRC text.
- No force-on-force tactics beyond public RG and regulation text.
- No security-control implementation guidance: controls are named as categories only, never products, configurations, detection logic, or tuning.
- Not legal advice.
- Not a plant-specific cyber security program.
- G-02 and G-03 are named only, idea stage, no slugs, nothing packaged from them.
- The nrc-nuclear pack is named in prose as the live SDOE pack for the contrast; no forward slug links to any pack appear in this pack.
- Sector anti-scope still applies: weapons and weapons-design physics, classified or export-controlled or safeguards-sensitive material, and paywalled standard text.
