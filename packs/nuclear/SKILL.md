---
name: nuclear
kind: orchestrator
disable-model-invocation: true
description: "Orchestrator (not a knowledge pack): routes a free-text Nuclear question to the right catalogue pack(s), reads them with you, and answers with pack and chapter citations. Runs only on explicit `/nuclear <question>`; carries no source content. Use when you do not know which `/pack` to ask."
---

<!-- argument-hint: [free-text Nuclear question] -->

# Nuclear Orchestrator: routes questions to the right knowledge packs

**This is an orchestrator, not a knowledge pack.** It carries **no source content**.
On explicit `/nuclear <question>` it matches your question to installed catalogue packs,
reads them, and answers with pack and chapter citations.

## When to use
**Prerequisites:** none: plain Markdown; works on any host that loads Agent Skills. Pair it with the packs it routes to.

`/nuclear` answers Nuclear questions by consulting installed packs. It is an
entry point, not a knowledge base. Use it when you do not already know which `/<slug>`
to open.

## How /nuclear answers

### Modes

| Mode | When | Gate |
|---|---|---|
| Narrow consult | One Topics row matches, at most one agency named, no compare/contrast/survey verb | None. Best single pack. End with "Also relevant" runners-up. |
| Broad consult | Two or more Topics rows, two or more agencies, or a compare/contrast/survey verb | One plan approval naming packs and why, then run to done. Disagreements under "Where the sources differ"; never average or blend. |
| Deliverable | An artifact verb (draft, write, produce, prepare, build, review, verify) plus a Deliverables row name or keyword | Plan approval, then stage pauses after Draft and after Review (Verify is last). |

### Routing

1. Match Topics keywords case-insensitively, with synonym judgement.
2. Agency filter: when the question names agencies, keep candidates listed on those Agency contexts rows as long as one survives; otherwise keep all candidates and say no pack from that agency covers the topic.
3. Narrow pick: first-listed pack of the matched row after the filter; if that pack's Scope & Limits flags the question thin, take the next on the row. The consult stays narrow (no gate).
4. Broad pick: best-positioned candidate per named agency, then first-listed of each matched row, then second-listed, stopping at four, or earlier once every matched row and agency is represented and at least two packs are chosen.
5. No match: name the three closest Topics rows, suggest a rephrase or a direct `/<slug>`, and make **no Nuclear claims**.

### Reading

A pack lives at `../<slug>/` from this folder (native installs put members side by side). For each selected pack: read its `SKILL.md` index; open at most two chapters from its Topic Index / Chapter Index; open one support file (`glossary.md`, `patterns.md`, or `cheatsheet.md`) only for term, technique, or decision-rule questions. At most four packs total. If no chapter covers the question, record "no chapter in `slug` covers this" and use the index frameworks where they apply.

Each pack brief returns at most 10 claims of at most two sentences, each with a citation, plus a `thin:` line when Scope & Limits flags the question and a `source:` line copied from the pack's `**Source**` line. No claim from outside its pack.

### Citations and Sources

Cite only files read this session, in these forms: `[slug chNN]`, `[slug index]`,
`[slug glossary|patterns|cheatsheet]`. Drop uncited claims. Agreeing claims merge into one statement carrying every citation. Where the packs are silent, say so; no fallback to model memory. Every answer ends with a **Sources** block listing each pack's slug, its `**Source**` line, and its licence. Content-pack licences come from the Licences table, else the label `Public Domain (US Government work)`. Signpost lines read `MIT (signpost)`. Non-commercial and share-alike terms appear in full.

### Deliverable stage chains

The matched Deliverables row is the chain. Draft / Review / Verify cells list the packs for each stage; an empty cell skips that stage (the plan says so). A review or verify request on a user-supplied artifact starts the chain at that stage.

- **Draft** builds the artifact from the Draft packs' guidance with inline citations, then pauses.
- **Review** lists cited findings against the Review packs' criteria and gives the revised artifact, then pauses.
- **Verify** reports a table of item, criterion, result, and citation, plus open items. It edits nothing and offers fixes as a follow-up.

Output goes in the reply unless the user names a file. A deliverable with no matching Deliverables row gets **no improvised chain**: name the closest Deliverables rows or offer a broad consult instead.

### Edge cases

- Bare `/nuclear` with no argument: print usage and three example questions drawn from the Topics rows.
- Sub-agent failure: rerun that brief in the main thread.
- Thin-pack step-down: if the selected pack's Scope & Limits flags the question thin, take the next pack on the row; the consult stays narrow.
- IEEE, IEC, or IAEA lookup: answer from [nrc-nuclear ch08] with designation and edition only, and state that the standard text is outside the packs.

## Routing map

