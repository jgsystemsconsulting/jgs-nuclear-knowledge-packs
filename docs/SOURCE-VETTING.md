<!--
Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Source Vetting

This is the integrity document for the repository. **No pack is accepted unless its
source clears this rubric.** The whole value of `jgs-nuclear-knowledge-packs` is that every pack
is redistributable by construction, so a colleague can install it, and we can publish it,
without a copyright or licence breach.

The governing principle:

> **"Free to download" is not "free to redistribute."**

A document you can read for free on a website may still be all-rights-reserved. A
knowledge pack *reproduces and transforms* a source into new files that we then publish.
That is redistribution plus derivative work. It needs an actual grant.

---

## The eligibility tiers

A source must land in **Tier 1 or Tier 2** to be packaged. Tier 3 is case-by-case and
needs a written rationale in the pack's `PACK.yaml`. The Excluded tier is a hard stop.

### 🟢 Tier 1: Public domain (maximum freedom)

Works with no copyright, or an explicit public-domain dedication. Reproduce, transform,
and redistribute freely. Attribution is courtesy, not obligation.

- **US Government works**: not subject to copyright in the US (17 U.S.C. § 105).
  Examples: NASA, NIST, US DoD, FAA publications.
- Look for a **Distribution Statement A** ("Approved for public release; distribution is
  unlimited") on defense documents, or a US-gov-authorship statement.
- CC0 / explicit public-domain dedication.

### 🟡 Tier 2: Open licence (shareable with conditions)

A licence that grants redistribution and (ideally) derivative works. The pack **must
carry the source's conditions forward**: attribution, share-alike, non-commercial,
trademark limits.

- **Creative Commons** BY, BY-SA, BY-NC, BY-NC-SA. (NC and SA propagate to the pack;
  see "Carrying conditions forward" below.)
- **Open Government Licence-style grants** (e.g. UK Open Government Licence v3):
  expressly permit copy, publish, and adapt with attribution. Conditions are captured
  per document (see "Per-document capture (industry)" below).
- Permissive software/content licences (MIT, Apache-2.0, BSD) where they cover the text.

> **Not Tier 2: OMG specifications.** The OMG Specification License *looks* open but its
> public grant is informational-use-only (no network posting, no modification; see the
> Excluded list). Do not classify OMG specs as Tier 2.

### 🟠 Tier 3: Caution (verbatim-only or unclear grant)

Package only with an explicit written justification in `PACK.yaml` and, where the grant
is ambiguous, a note that the maintainers judged it defensible (or sought permission).

- **No-derivatives clauses** (e.g. CC BY-ND). A knowledge pack transforms the source, so a
  strict no-derivatives source is normally **not** packageable, at most a verbatim excerpt
  with heavy citation. Prefer to exclude. (OMG specs are fully **Excluded**; see below.)
- **"Freely available" with no stated licence.** Free download ≠ redistribution grant.
  Treat as Excluded until a real grant is found or permission is obtained.

### 🔴 Excluded: read-only, not redistributable (hard stop)

These are valuable and you may *read and cite* them, but you may **not** package them.
This list exists so the repo never ships something that triggers a takedown.

| Source | Why excluded |
|---|---|
| **ISO 26262, IEC 61508, ISO-SAE 21434** (functional safety, functional safety of E/E systems, road-vehicle cybersecurity engineering standards) | Paywalled, all-rights-reserved; per-user licence model. Hard stop. (programme research 2026-09-24, docs/superpowers ingest bundle.) |
| **RTCA DO-178C / DO-254, SAE ARP4754A / ARP4761** (avionics software/hardware design assurance; civil aircraft systems development and safety assessment) | Paywalled; no redistribution or derivative grant. (programme research 2026-09-24, docs/superpowers ingest bundle.) |
| **ECSS standards (ESA/European space)** | Free download from ecss.nl but © ESA; "No ECSS document may be reproduced in any form without the explicit consent of ESA" (ECSS-P-00C §5.8). A pack is reproduction + derivative work. Carried from the exemplar vetting. (programme research 2026-09-24, docs/superpowers ingest bundle.) |
| **Def Stan documents (UK defence standards)** | Case-by-case: Crown copyright, downloads free of charge but registration-gated via the DSTAN portal. **Def Stan 00-051 is UNVERIFIED** pending a registered DSTAN user recording the cover licence statement; excluded until then. If OGL v3.0 applies inside the document → Tier 2; if bespoke MOD-consent/no-reproduction terms → stays Excluded. (programme research 2026-09-24, docs/superpowers ingest bundle.) |
| **IMO conventions and class-society rules** (e.g. SOLAS, MARPOL, classification society rule sets) | Paywalled or unclear reuse terms; no redistribution/derivative grant identified. (programme research 2026-09-24, docs/superpowers ingest bundle.) |
| **OMG formal specifications** (UML, SysML, BPMN, UAF, CORBA, MOF, XMI, OCL, DDS…) | OMG Specification License public grant is informational-use-only: the spec "will not be copied or posted on any network computer … or … transferred for commercial purposes" and "no modifications are made to this specification." A hosted, transformed pack breaches both. Cite + link to the OMG download; never package. Carried from the exemplar vetting. |
| **X1 IEEE Std 1012-2004** (IEEE) | Paywalled. Endorsed by RG 1.168 Rev 2. Excluded; name-only in ch05. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X2 IEEE Std 1028-2008** (IEEE) | Paywalled. Endorsed by RG 1.168 Rev 2. Excluded; name-only in ch05. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X3 IEEE Std 828-2005** (IEEE) | Paywalled. Endorsed by RG 1.169 Rev 1. Excluded; name-only in ch04. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X4 IEEE Std 829-2008** (IEEE) | Paywalled. Endorsed by RG 1.170 Rev 1. Excluded; name-only in ch06. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X5 IEEE Std 1008-1987** (IEEE) | Paywalled. Endorsed by RG 1.171 Rev 1. Excluded; name-only in ch06. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X6 IEEE Std 830-1998** (IEEE) | Paywalled. Endorsed by RG 1.172 Rev 1. Excluded; name-only in ch03. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X7 IEEE Std 1074-2006** (IEEE) | Paywalled. Endorsed by RG 1.173 Rev 1. Excluded; name-only in ch02. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X8 IEEE Std 603-1991** (IEEE) | Paywalled (later editions exist; cite 1991). Safety system criteria cited by the 2013 family. Excluded; name-only in ch01/ch08. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X9 IEEE Std 7-4.3.2-2003** (IEEE) | Paywalled. Cited by the 2013 family (RG 1.152 Rev 4 endorses the 2016 edition; that is not this slice). Excluded; name-only in ch08. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X10 IEC 60880 ed. 2.0:2006** (IEC) | Paywalled. NPP software, Category A. Excluded; name-only in ch08. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X11 IEC 61513 ed. 2.0:2011** (IEC) | Paywalled. NPP I&C system-level requirements. Excluded; name-only in ch08. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X12 IEC 62138 ed. 2.0:2018** (IEC) | Paywalled. Software for Category B and C. Excluded; name-only in ch08. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X13 IAEA safety guides (e.g. SSG-39)** (IAEA) | Free to read, IAEA copyright. International I&C context. Excluded, citation-only until a written reuse grant is confirmed per document. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X14 Regulatory Guide 1.152 Rev 4, July 2023, ML23054A463** (NRC) | US Government work, public domain. Criteria/SDOE companion endorsing IEEE 7-4.3.2-2016. Citation-only in ch08; out of pack body by scope ruling. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X15 NUREG-0800 BTP 7-18 Rev 6 (ML16019A327), BTP 7-19 Rev 9 May 2024 (ML24005A077), App 7.1-D Rev 1 (ML16019A114)** (NRC) | US Government work, public domain. PLC platform, diversity/CCF, IEEE 7-4.3.2 evaluation. Out of pack body by scope ruling; BTP 7-19 named in ch08 as the current diversity/CCF position. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |
| **X16 NUREG/CR contractor reports** (worked example NUREG/CR-6463, SoHar Inc., June 1996, ML063470583) | Contractor for NRC; not auto-cleared. Contractor authorship on title page. Excluded pending a written per-document determination (title page and NRC reuse statement) filed here; CR-6463 is the software-languages report, not a V&V handbook. NUREG/CR contractor reports are excluded until that determination is filed. (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md.) |

> If you are licensed to read one of these (e.g. an employer's standards seat), that
> licence is **yours**, not the repo's. Building a pack from it for
> your own private use may be fine; **publishing that pack here is not.** Keep
> source-restricted packs in a private/local skills directory, never in this repo.

**Not yet vetted:** ISO 14971, IEC 62304, ISO/IEC 42001. A sector build adds these rows
only after its own research pass records licence status.

---

## Per-document capture (industry)

Sector sources that allow reuse often attach conditions per document. Before packaging,
record the required capture in the pack:

| Source family | Capture rule |
|---|---|
| **OGL v3** (e.g. gov.uk publications) | Forward attribution; source link inside the pack |
| **EU MDCG guidance** | Reuse with attribution |
| **EASA documents** | Per-document reuse confirmation before packaging |
| **UK DEF-STAN** | Per-document licence statement before packaging |

For industry families in this table, the per-document capture rule (including the OGL source-acknowledgement link inside the pack) overrides the general link policy for those sources.

## Blocking checklists

- **UNECE R155 / R156**: availability re-verification is required before any automotive
  signpost row depends on it.

## Cleared families (programme research 2026-09-24)

tier-1 US federal publisher works cleared for sector use (FDA, NHTSA, NRC, FAA orders); tier-2 gov.uk OGL JSPs, per-document capture.

| Source set | Basis |
|---|---|
| **NRC software assurance set S1-S7** (RG 1.168 Rev 2 (ML13073A210); RG 1.169 Rev 1 (ML12355A642); RG 1.170 Rev 1 (ML13003A216); RG 1.171 Rev 1 (ML13004A375); RG 1.172 Rev 1 (ML13007A173); RG 1.173 Rev 1 (ML13009A190); NUREG-0800 BTP 7-14 Rev 6 (ML16019A308)) | US Government works, 17 U.S.C. § 105. Cleared Tier 1 for the nrc-nuclear pack (nuclear sector build 2026-09-26; binding spec docs/superpowers/specs/2026-09-25-nuclear-sector-repo.md). SOURCE-VETTING carries no agency-host URLs; ML accession ids and document titles only. |

Sector builds start from this explicit allowlist; anything not listed still goes through
the tiers above.

---

## Carrying conditions forward

When a source is Tier 2, the pack inherits its obligations:

- **Attribution (BY)**: `PACK.yaml` records title, author/publisher, version, URL; the
  pack `LICENSE` file reproduces the source notice.
- **Share-alike (SA)**: the pack's *content* is released under the same licence as the
  source (not the repo's MIT). State this in the pack `LICENSE`.
- **Non-commercial (NC)**: the pack is flagged `commercial_use: false` in `PACK.yaml`.
  The repo tooling (MIT) is separate from pack *content* licences.
- **Trademark / no-endorsement**: do not imply the source's authors endorse the pack;
  do not use a trademarked spec name on a transformed work (OMG rule).

The repository tooling and scaffolding are MIT. **Pack content licences are independent
and per-pack**: a pack folder always contains its own `LICENSE`.

---

## The vetting checklist (run before opening a pack PR)

1. [ ] Identified the exact source document, version, and publisher. (Read the source's
   own licence to vet it; the source URL is used for vetting only, never published.)
2. [ ] Found the **licence statement** in the source itself (not a third-party claim).
3. [ ] Assigned a tier (1 / 2 / 3) with the licence named.
4. [ ] Source is **not** on the Excluded list.
5. [ ] If Tier 2: NC / SA / BY / trademark conditions recorded in `PACK.yaml`.
6. [ ] If Tier 3: written justification present.
7. [ ] Pack folder contains a `LICENSE` reproducing the source's terms.
8. [ ] `PACK.yaml` `title`, `publisher`, `license`, `license_tier`, `commercial_use`
   filled: textual attribution, **no source-material URL published** (see LICENSING.md).

CI enforces 4, 7, and 8 mechanically (`tooling/validate_pack.py`). Tiers 1–3 judgement
is human and reviewed on the PR.

> **Link policy.** Source-material URLs are recorded during vetting but are **not**
> published anywhere in a pack or the docs. Attribution travels as text (title +
> publisher + version + licence) plus the licence-deed link, which the licences accept.
> See [LICENSING.md](LICENSING.md) §4.
