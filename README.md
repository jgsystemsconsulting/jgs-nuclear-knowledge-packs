<!--
Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

<h1 align="center">jgs-nuclear-knowledge-packs</h1>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT%20(tooling)-blue" alt="License: MIT (tooling)">
  <img src="https://img.shields.io/badge/version-0.3.0-green" alt="Version 0.3.0">
</p>

<p align="center">
  <strong>Installable catalogue of nuclear engineering knowledge-pack skills for
  coding agents, with one orchestrator that routes free-text sector questions to
  the right packs.</strong>
</p>

**Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (tooling); pack content under each source's own licence (see [NOTICE](NOTICE)).**

---

## What it is

This repo is the Nuclear member of the industry knowledge-pack fleet: one repo
per engineering sector, each an installable catalogue of knowledge-pack skills for
coding agents. The packs are reconstructed reference notes on U.S. Nuclear
Regulatory Commission software assurance guidance for digital computer software in
nuclear power plant safety systems: Regulatory Guide 1.168 Revision 2, Regulatory
Guides 1.169 through 1.173 Revision 1, NUREG-0800 Branch Technical Position
7-14 Revision 6, Regulatory Guide 1.152 Revision 4, and NUREG-0800 Appendix 7.1-D Revision 1, plus signposts to the wider nuclear standards world (IEEE, IEC,
and IAEA standards, cited by name only). It is engineering signposting and
reference material, not legal or licensing advice. **Not in scope:** nuclear
weapons, medical/clinical use (e.g. 10 CFR Part 35), classified material, or
full paywalled standard text. Full exclusion list: [Out of scope](#out-of-scope)
below and [docs/PACK-BACKLOG.md](docs/PACK-BACKLOG.md) hard walls.

## Out of scope

This catalogue is **civilian nuclear power plant digital I&C software
assurance** under the pinned NRC sources above. It is not a general nuclear
engineering library.

**Never in scope (do not add, route, or reconstruct):**

- Nuclear weapons, warheads, delivery systems, or weapons-design physics
- Classified, export-controlled, or safeguards-sensitive material (including
  NNSA / defence nuclear programmes beyond public civil guidance)
- Medical, industrial, or research-isotope uses outside power-plant safety
  systems (for example 10 CFR Part 35 medical use)
- Pure reactor-physics or radiation-transport textbooks with no licensing
  or plant-engineering deliverable
- Full text of paywalled standards (IEEE, IEC, ASME, ANS, NFPA, and similar):
  designation and edition only; buy or read at the owner
- Legal, licensing, or compliance advice; substitute counsel or the plant
  licensing basis

**In this release, also outside the live pack** (may appear later as separate
packs or stay excluded): BTP 7-18, BTP 7-19, other SRP Chapter 7 sections,
NUREG/CR contractor reports, PRA, fire protection, human factors,
cybersecurity beyond the RG 1.152 SDOE slice, fuel/criticality, emergency
preparedness, decommissioning, SMR/advanced-reactor frameworks, and non-US
regulator bodies except name-only IAEA signposts already listed.

If a question falls in the never-in-scope list, say so and stop. Do not
stretch the pack to cover it.

**Future packs:** thematic candidate list, source pins, waves, and build
checklist live in [docs/PACK-BACKLOG.md](docs/PACK-BACKLOG.md). That backlog is
research-ready scope, not a promise that every row will ship.

## Install

```bash
python install.py --dry-run   # preview
python install.py             # install the packs as agent skills
```

Shell equivalents: `install.sh` (bash) and `install.ps1` (PowerShell). After
install, each pack is invocable as an Agent Skill.

## Use

- **`/nuclear <question>`**: the orchestrator. Type a free-text nuclear question
  and it routes through a curated topic, agency, and deliverable map to the right
  pack(s), reads them, and answers with pack and chapter citations.
- **Using packs directly**: see [docs/skill-usage.md](docs/skill-usage.md) for
  install, invoking a pack by slug (`/<slug>`), how a pack answers, and the
  `/nuclear` orchestrator modes.

## Gates

Run all three from the repo root:

```bash
python tooling/validate_pack.py --all   # every pack matches docs/PACK-SPEC.md
python tooling/check_release.py         # release readiness: files, versions, leaks, links, index, headers
python tooling/test_ci_gate.py          # proves CI (.github/workflows/validate.yml) checks the same things
```

Local probe note: `tooling/test_ci_gate.py` positive runs fail link-policy in a tree carrying gitignored `sources/*` build inputs. Run it from a clean checkout or worktree, or move `sources/*` aside first, then restore `sources/*` after the run; `sources/*` are gitignored build inputs, never commit them.

CI green is not release-ready: `check_release.py` is the pre-tag gate. Run it
before tagging and confirm the sha on its `RELEASE CHECK: PASS` receipt matches
the commit you tag.

## Licence

Two separable layers:

- **Pack content:** Public Domain (US Government work, 17 U.S.C. 105) for the
  NRC-derived material. Attributions and caveats live in [NOTICE](NOTICE) and
  each `packs/<slug>/LICENSE`; the model is set out in
  [docs/LICENSING.md](docs/LICENSING.md).
- **Tooling and scaffolding:** [MIT](LICENSE) (JG Systems Consulting Ltd.).
