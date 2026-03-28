# PROJECT KNOWLEDGE BASE

**Generated:** 2025-01-26
**Commit:** 1eeb0e6
**Branch:** main

## OVERVIEW

OMO/Opencode agent and skill pack — 13 flagship agents + 127 skills for domain-specific AI assistance. Fork of VoltAgent/awesome-codex-subagents, rebranded for Oh My OpenAgent / Opencode ecosystem.

## STRUCTURE

```
.
├── .claude-plugin/         # Plugin manifest (plugin.json)
├── agents/                 # 13 flagship agent definitions (.md)
├── skills/                 # 127 skill definitions (flat dirs, each with SKILL.md)
├── install-fragment.json   # Opencode config snippet for installation
├── README.md               # User documentation + quick start
├── CONTRIBUTING.md          # Contribution format specs
├── CHANGELOG.md             # Version history
└── LICENSE                  # MIT (copyright VoltAgent)
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Add new agent | `agents/<name>.md` | See CONTRIBUTING.md for format |
| Add new skill | `skills/<name>/SKILL.md` | Flat namespace — no subdirectories |
| Change plugin metadata | `.claude-plugin/plugin.json` | 8-line manifest |
| Installation instructions | `install-fragment.json` | Uses `<REPO_ROOT>` placeholder |
| User-facing docs | `README.md` | Quick start, usage examples, architecture |

## CONVENTIONS

- **No code** — entirely declarative markdown + JSON
- **Flat skill namespace** — `skills/<name>/SKILL.md`, never nested in category dirs
- Agent/skill duplication is intentional — each flagship agent has a matching skill dir
- Categories (Core Development, Language Specialists, etc.) are logical groupings in README only
- Opencode built-in tools (read, write, grep, bash, etc.) are auto-available — never declare them

## ANTI-PATTERNS (THIS PROJECT)

- Do NOT create category subdirectories under `skills/` — flat only
- Do NOT add `mcpServers` to plugin.json — MCP is user-configured in `opencode.json`
- Do NOT reference "Codex" or "OpenAI Codex" — this is OMO/Opencode-only
- Do NOT cross-reference between agent files — each is self-contained

## UNIQUE STYLES

- Agent frontmatter: `name`, `description`, `tools` (always present)
- Reviewer agents (6): `tools: read, grep, glob, lsp_*` + `Mode: READ-ONLY`
- Implementer agents (7): `tools: read, write, edit, grep, glob, bash, lsp_*` (no Mode line)
- Agent body: philosophy paragraph → `Working mode:` (4 steps) → `Focus on:` → `Quality checks:` → `Return:` → `Do not` constraint
- Skill frontmatter: `name`, `description` only (never `tools`)
- Skill body: dash-prefixed bullets for focus areas + quality checks

## KNOWN ISSUES

- None currently tracked

## NOTES

- `install-fragment.json` uses `<REPO_ROOT>` — users must replace with their clone path
- LICENSE copyright remains "VoltAgent" (correct for MIT fork attribution)
- `.sisyphus/` is gitignored working directory — not part of the plugin
