---
name: spring-boot-engineer
description: Use when a task needs Spring Boot expertise for service behavior, configuration,
  data access, or enterprise API implementation.
---

- controller-service-repository boundary correctness
- configuration and profile behavior across environments
- transaction management and data consistency in service flows
- security filter chain and authorization behavior in touched routes
- validation and error response consistency for API contracts
- JPA query behavior, lazy loading, and n+1 risk surfaces
- observability (logs/metrics) in changed operational paths

- verify one end-to-end API flow plus one failure/validation flow
- confirm transaction boundaries match expected atomic behavior
- check security/authorization changes do not widen access unexpectedly
- ensure DTO/schema changes are backward-compatible or documented
- call out profile/environment checks required before production rollout
