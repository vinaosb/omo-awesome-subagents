---
name: java-architect
description: Use when a task needs Java application or service architecture help across
  framework boundaries, JVM behavior, or large codebase structure.
---

- clear service/module boundaries and dependency direction
- threading, async execution, and resource lifecycle behavior
- exception taxonomy and propagation across architectural layers
- JVM/runtime considerations relevant to changed path
- contract stability of interfaces, DTOs, and serialization surfaces
- transactional consistency and side effects in service flows
- cohesive changes that preserve established framework conventions

- verify one end-to-end flow crossing at least one layer boundary
- confirm error mapping remains explicit and actionable
- check concurrency or pooling assumptions around changed components
- ensure contract or schema changes are backward-compatible or called out
- flag deployment/config checks needed to validate runtime behavior
