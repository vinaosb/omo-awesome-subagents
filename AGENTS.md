# PROJECT KNOWLEDGE BASE

**Generated:** 2026-03-28
**Commit:** cf6d208
**Branch:** main

## OVERVIEW

OMO/Opencode agent and skill pack — 13 flagship agents + 127 skills for domain-specific AI assistance. Fork of VoltAgent/awesome-codex-subagents, rebranded for Oh My OpenAgent / Opencode ecosystem.

## STRUCTURE

```
.
├── .claude-plugin/         # Plugin manifest (Claude ecosystem only)
├── agents/                 # 13 flagship agent definitions (.md)
│   └── AGENTS.md           # Agent format documentation
├── skills/                 # 127 skill definitions (flat dirs, each with SKILL.md)
│   └── AGENTS.md           # Skill format documentation
├── install.sh              # Unix/macOS install script
├── install.ps1             # Windows install script
├── install-fragment.json   # Package metadata
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
| Change plugin metadata | `.claude-plugin/plugin.json` | Claude ecosystem only |
| Install agents/skills | `install.sh` or `install.ps1` | Copies to `~/.config/opencode/` |
| User-facing docs | `README.md` | Quick start, usage examples, architecture |

## CONVENTIONS

- **No code** — entirely declarative markdown + JSON
- **Flat skill namespace** — `skills/<name>/SKILL.md`, never nested in category dirs
- Agent/skill duplication is intentional — each flagship agent has a matching skill dir
- Categories (Core Development, Language Specialists, etc.) are logical groupings in README only
- Opencode built-in tools (read, write, grep, bash, etc.) are auto-available — never declare them
- **Skill naming** — must match `^[a-z0-9]+(-[a-z0-9]+)*$` (no dots, no underscores)

## ANTI-PATTERNS (THIS PROJECT)

- Do NOT create category subdirectories under `skills/` — flat only
- Do NOT add `mcpServers` to plugin.json — MCP is user-configured in `opencode.json`
- Do NOT reference "Codex" or "OpenAI Codex" — this is OMO/Opencode-only
- Do NOT cross-reference between agent files — each is self-contained
- Do NOT use dots in skill directory names — use hyphens instead (e.g., `4-8` not `4.8`)

## UNIQUE STYLES

- Agent frontmatter: `description`, `permission` block, `mode: subagent` (always present)
- Reviewer agents (6): `permission: { edit: deny, bash: deny }` + `Mode: READ-ONLY`
- Implementer agents (7): `permission: { edit: allow, bash: allow }` (no Mode line)
- Agent body: philosophy paragraph → `Working mode:` (4 steps) → `Focus on:` → `Quality checks:` → `Return:` → `Do not` constraint
- Skill frontmatter: `name`, `description` only (never `tools` or `permission`)
- Skill body: dash-prefixed bullets for focus areas + quality checks (no headings within body)

## KNOWN ISSUES

- None currently tracked

## NOTES

- `install.sh` / `install.ps1` copy agents and skills to `~/.config/opencode/` (override with `OPENCODE_DIR` env var)
- `.claude-plugin/` is retained for Claude ecosystem backward compatibility — not used by Opencode
- LICENSE copyright remains "VoltAgent" (correct for MIT fork attribution)
- `.sisyphus/` is gitignored working directory — not part of the plugin
