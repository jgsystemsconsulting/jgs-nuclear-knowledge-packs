# Chapter 3: Control and Automation Systems, Alarms, and Soft Controls

Sources: NRC NUREG-0700 Revision 4, Human-System Interface Design Review Guidelines, January 2026, ML26022A094; pin verified via official NRC publication page on 2026-11-13.

## Core Idea

Part II review treats five HSI systems as wholes: alarm systems, the safety parameter display system concept, group-view displays, soft controls, and automation. Where Part I checks elements an operator reads and touches, this chapter names system-level review topics and the recurring concerns reviewers bring to each system. The chapter states concerns only and carries no scheme, list, layout, or design.

## Frameworks Introduced

- Alarm systems as processing and presentation review topic. Review asks whether alarms support operator detection and response without overload; alarm overload and prioritization are named review concerns, never design recipes. No setpoint, scheme, or list ships here.
- Safety parameter display system as HSI concept only. The chapter introduces SPDS as monitored safety information presented to the operator, and states no variable, content, or layout. The live RG 1.97 pack carries accident monitoring variable criteria; this pack states only how such information is presented and used through HSI, and does not restate variable criteria.
- Group-view and large-screen displays as shared awareness review idea. Review asks whether shared displays support crew situation awareness; no screen content or layout ships here.
- Soft controls as selection and confirmation review theme. Review asks whether soft control selection stays clear and actuation stays confirmable; no control design ships here.
- Automation as levels and modes review topic. Levels and modes are named concepts only, with operator awareness of automation state and manual takeover named review concerns; no automation design ships here.

## Key Concepts

- Alarm system: HSI system that alerts operators to off-normal conditions and supports detection and response; named here as a review topic, with overload and prioritization as concerns and no scheme stated.
- Safety parameter display system (SPDS): HSI concept presenting monitored safety information to operators; named here as a concept only, with variable selection owned by the live accident monitoring pack.
- Group-view display: shared display supporting crew awareness of plant state; named here as a review idea, with no content or layout stated.
- Soft control: operator control implemented through the interface rather than a dedicated device; named here with selection clarity and actuation confirmation as review themes and no design stated.
- Automation: system functions that act with limited operator input; named here with levels and modes as concepts, operator awareness of automation state as a concern, and manual takeover as a review concern, with no design stated.
- Mode awareness: operator understanding of what automation is doing and which mode is active; named here as a review concern, with no criterion stated.

## Mental Models

Read each system as a whole reviewer checks, not as parts to design. Alarms exist so operators detect and respond; review asks whether overload defeats that purpose. Shared displays exist so the crew holds one picture; review asks whether awareness holds. Soft controls exist so operators act through the interface; review asks whether selection and confirmation hold. Automation exists to carry functions; review asks whether the crew can tell what it is doing and take over manually. When a candidate detail looks like a setpoint, a scheme, a list, a layout, or a design, it belongs in the guideline document, not in this pack.

## Anti-patterns

Stating any alarm setpoint, prioritization scheme, SPDS variable list, screen layout, automation design, or guideline wording is this chapter's named anti-pattern; review concerns ship, and no item-level content does. A companion error treats SPDS variable selection as packaged here; variable criteria stay with the live accident monitoring pack, and this pack covers presentation and use only. A third error reads a commercial automation taxonomy or remembered HSI standard into NUREG-0700; levels and modes are named concepts only, and no outside scheme ships under the NUREG-0700 label. The guideline document itself is the source for any design or review decision.

## Key Takeaways

- Part II system-level review covers alarm systems, the SPDS concept, group-view displays, soft controls, and automation as wholes.
- Alarm overload and prioritization, shared crew awareness, soft control selection and confirmation, automation state awareness, and manual takeover are named review concerns, not design recipes.
- SPDS ships as an HSI concept only; accident monitoring variable criteria stay with the live accident monitoring pack.
- No setpoint, scheme, variable list, layout, automation design, or guideline wording ships in this chapter.
- The guideline document itself is the source for any design or review decision.

## Connects

- ch01 scope, purpose, and HFE review frame this chapter sits inside.
- ch02 basic HSI elements, the displays and interactions these systems are built from.
- ch04 computer-based procedures and communications, the companion Part II review topic.
- ch05 workstations and workplace design, where operators view these systems.
- ch06 maintainability, degraded HSI conditions, and integration, where these systems are checked as one crew whole.
- ch07 cross-pack interfacing and limits, where the accident monitoring boundary returns.
