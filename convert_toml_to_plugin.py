#!/usr/bin/env python3
"""
convert_toml_to_plugin.py - Convert TOML agent definitions into an oh-my-openagent plugin.

Reads all .toml files from categories/ subdirectories and produces:
  plugin-output/
    .claude-plugin/plugin.json
    agents/{name}.md  (13 flagship files)
    skills/{name}/SKILL.md  (127 skill files)
    README.md
    install-fragment.json

Usage:
  python convert_toml_to_plugin.py             # full generation
  python convert_toml_to_plugin.py --dry-run   # preview without writing
  python convert_toml_to_plugin.py --validate  # check existing output integrity
"""

import argparse
import json
import re
import shutil
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
CATEGORIES_DIR = SCRIPT_DIR / "categories"
OUTPUT_DIR = SCRIPT_DIR / "plugin-output"
AGENTS_DIR = OUTPUT_DIR / "agents"
PLUGIN_DIR = OUTPUT_DIR / ".claude-plugin"

EXPECTED_AGENT_COUNT = 136

# New constants added for plugin enhancement
FLAGSHIP_AGENTS = frozenset(
    [
        "rust-engineer",
        "cpp-pro",
        "golang-pro",
        "kubernetes-specialist",
        "terraform-engineer",
        "security-auditor",
        "code-reviewer",
        "penetration-tester",
        "llm-architect",
        "mlops-engineer",
        "blockchain-developer",
        "embedded-systems",
        "game-developer",
    ]
)

EXCLUDED_AGENTS = frozenset(
    [
        "agent-organizer",
        "multi-agent-coordinator",
        "task-distributor",
        "workflow-orchestrator",
        "reviewer",
        "search-specialist",
        "context-manager",
        "knowledge-synthesizer",
    ]
)

CONSOLIDATION_MAP = {"incident-responder": "devops-incident-responder"}

READ_ONLY_TOOLS = (
    "read, grep, glob, lsp_symbols, lsp_diagnostics, lsp_goto_definition, "
    "lsp_find_references, lsp_prepare_rename, lsp_rename"
)

TOML_TO_OMO_CATEGORY = {
    "01-core-development": "deep",
    "02-language-specialists": "deep",
    "03-infrastructure": "deep",
    "04-quality-security": "deep",
    "05-data-ai": "ultrabrain",
    "06-developer-experience": "deep",
    "07-specialized-domains": "deep",
    "08-business-product": "writing",
    "09-meta-orchestration": "unspecified-high",
    "10-research-analysis": "unspecified-high",
}

EXPECTED_FLAGSHIP_COUNT = 13
EXPECTED_SKILL_COUNT = 127
SKILLS_DIR = OUTPUT_DIR / "skills"

CATEGORY_DIRS = [
    "01-core-development",
    "02-language-specialists",
    "03-infrastructure",
    "04-quality-security",
    "05-data-ai",
    "06-developer-experience",
    "07-specialized-domains",
    "08-business-product",
    "09-meta-orchestration",
    "10-research-analysis",
]

PLUGIN_JSON = {
    "name": "omo-awesome-subagents",
    "version": "1.0.0",
    "description": (
        "13 flagship subagents + 127 skills for oh-my-openagent, "
        "converted from omo-awesome-subagents Codex collection"
    ),
    "author": "omo-awesome",
    "mcpServers": {},
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_toml(path: Path) -> dict:
    """Read a TOML file and return the parsed dict."""
    with path.open("rb") as f:
        return tomllib.load(f)


def build_model_field(raw_model: str) -> str:
    """Add openai/ prefix to the model name."""
    return f"openai/{raw_model}"


def build_directive_block(reasoning_effort: str | None, sandbox_mode: str | None) -> str:
    """Build the blockquote directive block that goes at the top of the prompt body."""
    parts: list[str] = []

    if reasoning_effort:
        parts.append(f"> **Reasoning effort: {reasoning_effort}**")

    if sandbox_mode == "read-only":
        parts.append(
            "> **Mode: READ-ONLY** — You must not modify any files. "
            "You may only read, analyze, and report findings."
        )

    if parts:
        return "\n\n".join(parts) + "\n\n"
    return ""


def build_markdown(data: dict, sandbox_mode: str | None = None) -> str:
    """Convert a parsed TOML dict into the final .md file content."""
    frontmatter = {
        "name": data["name"],
        "description": data["description"],
    }
    if sandbox_mode == "read-only":
        frontmatter["tools"] = READ_ONLY_TOOLS

    fm_yaml = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True).rstrip("\n")

    directive = build_directive_block(
        data.get("model_reasoning_effort"),
        data.get("sandbox_mode"),
    )

    instructions = data.get("developer_instructions", "").strip()

    body = f"{directive}{instructions}"

    return f"---\n{fm_yaml}\n---\n\n{body}\n"


