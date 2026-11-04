#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""slug confinement regression for build_pack.main (spec P9, AD-3/AD-4).

Run:  python -X utf8 -I tooling/test_build_pack.py
Exits 0 when every hostile slug returns non-zero, prints ERROR to stderr, and
creates nothing under the temporary root, and one clean kebab slug returns 0
and creates packs/<slug>/PACK.yaml, packs/<slug>/LICENSE, and
packs/<slug>/chapters/. build_pack.REPO_ROOT is rebound to a fresh
TemporaryDirectory per case, so no run writes the live packs/ tree. The
backslash cases are the Windows traversal shape; a literal absolute slug is
never fed here, because before the guard exists it would write at the drive
root instead of inside the temporary root. No pytest, no CI wiring.
"""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pack  # noqa: E402

CLEAN_SLUG = "clean-pack-1"
HOSTILE_SLUGS = ["../evil", "foo/bar", r"..\evil", r"foo\bar", "a--b"]


def _argv(slug: str) -> list[str]:
    """Full valid argv for build_pack.main; element 0 is the program name."""
    return [
        "build_pack.py",
        "--slug", slug,
        "--title", "Probe Title",
        "--publisher", "Probe Publisher",
        "--version", "v1",
        "--license", "Public Domain",
        "--tier", "1",
    ]


def _run(slug: str, root: Path) -> tuple[int, str]:
    build_pack.REPO_ROOT = root
    err = io.StringIO()
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
        code = build_pack.main(_argv(slug))
    return code, err.getvalue()


def main() -> int:
    # (1) hostile slugs: non-zero exit, ERROR naming the slug on stderr, and
    # nothing created anywhere under the temporary root
    for slug in HOSTILE_SLUGS:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            code, err = _run(slug, root)
            assert code != 0, f"hostile slug accepted: {slug!r}"
            assert "ERROR" in err and slug in err, (
                f"no ERROR line naming {slug!r} on stderr: {err!r}"
            )
            assert list(root.rglob("*")) == [], (
                f"hostile slug {slug!r} wrote: {list(root.rglob('*'))}"
            )

    # (2) clean control: exit 0 and the expected scaffold tree
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        code, err = _run(CLEAN_SLUG, root)
        assert code == 0, err
        pack = root / "packs" / CLEAN_SLUG
        assert (pack / "PACK.yaml").is_file(), "PACK.yaml missing"
        assert (pack / "LICENSE").is_file(), "LICENSE missing"
        assert (pack / "chapters").is_dir(), "chapters/ missing"
        assert f"slug: {CLEAN_SLUG}" in (pack / "PACK.yaml").read_text(
            encoding="utf-8"
        ), "PACK.yaml does not carry the clean slug"

    print("build_pack tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
