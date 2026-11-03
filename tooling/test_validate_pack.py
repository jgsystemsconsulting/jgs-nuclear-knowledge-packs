#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based checks for validate_pack.check_pack pack-shape classification (no framework).

Run:  python tooling/test_validate_pack.py
Exits 0 when content-pack, signpost-pack, and orchestrator-pack shapes classify
as PACK-SPEC expects. Any failed assert raises and exits nonzero. Fixtures are
built in a temp dir; the live tree is only read (case 9), never mutated.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pack_kind  # noqa: E402
import validate_pack  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

CONTENT_SKILL = """---
name: {slug}
description: "Demo content pack used by the validator probe."
---
"""

SIGNPOST_SKILL = """---
name: {slug}
kind: signpost
description: "Demo signpost used by the validator probe."
---
"""

SIGNPOST_NO_DESC = """---
name: {slug}
kind: signpost
---
"""

ORCHESTRATOR_SKILL = """---
name: {slug}
kind: orchestrator
disable-model-invocation: true
description: "Demo orchestrator used by the validator probe. Explicit invocation only."
---
"""

BODY_PLANTED_SKILL = """---
name: {slug}
description: "Demo pack with a kind line planted below the frontmatter fence."
---
body text below the fence
kind: signpost
"""

WRONG_CASE_SKILL = """---
name: {slug}
Kind: Signpost
description: "Demo pack with a wrong-case kind declaration."
---
"""

PACK_YAML = """slug: {slug}
title: "Demo Pack"
publisher: "JG Systems Consulting Ltd."
license: "MIT"
license_tier: 2
commercial_use: true
"""


