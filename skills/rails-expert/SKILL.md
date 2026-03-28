---
name: rails-expert
description: Use when a task needs Ruby on Rails expertise for models, controllers,
  jobs, callbacks, or convention-driven application changes.
---

- model/controller/service responsibilities with convention alignment
- ActiveRecord query behavior, transactions, and callback side effects
- validation and authorization consistency in request lifecycle
- job/queue behavior and idempotency for async work
- route and serializer/JSON contract stability for clients
- n+1 risks and eager-loading strategy in changed endpoints
- keeping changes idiomatic to existing Rails code style

- verify one request flow from routing to persistence and response
- confirm callback or concern changes do not create hidden side effects
- check transaction boundaries where multiple writes occur
- ensure API/HTML error handling remains consistent and user-visible
- call out migration/deployment checks needed for schema-affecting changes
