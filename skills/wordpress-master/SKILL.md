---
name: wordpress-master
description: Use when a task needs WordPress-specific implementation or debugging
  across themes, plugins, content architecture, or operational site behavior.
---

- theme template and hook/filter interaction correctness
- plugin compatibility and conflict risk in shared runtime
- content model/admin workflow impact of code changes
- cache/CDN/permalink behavior affecting user-visible output
- security and permission boundaries in forms, AJAX, and admin actions
- performance implications for high-traffic pages and heavy plugins
- deployment and rollback practicality for production WP environments

- verify fix works with expected plugin/theme activation state
- confirm no regression in admin authoring or publishing workflows
- check cache and rewrite assumptions for stale or broken page behavior
- ensure capability/nonce/input validation remains secure
- call out hosting/staging validations needed outside local repository
