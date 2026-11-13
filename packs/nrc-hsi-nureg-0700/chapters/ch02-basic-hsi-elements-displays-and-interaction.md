# Chapter 2: Basic HSI Elements, Displays, and Interaction

Sources: NRC NUREG-0700 Revision 4, Human-System Interface Design Review Guidelines, January 2026, ML26022A094; pin verified via official NRC publication page on 2026-11-13.

## Core Idea

Element-level review covers the smallest review objects an operator reads and touches: how information is displayed, how the operator interacts with and manages the interface, and how analog and conventional devices present where they remain. This chapter names the Part I topic families, defines five concepts as design intent only, and states the review themes at principle level.

## Frameworks Introduced

- Three element families. Part I review groups element-level checks into information display, user-interface interaction and management, and analog and conventional devices. Families are topic sets, not checklists; one operator action can touch all three.
- Display as read intent. An information display exists so the operator can perceive plant state and understand what it means for the task at hand; review asks whether that read is supported, and states no display criterion here.
- Interaction as managed exchange. The operator selects, enters, navigates, and confirms; the interface gives feedback and tolerates error; review asks whether the exchange stays consistent and recoverable, and states no interaction criterion here.
- Analog and conventional devices as continuing topic. Where meters, lamps, switches, and recorders remain in service, their presentation and use stay inside review; this pack names the family and states no device criterion.

## Key Concepts

- Information display: the family of presented indications through which plant state reaches the operator; defined here as design intent that displayed information be perceptible and understandable, with no display criterion stated.
- User-interface interaction and management: the family of selections, entries, navigation moves, and interface-management actions through which the operator works; defined here as design intent that interaction stay consistent and give feedback, with no interaction criterion stated.
- Analog and conventional devices: meters, lamps, switches, recorders, and similar hardwired elements where still installed; named as a topic family, with no device criterion stated.
- Display element: one presented item the operator reads; this pack defines the term only, and states no wording, size, or coding criterion for any element.
- Navigation: moving attention and selection across displays and interface pages to reach the needed item; this pack defines the term as design intent only.
- Feedback: the interface response that tells the operator an action was received and what changed; this pack defines the term as design intent only.
- Data entry: the operator act of supplying values, selections, or commands to the system; this pack defines the term as design intent only.
- Error tolerance: the interface property of resisting mistaken action and letting the operator detect and recover; this pack defines the term as design intent only.

## Mental Models

Read each element as one link in a perceive, act, and confirm loop: the display shows state the operator can read, the interaction lets the operator act and move, feedback closes the loop, and error tolerance keeps a slip recoverable. Keep review themes at principle level: information perceptible and understandable, interaction consistent with feedback, interface resists and tolerates operator error. When a candidate detail looks like a number, a size, a time, or a colour rule, it belongs to the guideline document, not to this pack.

## Anti-patterns

Stating any individual guideline wording, guideline number, or criterion as read from the guideline set is this chapter's named anti-pattern; topic families and concept definitions ship, and no item-level content does. A companion error ships a numeric design value of any kind: character or symbol size, response-time value, colour or coding criterion, or any table or figure reference. A third error treats a concept definition as design instruction for a real display or control; definitions here state design intent for orientation, and no design recommendation for any real or hypothetical installation follows. Numeric design values and guideline-level criteria are not packaged here; the guideline document itself is the source for any design or review decision.

## Key Takeaways

- Part I element-level review covers information display, user-interface interaction and management, and analog and conventional devices as topic families.
- Display element, navigation, feedback, data entry, and error tolerance are defined here as design intent only.
- Review themes stay at principle level: information perceptible and understandable, interaction consistent with feedback, interface resists and tolerates operator error.
- No individual guideline wording or number and no numeric design value ships in this chapter.
- The guideline document itself is the source for any design or review decision.

## Connects

- ch01 scope, purpose, and the HFE review frame this chapter sits inside.
- ch03 control and automation systems including alarms and soft controls, the system-level wholes built from these elements.
- ch04 computer-based procedures and communications, which present through these elements.
- ch05 workstations and workplace design, where these elements are arranged and viewed.
- ch06 maintainability and degraded HSI conditions, which change what these elements show.
