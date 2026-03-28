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

Typical length: 15-19 lines. No `tools:` frontmatter (unlike agents). Minor variant: `ui-designer` uses explicit "Design checks:" heading.

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
- Must include frontmatter with `name` and `description`
- Body: dash-prefixed bullets only
- Never nest under category subdirectories

## KNOWN ISSUES

- None currently tracked
