# AGENTS DIRECTORY

## OVERVIEW

13 flagship domain-specialist agent definitions for Opencode. Each is a self-contained markdown file.

## FORMAT

All agents follow this template:

```markdown
---
description: Use when a task needs [specific capability].
mode: subagent
permission:
  edit: deny    # deny for reviewers, allow for implementers
  bash: deny    # deny for reviewers, allow for implementers
---

> **Reasoning effort: high**
> **Mode: READ-ONLY**                 # Reviewer agents only (6/13)

{Philosophy paragraph}

**Working mode:**
1. {Step}
2. {Step}
3. {Step}
4. {Step}

**Focus on:**
- {bullet}

**Quality checks:**
- {bullet}

**Return:**
- {bullet}

Do not {closing constraint referencing "parent agent"}.
```

**Key frontmatter fields:**
- `description` (REQUIRED): Starts with "Use when a task needs..."
- `mode: subagent`: Makes agents invocable by primary agents and via @ mentions
- `permission`: Controls tool access. Only `edit`, `bash`, `webfetch`, `skill`, `task` are configurable — all other tools (read, grep, glob, lsp_*) are available by default.

**Note:** `name` is NOT used — Opencode derives the agent name from the filename. `tools` is deprecated — use `permission` instead.

## AGENT TYPES

- **Reviewer agents** (read-only analysis): code-reviewer, kubernetes-specialist, llm-architect, penetration-tester, security-auditor, terraform-engineer
  - Permission: `edit: deny`, `bash: deny`
  - Include `Mode: READ-ONLY` line in body
- **Implementer agents** (can modify files): blockchain-developer, cpp-pro, embedded-systems, game-developer, golang-pro, mlops-engineer, rust-engineer
  - Permission: `edit: allow`, `bash: allow`
  - No `Mode: READ-ONLY` line (intentional — they implement changes)
- All agents share: evidence-driven philosophy, safety-first approach, smallest-change principle
- No agent cross-references another — each is fully self-contained

## ADDING AN AGENT

See `CONTRIBUTING.md` at repo root. Key rules:
- File: `agents/<name>.md`
- Must include frontmatter with `description`, `mode`, and `permission`
- Must follow the Working mode / Focus on / Quality checks / Return structure
- Must end with a "Do not" constraint