<!-- ROUTING-MAP:BEGIN -->
### Topics
| Topic | Keywords | Packs (best first) |
|---|---|---|
| Software verification & validation | software V&V, verification and validation, independent V&V, IV&V, V&V plan, SVVP, V&V tasks, integrity level, V&V report | `nrc-nuclear` |
| Software reviews & audits | software review, technical review, management review, inspection, walkthrough, software audit, audit | `nrc-nuclear` |
| Software configuration management | configuration management, SCM, CM plan, SCMP, baseline, configuration item, change control, configuration status accounting, configuration audit | `nrc-nuclear` |
| Software test documentation | test documentation, test plan, test design, test case, test procedure, test report, test log, anomaly report | `nrc-nuclear` |
| Software unit testing | unit testing, software unit testing, unit test, unit test coverage | `nrc-nuclear` |
| Software requirements specifications | software requirements specification, SRS, software requirements, requirements traceability, complex electronics | `nrc-nuclear` |
| Software life cycle processes | software life cycle, life-cycle process, life cycle model, software development plan, software management plan, software quality assurance plan | `nrc-nuclear` |
| BTP 7-14 software review | BTP 7-14, branch technical position 7-14, staff software review, acceptance criteria, implementation review, design outputs review, plan review | `nrc-nuclear` |
| Digital I&C safety system software | digital I&C, digital instrumentation and control, safety system software, safety-related software, digital computer software, nuclear power plant software | `nrc-nuclear` |
| Endorsed IEEE, IEC & IAEA standards | IEEE 603, IEEE 7-4.3.2, IEEE 828, IEEE 829, IEEE 830, IEEE 1008, IEEE 1012, IEEE 1028, IEEE 1074, IEC 60880, IEC 61513, IEC 62138, IAEA, SSG-39, RG 1.152, BTP 7-19, SDOE, Appendix 7.1-D, 7.1-D | `nrc-nuclear` |
| PLC in digital safety I&C | PLC, programmable logic controller, BTP 7-18, branch technical position 7-18 | `nrc-btp-7-18-plc` |
| PLC software and firmware boundary | PLC firmware, PLC software, programmable logic firmware, embedded logic PLC | `nrc-btp-7-18-plc` |
| PLC life cycle versus BTP 7-14 | PLC life cycle, PLC software life cycle, BTP 7-18 life cycle | `nrc-btp-7-18-plc`, `nrc-nuclear` |
| Commercial dedication of PLCs | PLC commercial dedication, PLC commercial grade dedication, PLC dedication | `nrc-btp-7-18-plc` |
| PLC failure modes | PLC failure mode, programmable logic failure, PLC common cause | `nrc-btp-7-18-plc` |
| PLC documentation set | PLC documentation, PLC software documentation, BTP 7-18 documentation | `nrc-btp-7-18-plc` |
| RG 1.152 and Appendix 7.1-D from a PLC question | PLC RG 1.152, PLC 7.1-D, PLC programmable digital device | `nrc-btp-7-18-plc`, `nrc-nuclear` |
| Part 50 licensing basis | Part 50, domestic licensing, production and utilization facilities | `nrc-10cfr-part50-licensing-basis` |
| Contents of applications | 50.34, contents of applications, FSAR, safety analysis report | `nrc-10cfr-part50-licensing-basis` |
| Technical specifications | 50.36, technical specifications, tech specs, limiting conditions | `nrc-10cfr-part50-licensing-basis` |
| Conditions of licenses | 50.54, conditions of licenses, license conditions | `nrc-10cfr-part50-licensing-basis` |
| Changes, tests, experiments | 50.59, 50.59 screening, changes tests experiments | `nrc-10cfr-part50-licensing-basis` |
| General Design Criteria | GDC, general design criteria, Appendix A | `nrc-10cfr-part50-licensing-basis`, `nrc-nuclear` |
| Licensing basis overview | licensing basis, Part 50 overview, licensing root | `nrc-10cfr-part50-licensing-basis` |
| QA program criteria | RG 1.28, QA program criteria, quality assurance program criteria | `nrc-qa-rg-1-28` |
| NQA-1 | NQA-1, ASME NQA-1, QA standard editions | `nrc-qa-rg-1-28` |
| Appendix B criteria overview | Appendix B criteria, eighteen criteria, QA criteria overview | `nrc-qa-rg-1-28` |
| Commercial-grade services | NEI 14-05A, laboratory calibration accreditation, accreditation in lieu of commercial grade surveys | `nrc-qa-rg-1-28` |
| QA in licensing | QA program description, 50.34 QA, design and construction QA | `nrc-qa-rg-1-28`, `nrc-10cfr-part50-licensing-basis` |

