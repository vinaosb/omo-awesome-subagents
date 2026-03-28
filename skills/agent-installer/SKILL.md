---
name: agent-installer
description: Use when a task needs help selecting, copying, or organizing custom agent
  files from this repository into Opencode agent directories.
---

- trigger-to-agent matching with minimal overlap and redundancy
- personal versus repo-scoped installation tradeoffs
- filename/name consistency and duplicate-agent conflict risks
- config updates needed for agent references or related settings
- MCP dependency awareness where agent behavior depends on external tools
- reproducibility of install steps across developer environments
- lightweight verification steps to confirm agent discovery works

- verify recommended agents are necessary for the stated goal
- confirm install path choice aligns with user scope expectations
- check for naming collisions with existing local/project agents
- ensure prerequisites are explicit before copy/config changes
- call out environment-specific checks needed after installation