def build_install_fragment() -> dict:
    """Build the install-fragment.json content."""
    return {
        "name": "omo-awesome-subagents",
        "marketplace": "local",
        "scope": "local",
        "version": "1.0.0",
        "installPath": str(OUTPUT_DIR).replace("/", "\\"),
        "lastUpdated": datetime.now(timezone.utc).isoformat(),
    }


def extract_skill_body(instructions: str) -> str:
    """Extract the actionable skill body from developer_instructions.

    Pulls "Focus on" and "Quality checks" / "Implementation checks" sections,
    strips their heading lines, and keeps the bullet content.  Falls back to the
    full instructions (with a stderr warning) when no sections are found.
    """
    _FOCUS_RE = re.compile(
        r"(?i)^Focus on:.*?(?=^(?:Quality|Implementation|Return|Do not)\b|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    _CHECKS_RE = re.compile(
        r"(?i)^(?:Quality|Implementation) checks?:.*?(?=^(?:Return|Do not)\b|\Z)",
        re.MULTILINE | re.DOTALL,
    )

    sections: list[str] = []

    for focus_match in _FOCUS_RE.finditer(instructions):
        # Strip the heading line ("Focus on:") and keep the rest
        lines = focus_match.group(0).strip().splitlines()
        content = "\n".join(lines[1:]).strip()
        if content:
            sections.append(content)

    for checks_match in _CHECKS_RE.finditer(instructions):
        lines = checks_match.group(0).strip().splitlines()
        content = "\n".join(lines[1:]).strip()
        if content:
            sections.append(content)

    body = "\n\n".join(s for s in sections if s)

    if not body:
        print(
            "[warn] extract_skill_body: no Focus/Quality/Implementation sections found, "
            "using full developer_instructions as fallback",
            file=sys.stderr,
        )
        body = instructions.strip()

    # Truncate at paragraph boundary if body exceeds 1200 words
    words = body.split()
    if len(words) > 1200:
        truncated = " ".join(words[:1200])
        # Find last paragraph break
        last_para = truncated.rfind("\n\n")
        if last_para > 0:
            truncated = truncated[:last_para]
        body = truncated.rstrip() + "\n\n(truncated)"

    return body


def build_skill_md(name: str, description: str, skill_body: str) -> str:
    """Build a skill .md file with YAML frontmatter and raw markdown body."""
    frontmatter = {
        "name": name,
        "description": description,
    }
    fm_yaml = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True).rstrip("\n")
    return f"---\n{fm_yaml}\n---\n\n{skill_body}\n"


