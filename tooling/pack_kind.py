#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
pack_kind.py: the single kind classifier for pack members.

A pack's kind comes exclusively from a `kind:` line inside the `---` fenced
YAML frontmatter block of packs/<slug>/SKILL.md. Body text never classifies:
a `kind: signpost` line below the fence must not flip the validate_pack
LICENSE/chapters skip or the link-policy exemption (spec P5, review finding
I6). Matching is case-sensitive: YAML mapping keys are case-sensitive, and an
exemption from the source-material link ban must not widen on a key no parser
reads (`Kind: Signpost` is a different key and classifies content).

stdlib only (imports re). Local gates import this module; the CI workflow
(.github/workflows/validate.yml) never executes checked-out repository code,
so it inline-replicates these regexes byte-identically; the parity is pinned
by tooling/test_ci_gate.py (KIND_PAIR, Task 3).
"""
from __future__ import annotations

import re

# The one frontmatter window for every reader. Anchored at file start (no
# re.M, so `^` binds to the string start); the closing fence may be the last
# line of the file with no trailing newline (`(?:\n|$)`).
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.S)

# Kind lines, matched inside the extracted frontmatter only. Case-sensitive
# by design (AD-2); the `\s*` tolerance inside the value stays as is (spec
# non-goal, residual risk accepted in the spec threat model).
SIGNPOST_RE = re.compile(r"^kind:\s*signpost\s*$", re.M)
ORCHESTRATOR_RE = re.compile(r"^kind:\s*orchestrator\s*$", re.M)


def pack_kind(skill_text: str) -> str:
    """Classify a SKILL.md text: "signpost" | "orchestrator" | "content".

    Reads only the frontmatter window. Unparseable or absent frontmatter is
    "content" (fail-closed: no exemption without parseable frontmatter). When
    both kind lines are present, signpost wins (the inventory's if/elif
    order, kept as the one shared semantics).
    """
    m = FM_RE.match(skill_text)
    if not m:
        return "content"
    fm = m.group(1)
    if SIGNPOST_RE.search(fm):
        return "signpost"
    if ORCHESTRATOR_RE.search(fm):
        return "orchestrator"
    return "content"


if __name__ == "__main__":
    raise SystemExit("pack_kind.py is a library; import it, do not run it")
