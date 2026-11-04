#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""render_md header seed defense regression (spec P11, AD-4).

Run:  python -X utf8 -I tooling/test_generate_capability_map.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_capability_map as g  # noqa: E402

MAP = {
    "clusters": [
        {
            "name": "Probe",
            "chapters": [
                {"pack": "p", "chapter": "c.md", "note": "w"},
            ],
        }
    ]
}


def main() -> int:
    canon = g.CANONICAL_LIVE_HEADER.rstrip("\n")
    seeds = [
        "Empty-tree template seed: no content packs yet.\n",
        "Changelog (v0.1.0): empty-tree template seed.\n",
        "x\nno content packs yet\ny\n",
    ]
    for seed in seeds:
        out = g.render_md(MAP, seed)
        low = out.casefold()
        assert "empty-tree template seed" not in low, seed
        assert "no content packs yet" not in low, seed
        assert out.startswith(canon), out[:80]

    clean = "# Author header\n\nKeep me.\n"
    out = g.render_md(MAP, clean)
    assert out.startswith(clean.rstrip("\n")), out[:80]
    assert "## Summary" in out
    assert "| **Total** | **1** |" in out

    print("generate_capability_map tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
