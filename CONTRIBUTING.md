# Contributing to omo-awesome-subagents

This collection provides 13 flagship subagents and 127 skills for Oh My OpenAgent (OMO) and Opencode. Contributions welcome!

## Prerequisites

- A working OMO or Opencode installation
- Basic familiarity with YAML frontmatter and Markdown
- Understanding of what makes a good agent/skill prompt

## Adding a New Skill

### Step 1: Create the skill directory

```
skills/your-skill-name/
  SKILL.md
```

**Naming rules:** Directory name must be lowercase alphanumeric with single hyphens, 1-64 characters. Regex: `^[a-z0-9]+(-[a-z0-9]+)*$`. The directory name must match the `name:` field in the frontmatter.

### Step 2: Write SKILL.md with frontmatter

```markdown
---
name: your-skill-name
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

**Reviewer agent** (read-only analysis):

```markdown
---
description: Use when a task needs [specific capability].
mode: subagent
permission:
  edit: deny
  bash: deny
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

Do not [closing constraint referencing "parent agent"].
```

**Implementer agent** (can modify files):

```markdown
---
description: Use when a task needs [specific capability].
mode: subagent
permission:
  edit: allow
  bash: allow
---

> **Reasoning effort: high**

[One paragraph describing the agent's philosophy and approach]

Working mode:
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]

Focus on:
- [area 1]
- [area 2]

Quality checks:
- [check 1]
- [check 2]

Return:
- [what the agent returns]

Do not [closing constraint referencing "parent agent"].
```

### Key rules for flagship agents

- `description` is REQUIRED — Opencode uses this for agent discovery
- `mode: subagent` is REQUIRED — makes agent invocable by other agents
- `permission` controls tool access — only `edit`, `bash`, `webfetch`, `skill`, `task` are configurable
- All other tools (read, grep, glob, lsp_*) are available by default
- Do NOT use `name:` — Opencode derives the name from the filename
- Do NOT use `tools:` — this field is deprecated, use `permission:` instead
- Must include reasoning effort level
- Must have working mode steps (typically 4)
- Must list focus areas and quality checks
- Must define a return format
- Must end with a "Do not" constraint

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
- Skill body uses dash-prefixed bullets only (no headings)

## Testing Your Contribution

1. Run `install.sh` or `install.ps1` to install locally
2. Load the skill and verify it injects correctly
3. Test with a real task that matches the skill's domain
4. Verify the frontmatter parses correctly

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Add your skill/agent file
4. Test locally
5. Open a PR with a clear description
6. Wait for review
