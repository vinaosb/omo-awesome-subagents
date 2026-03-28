# omo-awesome-subagents

A collection of 13 flagship subagents and 127 skills for Oh My OpenAgent (OMO) and Opencode.

## Quick Start

### Step 1: Clone the repo

```bash
git clone https://github.com/vinaosb/omo-awesome-subagents.git
```

### Step 2: Register the plugin

Copy this into your OMO plugin config (`~/.claude/plugins/installed_plugins.json`):

**Windows example:**
```json
{
  "name": "omo-awesome-subagents",
  "marketplace": "local",
  "scope": "local",
  "version": "1.0.0",
  "installPath": "C:\\Users\\you\\omo-awesome-subagents",
  "lastUpdated": "2026-03-27T05:45:31.608161+00:00"
}
```

**macOS/Linux example:**
```json
{
  "name": "omo-awesome-subagents",
  "marketplace": "local",
  "scope": "local",
  "version": "1.0.0",
  "installPath": "/home/you/omo-awesome-subagents",
  "lastUpdated": "2026-03-27T05:45:31.608161+00:00"
}
```

Replace the `installPath` with your actual clone location. The `install-fragment.json` file in this repo uses `<REPO_ROOT>` as a placeholder.

### Step 3: Restart your OMO/Opencode session

Close and reopen your terminal, or restart the OMO service.

### Step 4: Verify installation

Try invoking an agent to confirm the plugin loaded:

```
task(subagent_type="omo-awesome-subagents:code-reviewer", prompt="Review this codebase")
```

## Usage Examples

### Invoking a Flagship Agent

```
task(
    subagent_type="omo-awesome-subagents:code-reviewer",
    prompt="Review the authentication module for security issues"
)
```

### Using a Skill in a Task

```
task(
    prompt="Refactor this Python module for better testability",
    load_skills=["omo-awesome-subagents:python-pro"]
)
```

### Direct Skill Load

```
skill("omo-awesome-subagents:terraform-engineer")
```

### Combining Multiple Skills

```
task(
    prompt="Set up a secure Kubernetes deployment with Terraform",
    load_skills=["omo-awesome-subagents:kubernetes-specialist", "omo-awesome-subagents:terraform-engineer"]
)
```

## Architecture Overview

This plugin provides two types of content:

**Flagship Agents (13)**: Callable subagents via `task(subagent_type="omo-awesome-subagents:name")`. Each is a READ-ONLY specialist with focused tools for deep analysis and recommendations.

**Skills (127)**: Injectable knowledge modules via `skill("omo-awesome-subagents:name")` or `load_skills=[...]`. All 13 flagships also have skill equivalents.

## Flagship Agents

| Agent | Description |
|-------|-------------|
| `blockchain-developer` | Blockchain and smart contract development |
| `code-reviewer` | Code quality, design clarity, and risk assessment |
| `cpp-pro` | Production C++ with modern standards |
| `embedded-systems` | Embedded systems and firmware engineering |
| `game-developer` | Game development across engines and platforms |
| `golang-pro` | Production Go with concurrency patterns |
| `kubernetes-specialist` | Kubernetes architecture, operations, and debugging |
| `llm-architect` | LLM system design, prompt engineering, and RAG |
| `mlops-engineer` | ML pipeline design, model deployment, and monitoring |
| `penetration-tester` | Security testing and vulnerability assessment |
| `rust-engineer` | Production Rust with safety and performance |
| `security-auditor` | Security audit and compliance assessment |
| `terraform-engineer` | Infrastructure-as-code with Terraform |

## Skill Categories

These are logical groupings for reference, not directory structures. All skills are stored flat in `skills/<skill-name>/SKILL.md`.

| Category | Description | Example Skills |
|----------|-------------|----------------|
| Core Development | Core programming and software design | `python-pro`, `javascript-pro`, `refactoring-specialist` |
| Language Specialists | Programming language experts | `rust-engineer`, `golang-pro`, `swift-expert` |
| Infrastructure | Cloud, DevOps, and platform engineering | `kubernetes-specialist`, `terraform-engineer`, `docker-expert` |
| Quality and Security | Testing, security, and code quality | `security-auditor`, `penetration-tester`, `qa-expert` |
| Data and AI | Data engineering, ML, and AI | `llm-architect`, `mlops-engineer`, `data-scientist` |
| Developer Experience | Tooling and DX optimization | `dx-optimizer`, `debugger`, `tooling-engineer` |
| Specialized Domains | Domain-specific expertise | `blockchain-developer`, `game-developer`, `embedded-systems` |
| Business and Product | Product and business roles | `product-manager`, `business-analyst`, `ux-researcher` |
| Meta and Orchestration | Agent coordination and workflows | `incident-responder`, `error-coordinator` |
| Research and Analysis | Research and analysis tasks | `docs-researcher`, `competitive-analyst`, `trend-analyst` |

## MCP Servers

Agents in this plugin use Opencode's **built-in tools** (file read/write/edit, grep, glob, LSP, webfetch, bash) automatically — no extra configuration needed.

If you configure additional MCP servers in your `opencode.json` (e.g., Context7 for docs, Sentry for errors, Grep.app for GitHub code search), those tools are **also automatically available** to all plugin agents and skills. This is handled by Opencode's config merging — plugins don't need to declare MCP servers themselves.

## Excluded Agents

The following 8 agents are excluded due to overlap with OMO builtins:

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
omo-awesome-subagents/
  .claude-plugin/
    plugin.json          # Plugin manifest
  agents/
    *.md                 # 13 flagship agent definitions
  skills/
    agent-name/
      SKILL.md           # 127 skill definitions
  .gitignore
  LICENSE
  README.md
  install-fragment.json  # Template for plugin registration
```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Plugin not found | Check `installPath` is the correct absolute path. Restart OMO. |
| Agent not recognized | Use the full namespace: `omo-awesome-subagents:agent-name` |
| MCP server errors | Remove the MCP entry from your `opencode.json`. MCP servers are user-configured, not plugin-provided. |
| Skills not loading | Verify the plugin is registered in `installed_plugins.json` |

## License

MIT License
