# AGENTS DIRECTORY

## OVERVIEW

13 flagship domain-specialist agent definitions for Opencode. Each is a self-contained markdown file.

## FORMAT

All agents follow this template:

```markdown
---
name: agent-name
description: Use when a task needs [specific capability].
tools: read, grep, glob, ...          # ALWAYS present
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

## AGENT TYPES

- **Reviewer agents** (read-only analysis): code-reviewer, kubernetes-specialist, llm-architect, penetration-tester, security-auditor, terraform-engineer
  - Tools: `read, grep, glob, lsp_symbols, lsp_diagnostics, lsp_goto_definition, lsp_find_references, lsp_prepare_rename, lsp_rename`
  - Include `Mode: READ-ONLY` line
- **Implementer agents** (can modify files): blockchain-developer, cpp-pro, embedded-systems, game-developer, golang-pro, mlops-engineer, rust-engineer
  - Tools: `read, write, edit, grep, glob, bash, lsp_symbols, lsp_diagnostics, lsp_goto_definition, lsp_find_references, lsp_prepare_rename, lsp_rename`
  - No `Mode: READ-ONLY` line (intentional — they implement changes)
- All agents share: evidence-driven philosophy, safety-first approach, smallest-change principle
- No agent cross-references another — each is fully self-contained

## ADDING AN AGENT

See `CONTRIBUTING.md` at repo root. Key rules:
- File: `agents/<name>.md`
- Must include frontmatter with `name` and `description`
- Must follow the Working mode / Focus on / Quality checks / Return structure
- Must end with a "Do not" constraint
