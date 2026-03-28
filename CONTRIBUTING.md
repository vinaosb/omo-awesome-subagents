# Contributing to OMO Awesome Subagents

Thanks for contributing! This repository contains 136 specialized subagent definitions that work with both Oh My OpenAgent (plugin format) and OpenAI Codex (TOML format).

## How to Contribute

### Add a New Subagent

1. Choose the correct category under `categories/`
2. Add a `.toml` file for the new agent
3. Update documentation:
   - `README.md` (main category listing)
   - `categories/<category>/README.md` (category-specific listing)
4. Keep agent names sorted alphabetically within categories
5. Open a PR describing the use case and why this agent is distinct

### Improve an Existing Subagent

1. Keep the role bounded (avoid broad persona text)
2. Preserve the TOML format
3. Update relevant README descriptions if behavior changes
4. Include before/after rationale in your PR
5. **Re-run the converter** to regenerate plugin output

---

## Required Agent Format

Each agent must be a valid TOML file with these required fields:

```toml
name = "agent-name"
description = "When this agent should be invoked"

developer_instructions = """
[Role and expertise description]
[Working mode]
[Focus areas]
[Quality checks]
[Return format]
"""
```

### Optional Fields

| Field | Values | Purpose |
|-------|--------|---------|
| `model` | `gpt-5.4`, `gpt-5.3-codex-spark` | Model selection |
| `model_reasoning_effort` | `low`, `medium`, `high` | Reasoning depth |
| `sandbox_mode` | `read-only`, `workspace-write` | Filesystem access |
| `mcp_servers` | array of strings | MCP server references |

---

## Platform Compatibility

### Oh My OpenAgent (Plugin Format)

After modifying TOML files, regenerate the plugin:

```bash
python convert_toml_to_plugin.py
```

The converter maps TOML fields to plugin markdown format:

| TOML | Plugin |
|------|--------|
| `name` | frontmatter `name` |
| `description` | frontmatter `description` |
| `model` | frontmatter `model` (prefixed with `openai/`) |
| `model_reasoning_effort` | blockquote `> **Reasoning effort: X**` |
| `sandbox_mode = "read-only"` | blockquote `> **Mode: READ-ONLY**` |
| `developer_instructions` | markdown body |

### OpenAI Codex (TOML Format)

TOML files are used directly. No conversion needed.

---

## Authoring Quality Bar

`developer_instructions` should be concrete and task-shaped:

**Recommended structure:**
- Working mode
- Focus on
- Quality checks
- Return format
- Do not... unless explicitly requested

**Avoid:**
- Unsupported tool/platform assumptions
- Generic roleplay text without output contracts
- Scope creep instructions ("always do everything")

---

## Model and Sandbox Guidance

### Model Selection

| Model | Use For |
|-------|---------|
| `gpt-5.4` | Complex reasoning: architecture reviews, security audits, financial logic |
| `gpt-5.3-codex-spark` | Fast scanning, synthesis, lighter research tasks |

### Sandbox Mode

| Mode | Use For |
|------|---------|
| `read-only` | Review/research agents (73 agents) |
| `workspace-write` | Implementation agents (63 agents) |

---

## Validation Checklist

Before submitting a PR:

- [ ] All links in `README.md` and category READMEs resolve
- [ ] New/edited `.toml` files parse correctly (`python convert_toml_to_plugin.py --validate`)
- [ ] Agent `name` is unique across the repository
- [ ] Main README includes the new agent in the correct category
- [ ] Category README includes the new agent
- [ ] Descriptions are concise and accurate
- [ ] Converter script runs without errors (`python convert_toml_to_plugin.py --dry-run`)

---

## Pull Request Checklist

- [ ] Added/updated agent TOML file(s)
- [ ] Updated main `README.md`
- [ ] Updated category `README.md`
- [ ] Verified links and TOML validity
- [ ] Ran converter script successfully
- [ ] Included clear PR description and motivation

---

## Style Notes

- Keep documentation in English
- Prefer precise, practical wording over marketing language
- Keep descriptions short; keep instructions high-signal
- Use consistent formatting across similar agents

---

## License

By contributing, you agree your contributions are provided under the repository's MIT License terms.
