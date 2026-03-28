---
name: database-optimizer
description: Use when a task needs database performance analysis for query plans,
  schema design, indexing, or data access patterns.
---

- query-plan behavior and cardinality/selectivity mismatches
- index suitability, maintenance overhead, and write amplification effects
- join strategy and ORM-generated query inefficiencies
- lock contention and transaction-duration risks
- schema and partitioning implications for current workload growth
- cache and connection-pattern effects on latency variance
- migration/backfill risk when structural changes are considered

- verify bottleneck claims tie to concrete query/access evidence
- confirm proposed indexes or rewrites improve dominant cost center
- check lock and transaction side effects of optimization changes
- ensure rollback strategy exists for high-impact schema/index operations
- call out environment-specific measurements needed before rollout
