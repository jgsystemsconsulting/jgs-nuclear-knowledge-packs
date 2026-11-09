# Chapter 5: Cyber security versus SDOE contrast

Sources: NRC RG 5.71 Rev. 1, Cyber Security Programs for Nuclear Power Reactors, February 2023, ML22258A204; pin 2026-11-08 (P9 VERIFY cleared); carried nrc-nuclear SDOE-fence facts from its ch01, ch02, and ch09.

## Core Idea

Two guidance lines sit next to each other and do different jobs. RG 1.152 Rev 4 (July 2023, ML23054A463) covers PDD criteria and SDOE, and RG 1.152 does not address control-of-access features meant to stop malicious cyberattacks; that topic sits under 10 CFR 73.54 and the separate cybersecurity regulatory guide the RG names. Malicious cyberattack programs sit under a different regulation and guide. The nrc-nuclear pack carries RG 1.152 criteria and SDOE; malicious-cyberattack protection sits here, under 10 CFR 73.54 and RG 5.71.

## Frameworks Introduced

- The SDOE fence. SDOE work under RG 1.152 covers the secure development and operating environment side; the malicious-cyberattack side is 73.54 and RG 5.71 territory. Each question belongs to one side of the fence.
- The pointer history. RG 5.71 stayed a cyber-security pointer in nrc-nuclear, not a chapter; this pack carries the other side of that fence as its own body.

## Key Concepts

- RG 1.152 Rev 4 (July 2023, ML23054A463): covers PDD criteria and SDOE; its SDOE body lives in the live nrc-nuclear pack, named here in prose only.
- Control-of-access features meant to stop malicious cyberattacks: outside RG 1.152's coverage; the topic sits under 10 CFR 73.54 and the separate cybersecurity regulatory guide the RG names.
- Security families in nrc-nuclear: they name 73.54 plus RG 5.71 for malicious cyber-attack protection; RG 1.152 and RG 5.71 are adjacent only where the source points.
- Side-of-the-fence test: a question about the development environment and non-malicious access control is SDOE; a question about protection from cyber attacks is this pack's side.

## Mental Models

Sort questions by which side of the fence they land on before choosing a source: development-environment and non-malicious access questions belong to RG 1.152's SDOE side, carried in the live nrc-nuclear pack, and cyber-attack protection questions belong here. The two lines are adjacent only where the source points; adjacency is not coverage.

## Anti-patterns

Collapsing the fence is the chapter's named anti-pattern: treating SDOE guidance as cyber-attack coverage, or this pack as an SDOE or RG 1.152 body. This pack implies no RG 1.152 content; the SDOE side stays in the live nrc-nuclear pack, and its facts here are limited to the fence statements.

## Key Takeaways

- RG 1.152 Rev 4 covers PDD criteria and SDOE and does not address control-of-access features meant to stop malicious cyberattacks.
- Malicious cyberattack programs sit under a different regulation and guide: 10 CFR 73.54 and RG 5.71.
- RG 5.71 stayed a cyber-security pointer in nrc-nuclear, not a chapter; this pack carries the other side.
- The nrc-nuclear security families name 73.54 plus RG 5.71 for malicious cyber-attack protection; RG 1.152 and RG 5.71 are adjacent only where the source points.

## Connects To

- ch01 for the guide character on this side of the fence.
- ch02 for the regulation that owns the malicious-cyberattack side.
- ch07 for how the Part 73 frame neighbours this material.
