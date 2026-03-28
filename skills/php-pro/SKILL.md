---
name: php-pro
description: Use when a task needs PHP expertise for application logic, framework
  integration, runtime debugging, or server-side code evolution.
---

- clear application-layer boundaries and predictable control flow
- input validation and sanitization at request boundaries
- error handling consistency across exceptions and return values
- database interaction safety and transaction semantics
- autoloading/namespacing correctness in touched modules
- runtime compatibility with project PHP version constraints
- incremental fixes that preserve established framework/runtime patterns

- verify behavior for valid input and at least one invalid edge case
- confirm database writes are consistent under partial failure conditions
- check autoloading and namespace resolution for changed classes
- ensure response/error surfaces remain stable for callers
- call out deployment/runtime assumptions requiring environment checks
