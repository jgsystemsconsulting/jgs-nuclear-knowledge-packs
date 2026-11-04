#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""href-attribute escape regression for gen_packs_page.render (spec P6, AD-3/AD-4).

Run:  python -X utf8 -I tooling/test_gen_packs_page.py
Exits 0 when a quote- and ampersand-bearing SKILLS.md link target cannot break
out of the double-quoted href attribute (html.escape(..., quote=True) at the
href build in tooling/gen_packs_page.py) and a clean path emits the exact
current URL unchanged. Rows are constructed in parse_skills() output shape
(slug, path, licence, desc); no full-page equality assert, which is check 5c's
job (tooling/check_release.py:1027-1029). render() reads the BRAND-TOKENS
block from the live docs/index.html, so a broken marker block surfaces here
as an error before it reaches the generator. No pytest, no CI wiring.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_packs_page  # noqa: E402

BLOB_BASE = (
    "https://github.com/jgsystemsconsulting/"
    "jgs-nuclear-knowledge-packs/blob/main/"
)
HOSTILE_PATH = 'packs/hostile"/x&y/SKILL.md'
CLEAN_PATH = "packs/nuclear/SKILL.md"


def _row(slug: str, path: str) -> dict:
    """One row in parse_skills() output shape."""
    return {"slug": slug, "path": path, "licence": "MIT", "desc": "Probe row."}


def main() -> int:
    out = gen_packs_page.render(
        [_row("hostile-pack", HOSTILE_PATH), _row("clean-control", CLEAN_PATH)],
        "0.0.0",
    )

    # (0) both constructed rows rendered; a future render change that silently
    # skips rows must fail here first
    assert out.count("<tr data-text=") == 2, out.count("<tr data-text=")

    # (1) hostile row: the href attribute carries the escaped entities end to end
    assert (
        f'<a href="{BLOB_BASE}packs/hostile&quot;/x&amp;y/SKILL.md">hostile-pack</a>'
        in out
    ), "hostile path not fully escaped inside the href attribute"

    # (2) no raw quote from the path survives: a raw " after packs/hostile would
    # close the attribute early and rewrite the row's markup
    assert 'packs/hostile"' not in out, "raw quote survived in the href"

    # (3) no raw ampersand from the path survives unescaped
    assert "x&y/" not in out, "raw ampersand survived in the href"

    # (4) clean control: the exact current URL, no entities introduced
    assert (
        f'<a href="{BLOB_BASE}packs/nuclear/SKILL.md">clean-control</a>' in out
    ), "clean path must emit the exact current URL unchanged"

    print("gen_packs_page tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
