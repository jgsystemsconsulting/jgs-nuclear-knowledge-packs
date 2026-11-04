<!--
Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Other agents (non-Claude install targets)

Root `install.py` installs every pack under `packs/` into one or more coding agents.
Default target is Claude Code. Use `--list-agents` for the live registry; this page
documents what each non-default path does and how transform installs differ from
native folder copies.

## Quick commands

```bash
python install.py --list-agents         # agents, kind, scope, base path
python install.py --dry-run             # preview only
python install.py                       # Claude Code (native, default)
python install.py --agent openclaw      # one agent
python install.py --agent all           # every user-global agent
python install.py --flat                # native only: drop vendor namespace
python install.py --target DIR          # override install base (single agent)
```

After install, restart the agent and invoke a pack by slug (for example `/nuclear`
or `/<slug> <topic>`). Host slash-command syntax varies; the slug is stable.

## Native vs transform

| Kind | Agents | What lands on disk | Progressive disclosure |
|---|---|---|---|
| **native** | `claude`, `openclaw`, `copilot` | Full pack folder (`SKILL.md`, `chapters/`, extras) | Yes: host can load chapters on demand |
| **transform** | `codex`, `gemini`, `cursor` | One file per pack with the `SKILL.md` **index body inlined** | No: chapters stay in the repo; index-only answers |

Native agents speak the open [agentskills.io](https://github.com/agentskills/agentskills)
`SKILL.md` layout, so the installer copies each pack folder unchanged. Transform agents
use a different prompt/command/rule shape, so the installer writes a single file that
embeds the always-loaded index and a short provenance comment. Chapter files are not
copied into transform targets.

Vendor namespace default for native installs: `jgs-nuclear-knowledge-packs/<slug>/`
under the agent's skills root. Pass `--flat` to install native packs directly under the
skills root. Transform paths do not use that folder layout the same way (see below).

`--agent all` installs every agent marked user-global. Cursor is project-local and is
**excluded** from `all`; run `python install.py --agent cursor` from the project you want
rules in.

## Agent targets

Paths below assume default home layout. `claude` honours `$CLAUDE_CONFIG_DIR` (skills
land under `$CLAUDE_CONFIG_DIR/skills/...`). `--target DIR` overrides the base for a
single agent run.

### Claude Code — `claude` (native, default, user-global)

- Base: `~/.claude/skills/` (or `$CLAUDE_CONFIG_DIR/skills/`)
- Default layout: `.../jgs-nuclear-knowledge-packs/<slug>/` (full tree)
- Flat: `.../<slug>/`

### OpenClaw — `openclaw` (native, user-global)

- Base: `~/.openclaw/skills/`
- Same native copy behaviour and `--flat` rules as Claude.

### GitHub Copilot CLI — `copilot` (native, user-global)

- Base: `~/.copilot/skills/`
- Same native copy behaviour and `--flat` rules as Claude.

### OpenAI Codex CLI — `codex` (transform → prompt)

- Base: `~/.codex/prompts/`
- File: `<slug>.md`
- Content: provenance HTML comment + `SKILL.md` body (frontmatter stripped to body only)
- No vendor subdirectory; one top-level prompt file per pack.

### Gemini CLI — `gemini` (transform → TOML command)

- Base: `~/.gemini/commands/`
- File: `jgs-nuclear-knowledge-packs/<slug>.toml`
- Content: `description` from frontmatter; `prompt` is a triple-quoted string holding the
  provenance comment plus `SKILL.md` body.

### Cursor — `cursor` (transform → project-local rule)

- Base: `./.cursor/rules/` relative to the **current working directory** (not `$HOME`)
- File: `<slug>.mdc`
- Content: MDC frontmatter (`description`, empty `globs`, `alwaysApply: false`), then
  provenance comment + `SKILL.md` body
- Not included in `--agent all`. Run from the project root that should receive the rules.

## Ownership / re-install safety

The installer refuses to overwrite destinations it did not create:

- **Native:** destination must already contain a `PACK.yaml` whose `slug:` matches the
  pack folder name.
- **Transform:** destination file must contain the provenance marker
  `jgs-nuclear-knowledge-packs: '<slug>' transformed for ...`.

On a skip it prints the path and asks you to remove or rename the entry, then re-run.
Dry-run never writes; it still reports would-install / would-skip lines.

## What transform installs cannot do

- They do not ship `chapters/`, `glossary.md`, `patterns.md`, or `cheatsheet.md` into the
  agent directory.
- Answers from a transform install are **index-level** unless the host separately can read
  chapter files from a checkout of this repo.
- The `/nuclear` orchestrator notes the same limit when it only sees inlined indexes.

For full progressive disclosure, use a native agent (`claude`, `openclaw`, or `copilot`)
or keep a local clone available to the host.

## Related docs

- End-user install one-liner: repo [README](../README.md)
- Pack layout and validation: [PACK-SPEC.md](PACK-SPEC.md)
- Runtime usage (invoke, orchestrator, citations): [skill-usage.md](skill-usage.md)