def build_pack(root: Path, slug: str, *, skill: str | None, pack_yaml: bool = True,
               license_: bool = True, chapters: bool = True) -> Path:
    d = root / slug
    d.mkdir()
    if skill is not None:
        (d / "SKILL.md").write_text(skill.format(slug=slug), encoding="utf-8")
    if pack_yaml:
        (d / "PACK.yaml").write_text(PACK_YAML.format(slug=slug), encoding="utf-8")
    if license_:
        (d / "LICENSE").write_text("MIT", encoding="utf-8")
    if chapters:
        (d / "chapters").mkdir()
        (d / "chapters" / "ch01-intro.md").write_text("# Intro\n", encoding="utf-8")
    return d


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        # (1) full content-pack shape passes
        full = build_pack(root, "full-pack", skill=CONTENT_SKILL)
        assert validate_pack.check_pack(full) == [], validate_pack.check_pack(full)

        # (2) content pack minus LICENSE fails with the LICENSE error
        no_lic = build_pack(root, "no-license", skill=CONTENT_SKILL, license_=False)
        errs = validate_pack.check_pack(no_lic)
        assert errs == ["missing LICENSE (must reproduce the source's terms)"], errs

        # (3) content pack minus chapters/ fails with the chapters error
        no_ch = build_pack(root, "no-chapters", skill=CONTENT_SKILL, chapters=False)
        errs = validate_pack.check_pack(no_ch)
        assert errs == ["missing chapters/ directory"], errs

        # (4) signpost shape (SKILL.md + PACK.yaml only) passes
        sign = build_pack(root, "demo-signpost", skill=SIGNPOST_SKILL,
                          license_=False, chapters=False)
        assert validate_pack.check_pack(sign) == [], validate_pack.check_pack(sign)

        # (5) signpost missing SKILL.md fails: kind cannot be proven
        bare = build_pack(root, "bare-signpost", skill=None,
                          license_=False, chapters=False)
        errs = validate_pack.check_pack(bare)
        assert errs == ["missing SKILL.md",
                        "missing LICENSE (must reproduce the source's terms)",
                        "missing chapters/ directory"], errs

        # (6a) signpost missing PACK.yaml still fails
        no_meta = build_pack(root, "no-meta-signpost", skill=SIGNPOST_SKILL,
                             pack_yaml=False, license_=False, chapters=False)
        errs = validate_pack.check_pack(no_meta)
        assert errs == ["missing PACK.yaml"], errs

        # (6b) signpost frontmatter missing description still fails
        no_desc = build_pack(root, "no-desc-signpost", skill=SIGNPOST_NO_DESC,
                             license_=False, chapters=False)
        errs = validate_pack.check_pack(no_desc)
        assert errs == ["SKILL.md frontmatter missing 'description'"], errs

        # (7) orchestrator shape (SKILL.md + PACK.yaml only) passes
        orch = build_pack(root, "demo-orch", skill=ORCHESTRATOR_SKILL,
                          license_=False, chapters=False)
        assert validate_pack.check_pack(orch) == [], validate_pack.check_pack(orch)

        # (8) orchestrator without PACK.yaml still fails
        orch_np = build_pack(root, "demo-orch-np", skill=ORCHESTRATOR_SKILL,
                             pack_yaml=False, license_=False, chapters=False)
        errs = validate_pack.check_pack(orch_np)
        assert errs == ["missing PACK.yaml"], errs

        # (10) the shared classifier: one window, two kinds, content default
        assert pack_kind.pack_kind(SIGNPOST_SKILL.format(slug="k1")) == "signpost"
        assert pack_kind.pack_kind(ORCHESTRATOR_SKILL.format(slug="k2")) == "orchestrator"
        assert pack_kind.pack_kind(CONTENT_SKILL.format(slug="k3")) == "content"

        # (11) body-planted kind line never classifies (spec P5 AD-1, review I6)
        planted = BODY_PLANTED_SKILL.format(slug="k4")
        assert pack_kind.pack_kind(planted) == "content", planted

        # (12) wrong-case kind never classifies; YAML keys are case-sensitive (AD-2)
        wrong = WRONG_CASE_SKILL.format(slug="k5")
        assert pack_kind.pack_kind(wrong) == "content", wrong

        # (13) both kind lines present: signpost wins (inventory if/elif order, AD-1)
        both = "---\nname: k6\nkind: orchestrator\nkind: signpost\n---\nbody\n"
        assert pack_kind.pack_kind(both) == "signpost", both

        # (14) closing fence as the last line without a trailing newline parses
        tight = "---\nname: k7\nkind: signpost\n---"
        assert pack_kind.pack_kind(tight) == "signpost", tight

        # (15) body-planted kind regression: the pack classifies content, so
        # LICENSE and chapters are required and their absence fails loudly
        # (AD-6 item 1; red until validate_pack stops scanning the body)
        planted_pack = build_pack(root, "planted-pack",
                                  skill=BODY_PLANTED_SKILL,
                                  license_=False, chapters=False)
        errs = validate_pack.check_pack(planted_pack)
        assert errs == ["missing LICENSE (must reproduce the source's terms)",
                        "missing chapters/ directory"], errs

        # (16) wrong-case guard: `Kind: Signpost` in frontmatter classifies
        # content at the check_pack level too (AD-6 item 2)
        wrong_pack = build_pack(root, "wrong-case-pack",
                                skill=WRONG_CASE_SKILL,
                                license_=False, chapters=False)
        errs = validate_pack.check_pack(wrong_pack)
        assert errs == ["missing LICENSE (must reproduce the source's terms)",
                        "missing chapters/ directory"], errs

        # (17) closing fence at EOF: the old `\n---\s*\n` window misparsed a
        # SKILL.md whose fence is the last line; FM_RE handles it (AD-1)
        tight_pack = build_pack(root, "tight-fence-pack",
                                skill="---\nname: {slug}\nkind: signpost\ndescription: x\n---",
                                license_=False, chapters=False)
        assert validate_pack.check_pack(tight_pack) == [], \
            validate_pack.check_pack(tight_pack)

    # (9) the live tree carries the orchestrator stub plus the flipped
    # content pack (read-only). Signpost dirs are excluded from this pin
    # (orchestrator + content packs only; see P2/P4 retarget precedent).
    live = REPO_ROOT / "packs" / "nuclear"
    assert live.is_dir(), f"live orchestrator pack missing: {live}"
    assert validate_pack.check_pack(live) == [], validate_pack.check_pack(live)

    def _is_signpost(d: Path) -> bool:
        skill = d / "SKILL.md"
        if not skill.is_file():
            return False
        return pack_kind.pack_kind(
            skill.read_text(encoding="utf-8", errors="ignore")
        ) == "signpost"

    live_slugs = sorted(
        p.name for p in (REPO_ROOT / "packs").iterdir()
        if p.is_dir() and not _is_signpost(p)
    )
    assert live_slugs == ["nrc-nuclear", "nuclear"], live_slugs

    # (18) live signpost pack passes the structure checks check 5 now runs on
    # it (PACK.yaml mandatory fields, tier validity, slug match, frontmatter
    # name/description); the PACK-SPEC:103 promise on the live tree (AD-6 item 3)
    live_signpost = REPO_ROOT / "packs" / "nuclear-signpost"
    assert live_signpost.is_dir(), f"live signpost pack missing: {live_signpost}"
    assert validate_pack.check_pack(live_signpost) == [], \
        validate_pack.check_pack(live_signpost)

    print("validate_pack tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
