#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see ../LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based checks for the .zcode member of SKIP_DIRS in check_release.main().

Run: python tooling/test_check_release_skip_zcode.py
Exit 0 when: the SKIP_DIRS literal includes ".zcode", the comment above it
names maintainer session working state, a seeded leak plus link payload under
.zcode/ and under tooling/.zcode/ is not flagged by a full gate run, and the
identical payload at repo root fails both scans. Seeded files are created and
deleted by this test. Payload strings are built at runtime so this file,
which the gate itself scans, never carries a sentinel or banned URL literal.
"""
from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_release  # noqa: E402

ROOT = check_release.ROOT
GATE = ROOT / "tooling" / "check_release.py"


def skip_dirs_members() -> set[str]:
    tree = ast.parse(GATE.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "SKIP_DIRS" for t in node.targets
        ):
            assert isinstance(node.value, ast.Set), "SKIP_DIRS must stay a set literal"
            return {
                elt.value
                for elt in node.value.elts
                if isinstance(elt, ast.Constant) and isinstance(elt.value, str)
            }
    raise AssertionError("SKIP_DIRS assignment not found in check_release.py")


def payload() -> str:
    sentinel = check_release.LEAK_SENTINELS[0]
    hosts = check_release.load_banned_hosts()
    host = "nrc" + ".gov" if "nrc" + ".gov" in hosts else hosts[0]
    url = "https://www." + host + "/probe-seed"
    return "# probe seed\n\n" + sentinel + "\n\n" + url + "\n"


def run_gate() -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(GATE)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=ROOT,
    )
    return proc.returncode, proc.stdout + proc.stderr


def seeded_run(seed: Path) -> tuple[int, str]:
    made_dirs: list[Path] = []
    d = seed.parent
    while not d.exists():
        made_dirs.append(d)
        d = d.parent
    seed.parent.mkdir(parents=True, exist_ok=True)
    seed.write_text(payload(), encoding="utf-8")
    try:
        return run_gate()
    finally:
        seed.unlink(missing_ok=True)
        for d in made_dirs:
            try:
                d.rmdir()
            except OSError:
                pass


def main() -> int:
    members = skip_dirs_members()
    assert ".zcode" in members, f"SKIP_DIRS missing .zcode member: {sorted(members)}"
    assert ".planning" in members and ".superpowers" in members, (
        "SKIP_DIRS lost an existing member"
    )
    source = GATE.read_text(encoding="utf-8")
    assert "maintainer session working state" in source, (
        "comment above SKIP_DIRS must state .zcode holds maintainer session "
        "working state"
    )

    root_seed = ROOT / ".zcode" / "probe-seed.md"
    _rc, out = seeded_run(root_seed)
    assert "probe-seed.md" not in out, "seeded .zcode/ file was flagged by the gate"

    nested_seed = ROOT / "tooling" / ".zcode" / "probe-seed.md"
    _rc, out = seeded_run(nested_seed)
    assert "probe-seed.md" not in out, "seeded tooling/.zcode/ file was flagged"

    negative_seed = ROOT / "probe-seed-negative.md"
    rc, out = seeded_run(negative_seed)
    assert rc != 0, "negative control outside .zcode/ must fail the gate"
    assert "[leak]" in out and "probe-seed-negative.md" in out, (
        "negative control must trip the leak scan"
    )
    assert "[links]" in out, "negative control must trip the link scan"

    assert not root_seed.exists(), "probe seed left behind under .zcode/"
    assert not nested_seed.exists(), "probe seed left behind under tooling/.zcode/"
    assert not negative_seed.exists(), "negative probe seed left behind at repo root"
    print("test_check_release_skip_zcode: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
