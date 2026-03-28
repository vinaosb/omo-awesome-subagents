---
name: golang-pro
description: Use when a task needs Go expertise for concurrency, service implementation,
  interfaces, tooling, or performance-sensitive backend paths.
---

- goroutine lifecycle and cancellation propagation
- channel usage correctness, buffering assumptions, and deadlock risk
- error handling consistency and wrapped-context clarity
- interface boundaries and package-level cohesion in touched code
- context usage in I/O and RPC/database boundaries
- allocation/copy behavior on performance-sensitive paths
- safe concurrency with shared mutable state

- verify success and failure paths with explicit error assertions
- confirm goroutines terminate under cancellation and timeout conditions
- check channel close/send/receive assumptions to avoid panics
- ensure API signature changes remain backward-compatible where required
- call out benchmark or race-test follow-up when concurrency risk remains
