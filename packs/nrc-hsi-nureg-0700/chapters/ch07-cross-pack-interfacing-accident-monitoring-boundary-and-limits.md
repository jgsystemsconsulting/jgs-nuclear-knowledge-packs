# Chapter 7: Cross-Pack Interfacing, Accident Monitoring Boundary, and Limits

Sources: NRC NUREG-0700 Revision 4, Human-System Interface Design Review Guidelines, January 2026, ML26022A094; pin verified via official NRC publication page on 2026-11-13. RG 1.97 accident monitoring criteria are owned by the live accident monitoring pack, named here, not a source.

## Core Idea

This chapter fixes where this pack stops and neighbour packs start, and records the stop lines orientation material carries. Accident monitoring variable criteria belong to the live accident monitoring pack while this pack covers how monitored information reaches the operator through the HSI. Digital I&C platform questions, cyber security program questions, and post-fire safe shutdown capability belong to their live neighbour packs by topic adjacency. The chapter also records the full not-covered list and the honest fallback sentence the pack gives when it cannot answer. No method is summarized and no design is judged here.

## Frameworks Introduced

- Accident monitoring boundary. The live accident monitoring pack carries the Regulatory Guide 1.97 variable selection and display criteria; this pack covers the HSI presentation and interaction design review of displays, alarms, and controls only, and does not restate variable criteria.
- Digital I&C neighbour line. Platform and system design review questions sit with the live digital I&C packs, named here in prose; this pack covers HSI presentation and interaction only.
- Cyber security neighbour line. Security program questions sit with the live cyber security pack by topic adjacency, named here in prose; no program control is packaged here.
- Fire protection neighbour line. Post-fire safe shutdown capability sits with the live fire protection pack, named here in prose; a remote or alternative shutdown station is a workplace concept here and a capability question there.
- Review frame hook. NUREG-0800 Standard Review Plan Chapter 18 frames staff HFE review and NUREG-0711 structures program-level review; both are named here only as frame, never summarized.

## Key Concepts

- Accident monitoring variable criteria: owned by the live accident monitoring pack; named here as boundary, no criterion restated.
- HSI presentation boundary: how monitored information reaches the operator through displays, alarms, and controls; this pack's side of the boundary, stated at orientation depth.
- Digital I&C platform questions: owned by the live digital I&C packs; named here as boundary, no platform method stated.
- Cyber security program questions: owned by the live cyber security pack by topic adjacency; named here as boundary, no program control stated.
- Post-fire safe shutdown: owned by the live fire protection pack; named here as boundary, no shutdown analysis stated.
- Human reliability and task analysis methods: named only if at all; no method summarized here.

## Mental Models

Read this chapter as the pack drawing its own border: each neighbour named, each owned question placed on the neighbour side, and this pack's HSI presentation slice kept on this side. Keep neighbours at naming depth: the pack states which pack owns which question and never carries the neighbour's criteria, method, or analysis. When candidate detail looks like a variable criterion, a platform method, a security control, a shutdown analysis, or an HFE program method, it belongs in the owning document or pack, not here.

## Anti-patterns

Restating any neighbour-owned criterion, method, or analysis is this chapter's named anti-pattern; boundaries ship, and no neighbour content does. A companion error treats naming a neighbour as summarizing it; neighbours ship as prose names only, with no text, criteria, or method carried. A third error treats this pack as a source for design or licensing decisions; the pack ships orientation with stop lines, and the guideline document itself plus licensed engineering personnel are the sources for real decisions. Numeric design values and guideline-level criteria are not packaged here.

## Key Takeaways

- The live accident monitoring pack owns variable criteria; this pack covers HSI presentation and interaction design review only.
- Digital I&C platform questions, cyber security program questions, and post-fire safe shutdown capability are neighbour-owned and named only.
- NUREG-0711, SRP Chapter 18, and human reliability or task analysis method documents are named only if at all, never summarized.
- Not covered: no HFE review or usability verdict for a named control room, alarm system, or workstation, no design recommendation, no legal or licensing advice.
- This knowledge pack provides high-level orientation on human-system interface design review guidelines under NUREG-0700 Revision 4; it does not reproduce guideline text, evaluate plant-specific designs, or provide human factors engineering advice. For guideline text, consult NUREG-0700; for plant-specific HFE licensing or review, consult licensed engineering personnel.
- The guideline document itself is the source for any design or review decision.

## Connects

- ch01 scope, purpose, and HFE review frame this chapter closes.
- ch02 basic HSI elements, displays and interactions presented through this pack's side of the boundary.
- ch03 control and automation systems including alarms and soft controls, systems on this pack's side of the boundary.
- ch04 computer-based procedures and communications, resources on this pack's side of the boundary.
- ch05 workstations, local control stations, and workplace design, where the fire protection boundary returns.
- ch06 maintainability, degraded HSI conditions, and integration, where the digital I&C boundary returns.
