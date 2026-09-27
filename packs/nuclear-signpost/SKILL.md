---
name: nuclear-signpost
kind: signpost
description: "Signpost (not a knowledge pack) for nuclear I&C software and safety standards named by the NRC 2013 RG family and BTP 7-14: IEEE Std 603-1991, IEEE Std 7-4.3.2-2003, IEEE Std 828-2005, IEEE Std 829-2008, IEEE Std 830-1998, IEEE Std 1008-1987, IEEE Std 1012-2004, IEEE Std 1028-2008, IEEE Std 1074-2006; IEC 60880 ed. 2.0:2006, IEC 61513 ed. 2.0:2011, IEC 62138 ed. 2.0:2018; and IAEA safety guides (SSG-39 named). Contains no source content: each row carries only the designation, title, edition, owner, redistributability status, and the owner's URL. Use when you need to identify, cite, or locate one of these standards; paywalled rows point to IEEE or IEC, the IAEA row is designation-only, and free NRC-side text lives in pack nrc-nuclear."
---

# Nuclear I&C Software and Safety Standards: Signpost (pointers only)

**This is a signpost, not a knowledge pack.** It carries **no standards-body content**:
no reproduced clauses, no normative text, no synthesised summaries of the standards.
The IEEE and IEC rows below are paywalled with no redistribution grant (Excluded under
this repo's `docs/SOURCE-VETTING.md`). IAEA safety guides such as SSG-39 are free to
read but remain IAEA copyright and stay citation-only until a written reuse grant is
confirmed per document. What this skill does: tell you which document you want, who
owns it, whether a free copy exists, and where to get the authentic one.

**Sources line:** Editions are taken verbatim from
`packs/nrc-nuclear/chapters/ch08-endorsed-standards-and-adjacent-guidance.md`
(name-only map X1-X13). Do not silently upgrade an edition.

## When to use

You are developing, assessing, or reviewing nuclear power plant digital I&C or safety
software and need to identify or cite a governing IEEE, IEC, or IAEA document named by
the NRC 2013 RG family or BTP 7-14: which IEEE edition the pack pins for V&V, SCM,
requirements, unit testing, life cycle, or safety-system criteria; which IEC edition
covers Category A software or Category B/C software; which IAEA guide is named for
international I&C context. Paywalled rows route you to the owner. Free NRC staff
positions and the name-only map live in pack `nrc-nuclear`.

**Prerequisites:** none, plain Markdown.

## How to use

Find your document below. The **Status** column says whether it can be packaged:

- **Excluded**: paywalled, no redistribution grant; buy from the owner. *Cannot* be packaged here.
- **Citation-only**: free to read from the owner, but copyright terms bar repackaging until a written per-document determination exists; use the owner site, not this repo.

Editions match ch08 character-for-character. Do not quote a publication date or revision
that a row does not carry. Owner URLs appear here only because this pack is a signpost;
the repo link policy bars source-material URLs everywhere else.

## IEEE software and safety-system suite

| Designation | Title | Edition | Owner | Status | URL |
|-------------|-------|---------|-------|--------|-----|
| IEEE Std 603 | IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations | 1991 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/603-1991.html |
| IEEE Std 7-4.3.2 | IEEE Standard Criteria for Digital Computers in Safety Systems of Nuclear Power Generating Stations | 2003 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/7-4.3.2-2003.html |
| IEEE Std 828 | IEEE Standard for Software Configuration Management Plans | 2005 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/828-2005.html |
| IEEE Std 829 | IEEE Standard for Software and System Test Documentation | 2008 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/829-2008.html |
| IEEE Std 830 | IEEE Recommended Practice for Software Requirements Specifications | 1998 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/830-1998.html |
| IEEE Std 1008 | IEEE Standard for Software Unit Testing | 1987 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/1008-1987.html |
| IEEE Std 1012 | IEEE Standard for Software Verification and Validation | 2004 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/1012-2004.html |
| IEEE Std 1028 | IEEE Standard for Software Reviews and Audits | 2008 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/1028-2008.html |
| IEEE Std 1074 | IEEE Standard for Developing a Software Project Life Cycle Process | 2006 | IEEE | Excluded: paywalled, no redistribution grant; buy from the owner | https://standards.ieee.org/standard/1074-2006.html |

## IEC NPP I&C software

| Designation | Title | Edition | Owner | Status | URL |
|-------------|-------|---------|-------|--------|-----|
| IEC 60880 | Nuclear power plants - Instrumentation and control systems important to safety - Software aspects for computer-based systems performing category A functions | ed. 2.0:2006 | IEC | Excluded: paywalled, no redistribution grant; buy from the owner | https://webstore.iec.ch/en/publication/3747 |
| IEC 61513 | Nuclear power plants - Instrumentation and control important to safety - General requirements for systems | ed. 2.0:2011 | IEC | Excluded: paywalled, no redistribution grant; buy from the owner | https://webstore.iec.ch/en/publication/5529 |
| IEC 62138 | Nuclear power plants - Instrumentation and control systems important to safety - Software aspects for computer-based systems performing category B or C functions | ed. 2.0:2018 | IEC | Excluded: paywalled, no redistribution grant; buy from the owner | https://webstore.iec.ch/en/publication/63704 |

## IAEA

| Designation | Title | Edition | Owner | Status | URL |
|-------------|-------|---------|-------|--------|-----|
| IAEA safety guides (e.g. SSG-39) | Design of Instrumentation and Control Systems for Nuclear Power Plants (SSG-39 named as the worked example) | as named by the citing source | IAEA | Citation-only pending per-document determination; free to read, IAEA copyright; not packaged | https://www.iaea.org/ |

## Free paths in this repo and fleet

- **pack: nrc-nuclear** (this repo). Free NRC-side reconstructed notes for the July 2013 RG family (RG 1.168 Rev 2, RG 1.169-1.173 Rev 1) and NUREG-0800 BTP 7-14 Rev 6, plus ch08's name-only edition map for the rows above. The IEEE/IEC texts stay with their owners; nrc-nuclear carries the NRC staff positions.
- Fleet sibling repos are named, not linked, per the fleet link policy. No other fleet content pack ships these IEEE/IEC editions.

## Scope and limits

- No IEEE, IEC, or IAEA standard text appears in this skill or anywhere else in the repo.
- Editions are pinned as cited in nrc-nuclear ch08. Later IEEE or IEC editions exist; do not upgrade inside pack prose.
- RG 1.152 Rev 4, BTP 7-18, BTP 7-19, App 7.1-D, and NUREG/CR contractor reports are outside this signpost (see nrc-nuclear ch08 for the adjacent-NRC name map).
- Not legal or licensing advice. Not a substitute for the authentic standard or for the plant licensing basis.

---
*Signpost content (c) JG Systems Consulting Ltd. (MIT). Standard designations and titles
are named for reference only; "IEEE", "IEC", "IAEA", and document numbers are the
property of their respective owners. Named for identification, not endorsement.*
