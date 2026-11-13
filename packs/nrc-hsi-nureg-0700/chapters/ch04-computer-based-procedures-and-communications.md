# Chapter 4: Computer-Based Procedures and Communications

Sources: NRC NUREG-0700 Revision 4, Human-System Interface Design Review Guidelines, January 2026, ML26022A094; pin verified via official NRC publication page on 2026-11-13.

## Core Idea

Part II review treats computer-based procedure systems and HSI-supported communications as companion review topics. Procedure systems present procedures through the HSI and raise questions about presentation, tracking, branching, and fallback; communications covers how operators exchange information supported by the HSI. The chapter names the topic set only and carries no procedure text, product behavior, protocol, or criterion.

## Frameworks Introduced

- Computer-based procedures as orientation-depth review topic. Review asks how procedures are presented through the HSI; no procedure step or product behavior ships here.
- Step tracking and place-keeping as named concepts. Keeping the operator oriented in the procedure sequence is a review concern; no tracking design ships here.
- Branching and concurrent procedure handling as named concepts. Procedures that branch or run alongside others raise review questions; no handling design ships here.
- Paper-procedure fallback as named review concern. What operators use when the procedure system is unavailable stays a review question; no fallback design ships here.
- HSI-supported communications as companion review topic family. How the HSI supports operator communication is named as a review topic; no protocol or requirement ships here.

## Key Concepts

- Computer-based procedure: a procedure presented to operators through the HSI; named here as a review topic, with presentation, tracking, branching, and fallback as concerns and no step text stated.
- Step tracking: following operator progress through procedure steps; named here as a concept, with no design stated.
- Place-keeping: keeping operator position visible in the procedure; named here as a concept, with no design stated.
- Branching: procedure paths that diverge by plant condition or operator choice; named here as a concept, with no criterion stated.
- Paper-procedure fallback: use of paper procedures when the computer-based system is unavailable; named here as a review concern, with no fallback design stated.
- HSI-supported communications: operator communication carried or aided through the HSI; named here as a companion review topic family, with no protocol stated.

## Mental Models

Read procedure presentation as the reviewer checks it: can the operator see the procedure, follow the sequence, keep place, handle branches and concurrent procedures, and fall back when the system is unavailable. Read communications alongside: does the HSI support the exchange operators need. Keep both at topic level. When a candidate detail looks like a procedure step, a product behavior, a communication protocol, or a remembered criterion from a commercial standard or textbook, it belongs outside this pack, not under the NUREG-0700 label.

## Anti-patterns

Stating any procedure step, CBP product behavior, communication protocol, or remembered criterion from a commercial HSI standard or textbook under the NUREG-0700 label is this chapter's named anti-pattern; topics from the single named source ship, and no item-level content does. A companion error treats a concept definition as design instruction for a real procedure system; definitions state review topics for orientation, and no assessment of any plant procedure system follows. A third error imports a usability verdict on a real or hypothetical procedure installation; this pack assesses no plant procedure system and carries no finding. The guideline document itself is the source for any design or review decision.

## Key Takeaways

- Part II companion review covers computer-based procedures and HSI-supported communications as topic families.
- Procedure presentation, step tracking and place-keeping, branching and concurrent handling, and paper-procedure fallback are named review concerns.
- HSI-supported communications is named as a companion review topic family.
- No procedure step, product behavior, protocol, or outside criterion ships in this chapter, and no plant procedure system is assessed.
- The guideline document itself is the source for any design or review decision.

## Connects

- ch01 scope, purpose, and HFE review frame this chapter sits inside.
- ch02 basic HSI elements, the displays and interactions procedures present through.
- ch03 control and automation systems including alarms and soft controls, the companion Part II wholes.
- ch05 workstations and workplace design, where operators use procedures and communicate.
- ch06 maintainability, degraded HSI conditions, and integration, where procedures join the integrated crew whole.
