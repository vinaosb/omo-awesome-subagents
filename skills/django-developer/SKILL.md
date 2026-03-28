---
name: django-developer
description: Use when a task needs Django-specific work across models, views, forms,
  ORM behavior, or admin and middleware flows.
---

- model integrity, query behavior, and migration safety in changed paths
- view/form/serializer logic consistency with auth and permission rules
- middleware side effects and request lifecycle ordering assumptions
- ORM efficiency (N+1, select_related/prefetch_related) for touched endpoints
- admin customizations and signal handlers that may hide side effects
- template context and validation error behavior visible to users
- compatibility with established project settings and app boundaries

- verify behavior with representative request data and permission context
- confirm migrations are reversible or explicitly note irreversible operations
- check transaction boundaries where multiple writes occur
- ensure validation and error responses remain consistent across forms/APIs
- call out required environment checks (cache, async worker, storage backend)
