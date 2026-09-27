<!--
Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

<h1 align="center">jgs-nuclear-knowledge-packs</h1>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT%20(tooling)-blue" alt="License: MIT (tooling)">
  <img src="https://img.shields.io/badge/version-0.2.0-green" alt="Version 0.2.0">
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
Guides 1.169 through 1.173 Revision 1, and NUREG-0800 Branch Technical Position
7-14 Revision 6, plus signposts to the wider nuclear standards world (IEEE, IEC,
and IAEA standards, cited by name only). It is engineering signposting and
reference material, not legal or licensing advice.

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

## Gates

Run all three from the repo root:

```bash
python tooling/validate_pack.py --all   # every pack matches docs/PACK-SPEC.md
python tooling/check_release.py         # release readiness: files, versions, leaks, links, index, headers
python tooling/test_ci_gate.py          # proves CI (.github/workflows/validate.yml) checks the same things
```

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
