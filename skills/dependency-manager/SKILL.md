---
name: dependency-manager
description: Use when a task needs dependency upgrades, package graph analysis, version-policy
  cleanup, or third-party library risk assessment.
---

- version policy and compatibility constraints across direct and transitive deps
- security and maintenance risk in outdated or vulnerable packages
- lockfile integrity and reproducible install/build behavior
- upgrade blast radius across runtime, tests, and tooling pipelines
- license/compliance implications where dependency changes affect distribution
- package graph simplification opportunities that reduce long-term risk
- rollback strategy for problematic upgrades

- verify upgrade recommendations include compatibility and risk rationale
- confirm transitive dependency impact is considered for critical paths
- check reproducibility after lockfile or resolver changes
- ensure security fixes are prioritized by exploitability and exposure
- call out required integration tests before final dependency promotion
