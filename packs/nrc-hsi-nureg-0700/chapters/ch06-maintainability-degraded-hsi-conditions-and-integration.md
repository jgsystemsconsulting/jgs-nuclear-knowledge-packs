# Chapter 6: Maintainability, Degraded HSI Conditions, and Integration

Sources: NRC NUREG-0700 Revision 4, Human-System Interface Design Review Guidelines, January 2026, ML26022A094; pin verified via official NRC publication page on 2026-11-13.

## Core Idea

Further design topics review covers keeping digital HSI testable and maintainable, recognizing and riding through degraded I&C and HSI conditions, and checking HSI resources as an integrated whole for crew tasks. Where earlier chapters check elements and systems one by one, this chapter names the review concerns that appear only when test, degradation, and crew use are considered together. The chapter states concerns only and carries no maintenance procedure, failure analysis, backup design, or plant response assessment.

## Frameworks Introduced

- Maintainability of digital systems review topic family. Review asks whether test and maintenance interfaces, bypass awareness, and out-of-service awareness are addressed as concepts; no maintenance task is written and no test procedure ships here.
- Degraded I&C and HSI conditions review topic family. Detecting degradation and falling back safely are named review concerns; no failure mode is analysed and no plant degradation response is assessed here.
- HSI resource integration review topic. Alarms, displays, controls, procedures, automation, and workplace are checked as an integrated whole supporting crew tasks, not only element by element. Integration is the review question of whether the parts work together for the crew, and no integration design ships here.
- Digital I&C neighbour line. Platform and system design review questions behind degradation and maintainability belong to the live digital I&C packs, named here in prose; this chapter covers HSI review concerns only.

## Key Concepts

- Maintainability (digital systems): review topic covering whether digital HSI supports test and maintenance awareness; named here as review topic, no task or procedure stated.
- Test and maintenance interfaces: interfaces supporting test and maintenance work; named here as concept, no design stated.
- Bypass awareness: operator awareness of bypassed functions as review concept; named concept, no scheme stated.
- Out-of-service awareness: operator awareness of out-of-service equipment as review concept; named concept, no list stated.
- Degraded HSI conditions: conditions where I&C or HSI capability is reduced; named here as review topic, no failure mode analysed.
- Falling back safely: safe fallback under degradation as review concern; named concern, no response assessed.
- HSI integration: checking alarms, displays, controls, procedures, automation, and workplace as an integrated whole for crew tasks; named here as review topic, no design stated.

## Mental Models

Read this chapter as the reviewer stepping back: test interfaces named so maintenance awareness can be checked, degradation named so detection and safe fallback can be checked, and the whole HSI named so crew task support can be checked across elements. Keep each concern at topic level: review asks whether maintainability, degradation response, and integration are addressed, without stating any procedure, analysis, or design the pack could answer from. When candidate detail looks like a maintenance task, a failure analysis, a backup design, or a plant degradation response, it belongs in the guideline document or the owning neighbour pack, not in this pack.

## Anti-patterns

Writing any maintenance task, test procedure, failure mode analysis, backup design, or plant degradation response is this chapter's named anti-pattern; concerns ship, and no task, analysis, or design does. A companion error treats integration as naming a system design; integration ships as the review question of parts working together for crew tasks, and no integration design is produced here. A third error treats degradation as naming a plant response verdict; degradation ships as detection and safe fallback review concerns, and no plant response is assessed here. Numeric design values and guideline-level criteria are not packaged here; the guideline document itself is the source for any design or review decision.

## Key Takeaways

- Further topics review covers maintainability of digital systems, degraded I&C and HSI conditions, and HSI resource integration.
- Test and maintenance interfaces, bypass awareness, and out-of-service awareness ship as maintainability concepts; no maintenance task is written.
- Detecting degradation and falling back safely ship as review concerns; no failure mode is analysed and no plant response is assessed.
- Alarms, displays, controls, procedures, automation, and workplace are checked as an integrated whole for crew tasks, not only element by element.
- The guideline document itself is the source for any design or review decision.

## Connects

- ch01 scope, purpose, and HFE review frame this chapter sits inside.
- ch02 basic HSI elements, displays and interactions checked as part of the integrated whole.
- ch03 control and automation systems including alarms and soft controls, systems joining the integrated whole.
- ch04 computer-based procedures and communications, resources joining the integrated whole.
- ch05 workstations, local control stations, and workplace design, the workplace joining the integrated whole.
- ch07 cross-pack interfacing and limits, where neighbour boundaries return.
