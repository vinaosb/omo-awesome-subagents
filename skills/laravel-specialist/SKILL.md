---
name: laravel-specialist
description: Use when a task needs Laravel-specific work across routing, Eloquent,
  queues, validation, or application structure.
---

- route/controller/service boundary clarity for touched behavior
- Eloquent query correctness, eager loading, and transaction safety
- validation and authorization policy consistency
- queue/job/retry side effects for asynchronous operations
- configuration and environment boundaries (.env, cache, queue drivers)
- event/listener or observer side effects that affect data consistency
- preserving Laravel conventions to keep code maintainable

- verify one success path and one validation/authorization failure path
- confirm database writes remain atomic where multiple models are involved
- check for N+1 query regressions in touched endpoints
- ensure queue/job behavior is idempotent or explicitly documented
- call out environment checks needed for cache/queue/session backends
