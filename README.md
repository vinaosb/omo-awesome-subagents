# omo-awesome-subagents

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Agents](https://img.shields.io/badge/agents-13-green.svg)](#flagship-agents)
[![Skills](https://img.shields.io/badge/skills-127-purple.svg)](#skill-categories)

A collection of 13 flagship subagents and 127 skills for [Oh My OpenAgent (OMO)](https://github.com/nicepkg/OpenAgent) and [Opencode](https://opencode.ai).

## Table of Contents

- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Architecture Overview](#architecture-overview)
- [Flagship Agents](#flagship-agents)
- [Skill Categories](#skill-categories)
- [MCP Servers](#mcp-servers)
- [Excluded Agents](#excluded-agents)
- [File Structure](#file-structure)
- [Troubleshooting](#troubleshooting)

## Quick Start

### Step 1: Clone the repo

```bash
git clone https://github.com/vinaosb/omo-awesome-subagents.git
```

### Step 2: Install agents and skills

**Option A: One-click install (recommended)**

Unix/macOS:
```bash
cd omo-awesome-subagents
chmod +x install.sh
./install.sh
```

Windows (PowerShell):
```powershell
cd omo-awesome-subagents
.\install.ps1
```

This copies all agents and skills to `~/.config/opencode/`. You can override the target directory with the `OPENCODE_DIR` environment variable.

**Option B: Manual install**

Copy the `agents/` and `skills/` directories to your Opencode config directory:

```bash
# Unix/macOS
cp agents/*.md ~/.config/opencode/agents/
cp -r skills/*/ ~/.config/opencode/skills/

# Windows (PowerShell)
Copy-Item agents\*.md ~\.config\opencode\agents\ -Force
Copy-Item skills\* ~\.config\opencode\skills\ -Recurse -Force
```

### Step 3: Restart your Opencode session

Close and reopen your terminal, or restart the OMO service.

### Step 4: Verify installation

Try invoking an agent to confirm the installation:

```
task(subagent_type="code-reviewer", prompt="Review this codebase")
```

## Usage Examples

### Invoking a Flagship Agent

```
task(
    subagent_type="code-reviewer",
    prompt="Review the authentication module for security issues"
)
```

### Using a Skill in a Task

```
task(
    prompt="Refactor this Python module for better testability",
    load_skills=["python-pro"]
)
```

### Direct Skill Load

```
skill("terraform-engineer")
```

### Combining Multiple Skills

```
task(
    prompt="Set up a secure Kubernetes deployment with Terraform",
    load_skills=["kubernetes-specialist", "terraform-engineer"]
)
```

## Architecture Overview

This collection provides two types of content:

**Flagship Agents (13)**: Callable subagents via `task(subagent_type="name")`. Includes 6 reviewer agents (READ-ONLY analysis) and 7 implementer agents (can modify files). All use Opencode's `permission` block to control tool access.

**Skills (127)**: Injectable knowledge modules via `skill("name")` or `load_skills=[...]`. All 13 flagships also have skill equivalents. Skills inherit tool access from the invoking agent.

## Flagship Agents

### Reviewer Agents (READ-ONLY)

These agents analyze and report findings without modifying files. They have `permission: { edit: deny, bash: deny }`.

| Agent | Description |
|-------|-------------|
| `code-reviewer` | Code quality, design clarity, and risk assessment |
| `kubernetes-specialist` | Kubernetes architecture, operations, and debugging |
| `llm-architect` | LLM system design, prompt engineering, and RAG |
| `penetration-tester` | Security testing and vulnerability assessment |
| `security-auditor` | Security audit and compliance assessment |
| `terraform-engineer` | Infrastructure-as-code with Terraform |

### Implementer Agents (Can Modify Files)

These agents can read, analyze, AND implement code changes. They have `permission: { edit: allow, bash: allow }`.

| Agent | Description |
|-------|-------------|
| `blockchain-developer` | Blockchain and smart contract development |
| `cpp-pro` | Production C++ with modern standards |
| `embedded-systems` | Embedded systems and firmware engineering |
| `game-developer` | Game development across engines and platforms |
| `golang-pro` | Production Go with concurrency patterns |
| `mlops-engineer` | ML pipeline design, model deployment, and monitoring |
| `rust-engineer` | Production Rust with safety and performance |

## Skill Categories

These are logical groupings for reference, not directory structures. All skills are stored flat in `skills/<skill-name>/SKILL.md`.

<details>
<summary>View all 10 skill categories</summary>

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

</details>

## MCP Servers

Agents in this collection use Opencode's **built-in tools** (file read/write/edit, grep, glob, LSP, webfetch, bash) automatically — no extra configuration needed.

If you configure additional MCP servers in your `opencode.json` (e.g., Context7 for docs, Sentry for errors, Grep.app for GitHub code search), those tools are **also automatically available** to all agents and skills. This is handled by Opencode's config merging — agents don't need to declare MCP servers themselves.

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
    plugin.json            # Claude plugin manifest (Claude ecosystem only)
  .github/workflows/
    validate.yml           # CI: agent/skill structure validation
  agents/
    *.md                   # 13 flagship agent definitions
  skills/
    <skill-name>/
      SKILL.md             # 127 skill definitions (flat namespace)
  install.sh               # Unix/macOS install script
  install.ps1              # Windows install script
  install-fragment.json    # Package metadata
  CONTRIBUTING.md          # Contribution guide
  CHANGELOG.md             # Version history
  .gitignore
  LICENSE
  README.md
```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Agent not found | Verify files are in `~/.config/opencode/agents/`. Restart Opencode. |
| Agent not recognized | Use the agent name matching the filename: `code-reviewer`, not `code_reviewer` |
| Skills not loading | Verify skill directories are in `~/.config/opencode/skills/`. Each must contain `SKILL.md`. |
| MCP server errors | MCP servers are user-configured in `opencode.json`, not provided by this collection. |
| Permission denied on install.sh | Run `chmod +x install.sh` first |

## License

[MIT License](LICENSE)
