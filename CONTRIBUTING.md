# Contributing to omo-awesome-subagents

This plugin provides 13 flagship subagents and 127 skills for Oh My OpenAgent (OMO) and Opencode. Contributions welcome!

## Prerequisites

- A working OMO or Opencode installation
- Basic familiarity with YAML frontmatter and Markdown
- Understanding of what makes a good agent/skill prompt

## Adding a New Skill

### Step 1: Create the skill directory

```
skills/your-agent-name/
  SKILL.md
```

### Step 2: Write SKILL.md with frontmatter

```markdown
---
name: your-agent-name
description: Use when a task needs [specific capability]. Keep to one sentence.
---

- [focus area 1]
- [focus area 2]
- [focus area 3]

- [quality check 1]
- [quality check 2]
```

### Step 3: Verify your skill

Skills are stored flat in `skills/<skill-name>/SKILL.md`. There are no category subdirectories. Browse the existing skills directory to see naming conventions.

**Note:** Do NOT add agents that overlap with OMO builtins (agent-organizer, context-manager, knowledge-synthesizer, multi-agent-coordinator, reviewer, search-specialist, task-distributor, workflow-orchestrator).

## Adding a Flagship Agent

Flagship agents are the 13 primary callable subagents. These should only be added by maintainers after a skill has proven its value.

### Agent file format

```
agents/your-agent-name.md
```

```markdown
---
name: your-agent-name
description: Use when a task needs [specific capability].
tools: read, grep, glob, lsp_symbols, lsp_diagnostics, lsp_goto_definition,
  lsp_find_references, lsp_prepare_rename, lsp_rename
---

> **Reasoning effort: high**

> **Mode: READ-ONLY** — You must not modify any files. You may only read, analyze, and report findings.

[One paragraph describing the agent's philosophy and approach]

Working mode:
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]

Focus on:
- [area 1]
- [area 2]
- [area 3]

Quality checks:
- [check 1]
- [check 2]
- [check 3]

Return:
- [what the agent returns]
```

**Key rules for flagship agents:**
- Must be READ-ONLY (no file modifications)
- Must include reasoning effort level
- Must have working mode steps (typically 4)
- Must list focus areas and quality checks
- Must define a return format

## Skill vs Agent: When to Use Which

| Use SKILL when | Use AGENT when |
|----------------|----------------|
| Injecting knowledge into an existing session | Task needs a dedicated reasoning session with its own scope |
| Providing context/guidance | Independent analysis or exploration required |

## Style Guidelines

- **Description:** One sentence, starts with "Use when a task needs..."
- **Focus areas:** Actionable, specific, not generic
- **Quality checks:** Verifiable, grounded in concrete outputs
- No emojis in agent/skill files
- Keep descriptions concise (agents should be specialists, not generalists)
- Use American English spelling

## Testing Your Contribution

1. Load the skill locally and verify it injects correctly
2. Test with a real task that matches the skill's domain
3. Verify the frontmatter parses correctly

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Add your skill/agent file
4. Test locally
5. Open a PR with a clear description
6. Wait for review
