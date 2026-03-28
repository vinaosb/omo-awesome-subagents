# SKILLS DIRECTORY

## OVERVIEW

127 skill definitions in flat namespace. Each skill is a directory containing a single `SKILL.md` file.

## STRUCTURE

```
skills/
├── accessibility-expert/SKILL.md
├── agent-installer/SKILL.md
├── algorithm-specialist/SKILL.md
├── ...                              # 127 total, alphabetical
└── wordpress-developer/SKILL.md
```

**FLAT ONLY** — no category subdirectories. Categories exist as logical groupings in README, not as filesystem structure.

## FORMAT

```markdown
---
name: skill-name
description: Use when a task needs [specific capability].
---

- {Focus area bullet}
- {Focus area bullet}
- {Quality/design check bullet}
```

**Key frontmatter fields:**
- `name` (REQUIRED): Must match directory name. Lowercase alphanumeric + single hyphens, 1-64 chars. Regex: `^[a-z0-9]+(-[a-z0-9]+)*$`
- `description` (REQUIRED): 1-1024 chars. Starts with "Use when..."

Typical length: 15-19 lines. No `tools:` or `permission:` frontmatter (skills inherit tool access from the invoking agent). Body uses dash-prefixed bullets only — no headings within the body.

## CATEGORIES (LOGICAL ONLY)

| Category | Example Skills |
|----------|---------------|
| Core Development | code-reviewer, debugging-specialist, refactoring-expert |
| Language Specialists | rust-engineer, golang-pro, cpp-pro, python-specialist |
| DevOps & Infrastructure | kubernetes-specialist, terraform-engineer, ci-cd-specialist |
| Security | security-auditor, penetration-tester, vulnerability-scanner |
| AI/ML | llm-architect, mlops-engineer, prompt-engineer |
| Frontend | react-specialist, ui-designer, accessibility-expert |
| Backend | api-designer, database-optimizer, microservices-architect |
| Testing | integration-tester, performance-tester, test-automation |
| Documentation | technical-writer, api-documenter, changelog-manager |
| Specialized | blockchain-developer, game-developer, embedded-systems |

## ADDING A SKILL

See `CONTRIBUTING.md` at repo root. Key rules:
- Directory: `skills/<name>/SKILL.md`
- Directory name must match `name:` in frontmatter
- Must include frontmatter with `name` and `description`
- Body: dash-prefixed bullets only (no headings)
- Never nest under category subdirectories

## KNOWN ISSUES

- None currently tracked