def build_readme(
    categories: list[str],
    agent_names: list[str],
    flagship_names: list[str],
    skill_names: list[str],
    category_map: dict[str, str],
) -> str:
    """Generate the README.md content."""
    cat_list = "\n".join(f"- `{c}`" for c in categories)
    flagship_list = "\n".join(f"- `{name}`" for name in flagship_names)
    excluded_list = "\n".join(f"- `{name}`" for name in sorted(EXCLUDED_AGENTS))

    # Category mapping table with example agents
    category_examples = {
        "01-core-development": "api-designer, python-pro, frontend-developer",
        "02-language-specialists": "rust-engineer, cpp-pro, golang-pro",
        "03-infrastructure": "kubernetes-specialist, terraform-engineer, incident-responder",
        "04-quality-security": "security-auditor, code-reviewer, penetration-tester",
        "05-data-ai": "llm-architect, mlops-engineer, data-analyst",
        "06-developer-experience": "documentation-specialist, performance-optimizer, accessibility-specialist",
        "07-specialized-domains": "blockchain-developer, embedded-systems, game-developer",
        "08-business-product": "product-manager, technical-writer, ux-researcher",
        "09-meta-orchestration": "agent-organizer (excluded), workflow-orchestrator (excluded)",
        "10-research-analysis": "docs-researcher, browser-debugger, patent-analyst",
    }

    cat_table_rows = [
        "| TOML Category | OMO Category | Example Agents |",
        "|---------------|--------------|----------------|",
    ]
    for toml_cat in categories:
        omo_cat = category_map.get(toml_cat, "unspecified")
        examples = category_examples.get(toml_cat, "")
        cat_table_rows.append(f"| {toml_cat} | {omo_cat} | {examples} |")
    cat_table = "\n".join(cat_table_rows)

    return f"""\
# omo-awesome-subagents Plugin

A collection of **13 flagship subagents + 127 skills** for Oh My OpenAgent (OMO), converted from the omo-awesome-subagents Codex collection.

## Architecture Overview

This plugin provides two distinct types of agent definitions:

- **Flagship Agents** (13): Callable subagents invoked via `task(subagent_type="omo-awesome-subagents:name")`. These are the most powerful and commonly-used agents, each with full reasoning capabilities.

- **Skills** (127): Injectable knowledge modules loaded via `skill("omo-awesome-subagents:name")` or `load_skills=["omo-awesome-subagents:name"]` in task configurations. Skills provide specialized instructions without spawning separate agents.

All flagship agents ALSO have skill versions available, giving you flexibility in how you use them.

## Flagship Agents

The 13 flagship agents are the primary callable subagents:

{flagship_list}

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

Alternatively, place the entire `plugin-output/` directory where your plugin loader expects it and register it manually.

## Agent Namespacing

All agents are namespaced under the plugin name:

```
omo-awesome-subagents:agent-name
```

For example: `omo-awesome-subagents:api-designer`, `omo-awesome-subagents:python-pro`.

## Categories

The 127 skills span 10 categories:

{cat_list}

## Category Mapping

TOML categories map to OMO categories as follows:

{cat_table}

## MCP Servers

This plugin includes 2 MCP servers:

- **`openaiDeveloperDocs`**: Connects to OpenAI developer documentation for API reference lookup
- **`chrome_devtools`**: Chrome DevTools protocol for browser debugging and automation

## Excluded Agents

The following 8 agents are excluded as they overlap with oh-my-openagent builtins:

{excluded_list}

## Embedded Prompt Directives

Two TOML fields are converted into blockquote directives at the top of each agent's prompt body (rather than frontmatter fields):

- **`model_reasoning_effort`**: Rendered as `> **Reasoning effort: {{value}}**` at the start of the prompt. Tells the model how much deliberation to apply.
- **`sandbox_mode`**: When set to `read-only`, rendered as `> **Mode: READ-ONLY** - You must not modify any files. You may only read, analyze, and report findings.` This enforces analysis-only behavior through the system prompt.

Agents with `sandbox_mode = "workspace-write"` receive no directive (full workspace access is the default).

## File Structure

```
plugin-output/
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

## Regenerating

Run the converter script to regenerate the plugin output from the source TOML files:

```bash
python convert_toml_to_plugin.py            # full generation
python convert_toml_to_plugin.py --dry-run   # preview without writing
python convert_toml_to_plugin.py --validate  # check existing output integrity
```

The script is idempotent: re-running cleans and regenerates all output.
"""


# ---------------------------------------------------------------------------
# Agent classification and MCP extraction
# ---------------------------------------------------------------------------


def extract_mcp_servers(toml_data: dict, source_path: Path) -> dict | None:
    """Extract MCP server definitions from a parsed TOML agent dict.

    Returns ``{"server_name": {"url": "...", ...}}`` or *None* when the
    agent defines no ``[mcp_servers]`` table.  An optional
    ``startup_timeout_sec`` key is included only when the source entry
    provides one.  Entries that lack a ``url`` field are skipped with a
    stderr warning.
    """
    raw = toml_data.get("mcp_servers")
    if raw is None:
        return None

    servers: dict[str, dict] = {}
    for name, entry in raw.items():
        url = entry.get("url")
        if not url:
            print(
                f"WARNING: MCP server '{name}' in {source_path} has no url — skipped",
                file=sys.stderr,
            )
            continue
        server: dict[str, object] = {"url": url}
        timeout = entry.get("startup_timeout_sec")
        if timeout is not None:
            server["startup_timeout_sec"] = timeout
        servers[name] = server

    return servers if servers else None


