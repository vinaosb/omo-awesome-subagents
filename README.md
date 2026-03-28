# omo-awesome-subagents Plugin

A collection of **13 flagship subagents + 127 skills** for Oh My OpenAgent (OMO) and Opencode.

## Quick Start

1. Clone this repository
2. Register the plugin in your OMO/Opencode configuration:
   ```json
   {
     "omo-awesome-subagents": {
       "path": "/path/to/omo-awesome-subagents",
       "enabled": true
     }
   }
   ```
3. Restart your OMO/Opencode session

## Architecture Overview

This plugin provides two distinct types of agent definitions:

- **Flagship Agents** (13): Callable subagents invoked via `task(subagent_type="omo-awesome-subagents:name")`. These are the most powerful and commonly-used agents, each with full reasoning capabilities.

- **Skills** (127): Injectable knowledge modules loaded via `skill("omo-awesome-subagents:name")` or `load_skills=["omo-awesome-subagents:name"]` in task configurations. Skills provide specialized instructions without spawning separate agents.

All flagship agents ALSO have skill versions available, giving you flexibility in how you use them.

## Flagship Agents

The 13 flagship agents are the primary callable subagents:

- `blockchain-developer`
- `code-reviewer`
- `cpp-pro`
- `embedded-systems`
- `game-developer`
- `golang-pro`
- `kubernetes-specialist`
- `llm-architect`
- `mlops-engineer`
- `penetration-tester`
- `rust-engineer`
- `security-auditor`
- `terraform-engineer`

## Skill Companions

All 127 agents (including the 13 flagships) are available as skills. Skills are useful when you want to inject specialized knowledge into an existing agent session rather than spawning a new subagent.

Load a skill in your task configuration:
```
task(
    prompt="...",
    load_skills=["omo-awesome-subagents:python-pro"]
)
```

## Installation

1. Copy the contents of `install-fragment.json` into the `installed_plugins` array in `~/.claude/plugins/installed_plugins.json`.
2. Restart oh-my-openagent. The plugin loader will discover the agents automatically.

Alternatively, place the entire repository directory where your plugin loader expects it and register it manually.

## Agent Namespacing

All agents are namespaced under the plugin name:

```
omo-awesome-subagents:agent-name
```

For example: `omo-awesome-subagents:api-designer`, `omo-awesome-subagents:python-pro`.

## Categories

The 127 skills span 10 categories:

- `01-core-development`
- `02-language-specialists`
- `03-infrastructure`
- `04-quality-security`
- `05-data-ai`
- `06-developer-experience`
- `07-specialized-domains`
- `08-business-product`
- `09-meta-orchestration`
- `10-research-analysis`

## Category Mapping

| OMO Category | Example Agents |
|--------------|----------------|
| deep | api-designer, python-pro, frontend-developer |
| deep | rust-engineer, cpp-pro, golang-pro |
| deep | kubernetes-specialist, terraform-engineer, incident-responder |
| deep | security-auditor, code-reviewer, penetration-tester |
| ultrabrain | llm-architect, mlops-engineer, data-analyst |
| deep | documentation-specialist, performance-optimizer, accessibility-specialist |
| deep | blockchain-developer, embedded-systems, game-developer |
| writing | product-manager, technical-writer, ux-researcher |
| unspecified-high | agent-organizer (excluded), workflow-orchestrator (excluded) |
| unspecified-high | docs-researcher, browser-debugger, patent-analyst |

## MCP Servers

This plugin includes 2 MCP servers:

- **`openaiDeveloperDocs`**: Connects to OpenAI developer documentation for API reference lookup
- **`chrome_devtools`**: Chrome DevTools protocol for browser debugging and automation

## Excluded Agents

The following 8 agents are excluded as they overlap with oh-my-openagent builtins:

- `agent-organizer`
- `context-manager`
- `knowledge-synthesizer`
- `multi-agent-coordinator`
- `reviewer`
- `search-specialist`
- `task-distributor`
- `workflow-orchestrator`

## File Structure

```
.claude-plugin/
  plugin.json          # Plugin manifest (includes MCP servers)
agents/
  agent-name.md        # 13 flagship agent files
skills/
  agent-name/
    SKILL.md           # 127 skill files
README.md
install-fragment.json
```

## License

[MIT License](LICENSE)