### Agency contexts
| Agency | Keywords | Packs |
|---|---|---|
| NRC | NRC, Nuclear Regulatory Commission, NUREG-0800, SRP, Standard Review Plan, Regulatory Guide | `nrc-nuclear`, `nrc-10cfr-part50-licensing-basis`, `nrc-btp-7-18-plc`, `nrc-qa-rg-1-28` |

### Deliverables
| Deliverable | Keywords | Draft | Review | Verify |
|---|---|---|---|---|
| Software V&V plan outline | V&V plan outline, SVVP outline, verification and validation plan outline | `nrc-nuclear` | `nrc-nuclear` | `nrc-nuclear` |
| Software CM plan review | CM plan review, SCMP review, configuration management plan review | `nrc-nuclear` | `nrc-nuclear` | `nrc-nuclear` |
| SRS review checklist | SRS review checklist, requirements specification review, SRS checklist | `nrc-nuclear` | `nrc-nuclear` | `nrc-nuclear` |
| BTP 7-14 review readiness matrix | review readiness matrix, BTP 7-14 readiness, software review readiness | `nrc-nuclear` | `nrc-nuclear` | `nrc-nuclear` |
| PLC question list | PLC review questions, BTP 7-18 question list, PLC review outline | `nrc-btp-7-18-plc` | `nrc-btp-7-18-plc` | `nrc-btp-7-18-plc` |
| Part 50 licensing basis question list | Part 50 question list, licensing basis review questions, licensing basis outline | `nrc-10cfr-part50-licensing-basis` | `nrc-10cfr-part50-licensing-basis` | `nrc-10cfr-part50-licensing-basis` |
| QA criteria question list | QA criteria questions, RG 1.28 question list, QA program outline | `nrc-qa-rg-1-28` | `nrc-qa-rg-1-28` | `nrc-qa-rg-1-28` |

### Licences
| Pack | Licence |
|---|---|
<!-- ROUTING-MAP:END -->

## Host modes

Pick the highest mode the host can run:

| Mode | When | Behaviour |
|---|---|---|
| Fan-out | Sub-agents available | One brief per pack in parallel; main thread composes the answer. On sub-agent failure, rerun that brief in the main thread. |
| Sequential | No sub-agents, member files readable | Same briefs one at a time; write each pack's notes before opening the next. |
| Index-only | Transform installs (Codex, Gemini, Cursor rules) | Read sibling index files when readable. Cite `[slug index]` only, name chapters as follow-ups, and label the answer `index-level: chapter bodies not installed`. |
| Route-only | No member file readable | Report the routing decision and the `/slug` commands only. Make **no Nuclear claims**. |

**Native-root fallback.** When the skill folder is not revealed, try
`~/.claude/skills/`, `~/.openclaw/skills/`, `~/.copilot/skills/`, each with and
without the `jgs-nuclear-knowledge-packs/` namespace. Transform index files live at
`~/.codex/prompts/<slug>.md`, `~/.gemini/commands/jgs-nuclear-knowledge-packs/<slug>.toml`,
and `./.cursor/rules/<slug>.mdc`.

Narrow consults read in the main thread on every host. A missing routed pack is
noted and skipped; if none remain, fall back to route-only.

## Scope & Limits

- No Nuclear claim without a citation from a pack file read this session.
- The map is curated, not exhaustive. Agency rows are a filter, not an endorsement.
- At most six packs per Topics row. At most four packs read per answer.
- Deliverable stage chains come only from Deliverables rows; empty cells skip that stage.
- `/nuclear` never overwrites an existing file without a yes at a gate.
- **Sector charter.** Catalogue covers civilian nuclear power plant digital I&C
  software assurance and Part 50 licensing-basis orientation under live packs
  (today: `nrc-nuclear`, `nrc-btp-7-18-plc`, `nrc-10cfr-part50-licensing-basis`, `nrc-qa-rg-1-28`) plus name-only
  standards signposts. It is not a general nuclear engineering library.
- **Never route or invent content for:** nuclear weapons or weapons-design
  physics; classified, export-controlled, or safeguards-sensitive material
  (including NNSA / defence nuclear programmes beyond public civil guidance);
  medical, industrial, or research-isotope programmes outside power-plant
  safety systems (for example 10 CFR Part 35); pure physics textbooks with no
  plant or licensing deliverable; full text of paywalled standards (IEEE, IEC,
  ASME, ANS, NFPA, and similar); legal or licensing advice.
- On a never-in-scope question: state the exclusion in one or two sentences,
  cite this section, and stop. Do not stretch a pack or fabricate chapters.

---
*Orchestrator content © JG Systems Consulting Ltd. (MIT). Pack names and source titles
are identified for routing only; each pack keeps its own licence.*
