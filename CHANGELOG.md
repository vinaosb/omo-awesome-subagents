# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-03-28

### Added
- `install.sh` (Unix/macOS) and `install.ps1` (Windows) install scripts
- Agents format documentation (`agents/AGENTS.md`)
- Skills format documentation (`skills/AGENTS.md`)
- Collapsible skill category table in README
- Troubleshooting section in README
- Usage examples section in README

### Changed
- Migrated all 13 agent frontmatter from `tools:` string to Opencode `permission:` block
- Added `mode: subagent` to all agent frontmatter
- Removed `name:` from agent frontmatter (filename is the name in Opencode)
- Renamed `dotnet-framework-4.8-expert` to `dotnet-framework-4-8-expert` (Opencode naming spec)
- Renamed `powershell-5.1-expert` to `powershell-5-1-expert` (Opencode naming spec)
- Enhanced 5 minimal skill bodies: code-mapper, ui-designer, ui-fixer, mobile-developer, websocket-engineer
- Removed non-standard headings from code-mapper and ui-designer skills
- Rewrote README.md with split Reviewer/Implementer agent tables and Opencode-native paths
- Rewrote CONTRIBUTING.md with both reviewer/implementer templates and skill naming rules
- Updated `install-fragment.json` to Opencode-native metadata format

### Fixed
- Fixed grammar in cpp-pro, golang-pro, rust-engineer ("Prioritize smallest" → "Prioritize the smallest")
- Fixed incorrect MCP server reference in CHANGELOG v1.0.0

## [1.0.0] - 2026-03-28

### Added
- 13 flagship subagents as callable OMO/Opencode agents
- 127 skills as injectable knowledge modules
- Plugin manifest (`.claude-plugin/plugin.json`) for Claude ecosystem compatibility
- `install-fragment.json` template for plugin registration
- MIT License

### Removed
- Removed TOML source files (previously 136 files in `categories/`)
- Removed converter script (`convert_toml_to_plugin.py`)
- Removed OpenAI Codex compatibility (OMO/Opencode-only focus)

### Changed
- Restructured repository to promote plugin output to root
- Rebranded from VoltAgent/awesome-codex-subagents to omo-awesome-subagents
- Updated all documentation to remove TOML and Codex references