def merge_agent_toml(primary: dict, absorbed: dict) -> dict:
    """Merge *absorbed* agent TOML data into *primary*.

    Only ``developer_instructions`` are merged (concatenated with a
    separator).  All other top-level fields (``name``, ``description``,
    ``model``, ``model_reasoning_effort``, ``sandbox_mode``) are kept
    from *primary* unchanged.
    """
    merged = dict(primary)
    pri_instr = primary.get("developer_instructions", "")
    abs_instr = absorbed.get("developer_instructions", "")
    if abs_instr:
        merged["developer_instructions"] = pri_instr + "\n\n---\n\n" + abs_instr
    return merged


def collect_and_classify_agents() -> tuple[dict, list, list]:
    """Load every TOML agent, apply consolidation, and classify.

    Returns ``(all_agents_dict, flagship_list, excluded_list)`` where:

    * *all_agents_dict*: ``{name: toml_data}`` for all agents that are
      neither excluded nor absorbed.
    * *flagship_list*: sorted names of agents in ``FLAGSHIP_AGENTS``.
    * *excluded_list*: sorted names of agents in ``EXCLUDED_AGENTS``.
    """
    toml_files = sorted(CATEGORIES_DIR.rglob("*.toml"))

    # Build {name: toml_data} for every source file
    raw: dict[str, dict] = {}
    for path in toml_files:
        data = load_toml(path)
        raw[data["name"]] = data

    # Determine which names are absorbed (values of CONSOLIDATION_MAP)
    absorbed_names: set[str] = set(CONSOLIDATION_MAP.values())

    # Apply consolidation: merge absorbed into primary
    for primary_name, absorbed_name in CONSOLIDATION_MAP.items():
        if primary_name in raw and absorbed_name in raw:
            raw[primary_name] = merge_agent_toml(raw[primary_name], raw[absorbed_name])

    # Classify
    all_agents: dict[str, dict] = {}
    flagship_list: list[str] = []
    excluded_list: list[str] = []

    for name, data in raw.items():
        if name in EXCLUDED_AGENTS:
            excluded_list.append(name)
            continue
        if name in absorbed_names:
            # Absorbed agents are folded into their primary; skip them
            continue

        all_agents[name] = data

        if name in FLAGSHIP_AGENTS:
            flagship_list.append(name)

    # Warn about unclassified agents
    known = FLAGSHIP_AGENTS | EXCLUDED_AGENTS | absorbed_names
    for name in sorted(all_agents):
        if name not in known:
            # Standard skills are expected — no warning needed
            pass

    flagship_list.sort()
    excluded_list.sort()

    return all_agents, flagship_list, excluded_list


# ---------------------------------------------------------------------------
# Core conversion
# ---------------------------------------------------------------------------

def collect_toml_files() -> list[Path]:
    """Recursively collect all .toml files from categories/."""
    files = sorted(CATEGORIES_DIR.rglob("*.toml"))
    return files


