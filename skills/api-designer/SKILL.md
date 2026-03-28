---
name: api-designer
description: Use when a task needs API contract design, evolution planning, or compatibility
  review before implementation starts.
---

- resource and endpoint modeling aligned to domain boundaries
- request and response schema clarity
- validation semantics and error model consistency
- auth, authorization, and tenant-scoping expectations in the contract
- pagination, filtering, sorting, and partial response strategy where relevant
- idempotency and retry behavior for mutating operations
- versioning and deprecation strategy
- observability-relevant contract signals (correlation keys, stable error codes)

Architecture checks:
- ensure contract behavior is explicit, not framework-default ambiguity
- isolate transport contract from internal storage schema where possible
- identify client-breaking changes and hidden coupling
- call out where "one endpoint" would blur ownership and increase long-term cost

- provide one canonical success response and one canonical failure response per critical operation
- confirm field optionality/nullability reflects real behavior
- verify error taxonomy is actionable for clients
- describe migration path for changed fields or semantics
