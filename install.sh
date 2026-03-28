#!/bin/bash
set -e

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
OPENCODE_DIR="${OPENCODE_DIR:-$HOME/.config/opencode}"

echo "Installing omo-awesome-subagents..."
echo "  Source: $REPO_ROOT"
echo "  Target: $OPENCODE_DIR"

# Create target directories
mkdir -p "$OPENCODE_DIR/agents" "$OPENCODE_DIR/skills"

# Copy agents (skip AGENTS.md meta file)
copied_agents=0
for agent in "$REPO_ROOT/agents/"*.md; do
  basename_file=$(basename "$agent")
  if [ "$basename_file" = "AGENTS.md" ]; then
    continue
  fi
  cp "$agent" "$OPENCODE_DIR/agents/"
  copied_agents=$((copied_agents + 1))
done

# Copy skills (skip AGENTS.md meta file)
copied_skills=0
for dir in "$REPO_ROOT/skills/"*/; do
  skill_name=$(basename "$dir")
  if [ -f "$dir/SKILL.md" ]; then
    mkdir -p "$OPENCODE_DIR/skills/$skill_name"
    cp "$dir/SKILL.md" "$OPENCODE_DIR/skills/$skill_name/"
    copied_skills=$((copied_skills + 1))
  fi
done

echo ""
echo "Done!"
echo "  Installed $copied_agents agents to $OPENCODE_DIR/agents/"
echo "  Installed $copied_skills skills to $OPENCODE_DIR/skills/"
echo ""
echo "Restart your Opencode session to use them."