def convert(dry_run: bool = False) -> list[str]:
    """Run the full conversion. Returns list of generated flagship agent names."""
    all_agents, flagship_list, excluded_list = collect_and_classify_agents()
    print(f"Found {len(all_agents)} agents ({len(flagship_list)} flagship, "
          f"{len(all_agents) - len(flagship_list)} skill-only, "
          f"{len(excluded_list)} excluded)")

    if dry_run:
        print("\n=== DRY RUN -- no files will be written ===\n")

    # Clean output directory (idempotent)
    if not dry_run and OUTPUT_DIR.exists():
        print(f"Cleaning existing output directory: {OUTPUT_DIR}")
        shutil.rmtree(OUTPUT_DIR)

    # Create directories
    if not dry_run:
        AGENTS_DIR.mkdir(parents=True, exist_ok=True)
        SKILLS_DIR.mkdir(parents=True, exist_ok=True)
        PLUGIN_DIR.mkdir(parents=True, exist_ok=True)

    flagship_count = 0
    skill_count = 0
    categories_seen: set[str] = set()
    mcp_servers: dict[str, dict] = {}

    # We need to discover the source TOML path for each agent to find its category
    # and to extract MCP servers. Build a name->path map from categories dir.
    toml_paths: dict[str, Path] = {}
    for toml_path in sorted(CATEGORIES_DIR.rglob("*.toml")):
        data = load_toml(toml_path)
        toml_paths[data["name"]] = toml_path

    for name in sorted(all_agents.keys()):
        data = all_agents[name]
        source_path = toml_paths.get(name)

        # Track category from the TOML source path
        if source_path:
            category = source_path.parent.name
            categories_seen.add(category)

        # Extract MCP servers
        if source_path:
            servers = extract_mcp_servers(data, source_path)
            if servers:
                mcp_servers.update(servers)

        # Flagship agents get BOTH agents/{name}.md AND skills/{name}/SKILL.md
        if name in FLAGSHIP_AGENTS:
            sandbox_mode = data.get("sandbox_mode")
            md_content = build_markdown(data, sandbox_mode=sandbox_mode)
            md_path = AGENTS_DIR / f"{name}.md"

            if dry_run:
                print(f"  [DRY] agents/{name}.md")
            else:
                md_path.write_text(md_content, encoding="utf-8")
                print(f"  [OK] agents/{name}.md")
            flagship_count += 1

        # ALL non-excluded agents get skills/{name}/SKILL.md
        skill_body = extract_skill_body(data.get("developer_instructions", ""))
        skill_content = build_skill_md(name, data.get("description", ""), skill_body)
        skill_dir = SKILLS_DIR / name
        if dry_run:
            print(f"  [DRY] skills/{name}/SKILL.md")
        else:
            skill_dir.mkdir(parents=True, exist_ok=True)
            (skill_dir / "SKILL.md").write_text(skill_content, encoding="utf-8")
            print(f"  [OK] skills/{name}/SKILL.md")
        skill_count += 1

    # Write plugin.json with MCP servers
    plugin_manifest = dict(PLUGIN_JSON)
    plugin_manifest["mcpServers"] = mcp_servers
    plugin_json_path = PLUGIN_DIR / "plugin.json"
    if dry_run:
        print(f"\n  [DRY] .claude-plugin/plugin.json")
    else:
        plugin_json_path.write_text(
            json.dumps(plugin_manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"\n  [OK] .claude-plugin/plugin.json")

    # Write install-fragment.json
    install_path = OUTPUT_DIR / "install-fragment.json"
    install_data = build_install_fragment()
    if dry_run:
        print(f"  [DRY] install-fragment.json")
    else:
        install_path.write_text(
            json.dumps(install_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"  [OK] install-fragment.json")

    # Write README.md
    readme_content = build_readme(
        sorted(categories_seen),
        flagship_list,
        flagship_list,
        sorted(all_agents.keys()),
        TOML_TO_OMO_CATEGORY,
    )
    readme_path = OUTPUT_DIR / "README.md"
    if dry_run:
        print(f"  [DRY] README.md")
    else:
        readme_path.write_text(readme_content, encoding="utf-8")
        print(f"  [OK] README.md")

    print(f"\n{'[DRY RUN] Would generate' if dry_run else 'Generated'}: "
          f"{flagship_count} flagship agent files + {skill_count} skill files + "
          f"plugin.json + README.md + install-fragment.json")

    return flagship_list


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate() -> bool:
    """Validate existing plugin output integrity."""
    print("=== Validating plugin output ===\n")
    errors: list[str] = []

    # Check plugin.json
    pj = PLUGIN_DIR / "plugin.json"
    if pj.exists():
        data = json.loads(pj.read_text(encoding="utf-8"))
        if data.get("name") != "omo-awesome-subagents":
            errors.append(f"plugin.json name mismatch: {data.get('name')}")
        elif data.get("version") != "1.0.0":
            errors.append(f"plugin.json version mismatch: {data.get('version')}")
        else:
            print("  [OK] plugin.json basic fields")

        if "mcpServers" not in data:
            errors.append("plugin.json missing mcpServers key")
        else:
            mcp = data.get("mcpServers", {})
            if len(mcp) != 2:
                errors.append(f"Expected 2 MCP servers, found {len(mcp)}")
            expected_mcp = {"openaiDeveloperDocs", "chrome_devtools"}
            if set(mcp.keys()) != expected_mcp:
                errors.append(f"MCP servers mismatch: expected {expected_mcp}, got {set(mcp.keys())}")
            else:
                print("  [OK] plugin.json mcpServers")
    else:
        errors.append("Missing .claude-plugin/plugin.json")

    # Check install-fragment.json
    ifp = OUTPUT_DIR / "install-fragment.json"
    if ifp.exists():
        data = json.loads(ifp.read_text(encoding="utf-8"))
        required_keys = {"name", "marketplace", "scope", "version", "installPath", "lastUpdated"}
        if not required_keys.issubset(data.keys()):
            errors.append(f"install-fragment.json missing keys: {required_keys - data.keys()}")
        elif data["name"] != "omo-awesome-subagents":
            errors.append(f"install-fragment.json name mismatch: {data['name']}")
        else:
            print("  [OK] install-fragment.json")
    else:
        errors.append("Missing install-fragment.json")

    # Check README.md
    rp = OUTPUT_DIR / "README.md"
    if rp.exists():
        print("  [OK] README.md")
    else:
        errors.append("Missing README.md")

    # Check agent .md files (flagship only — 13 expected)
    if AGENTS_DIR.exists():
        md_files = sorted(AGENTS_DIR.glob("*.md"))
        print(f"  Found {len(md_files)} agent .md files")

        if len(md_files) != EXPECTED_FLAGSHIP_COUNT:
            errors.append(
                f"Expected {EXPECTED_FLAGSHIP_COUNT} flagship agent files, found {len(md_files)}"
            )

        # Check all flagship names present
        flagship_names_in_dir = {f.stem for f in md_files}
        missing_flagships = FLAGSHIP_AGENTS - flagship_names_in_dir
        if missing_flagships:
            errors.append(f"Missing flagship agent files: {missing_flagships}")
        extra_flagships = flagship_names_in_dir - FLAGSHIP_AGENTS
        if extra_flagships:
            errors.append(f"Extra flagship agent files (not in FLAGSHIP_AGENTS): {extra_flagships}")

        # Load source TOML data for tools validation
        all_agents, _, _ = collect_and_classify_agents()
        read_only_flagships = {
            name for name in FLAGSHIP_AGENTS
            if all_agents.get(name, {}).get("sandbox_mode") == "read-only"
        }

        # Validate each .md file structure
        for md_file in md_files:
            content = md_file.read_text(encoding="utf-8")

            # Check frontmatter delimiters
            if not content.startswith("---\n"):
                errors.append(f"{md_file.name}: missing opening frontmatter delimiter")
                continue

            parts = content.split("---\n", 2)
            if len(parts) < 3:
                errors.append(f"{md_file.name}: malformed frontmatter (no closing ---)")
                continue

            # Parse frontmatter
            try:
                fm = yaml.safe_load(parts[1])
            except yaml.YAMLError as e:
                errors.append(f"{md_file.name}: invalid YAML frontmatter: {e}")
                continue

            # Check required fields (NO model)
            for key in ("name", "description"):
                if key not in fm:
                    errors.append(f"{md_file.name}: missing frontmatter field '{key}'")

            # Check forbidden: no model field in any agent .md
            if "model:" in content:
                errors.append(f"{md_file.name}: contains 'model:' field (forbidden)")

            # Check forbidden fields
            for forbidden in ("mode",):
                if forbidden in fm:
                    errors.append(f"{md_file.name}: forbidden frontmatter field '{forbidden}'")

            # Check tools field: present only for read-only flagships
            agent_name = md_file.stem
            if agent_name in read_only_flagships:
                if "tools" not in fm:
                    errors.append(f"{md_file.name}: read-only flagship missing 'tools' field")
            else:
                if "tools" in fm:
                    errors.append(f"{md_file.name}: non-read-only flagship has 'tools' field")

        if not missing_flagships and not extra_flagships and len(md_files) == EXPECTED_FLAGSHIP_COUNT:
            print(f"  [OK] All {EXPECTED_FLAGSHIP_COUNT} flagship agent files present and accounted for")
    else:
        errors.append("Missing agents/ directory")

    # Check skills/ directory
    if SKILLS_DIR.exists():
        skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
        print(f"  Found {len(skill_files)} skill files")
        if len(skill_files) != EXPECTED_SKILL_COUNT:
            errors.append(f"Expected {EXPECTED_SKILL_COUNT} skill files, found {len(skill_files)}")
        else:
            print(f"  [OK] All {EXPECTED_SKILL_COUNT} skill files present")
    else:
        errors.append("Missing skills/ directory")

    # Report
    if errors:
        print(f"\n[FAIL] Validation FAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return False
    else:
        print("\n[OK] Validation PASSED -- all checks OK")
        return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert TOML agent definitions into an oh-my-openagent plugin."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be generated without writing files.",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Check existing output integrity without regenerating.",
    )
    args = parser.parse_args()

    if args.validate:
        ok = validate()
        sys.exit(0 if ok else 1)
    else:
        convert(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
