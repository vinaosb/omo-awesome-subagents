# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
