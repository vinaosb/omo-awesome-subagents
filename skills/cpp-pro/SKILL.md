---
name: cpp-pro
description: Use when a task needs C++ work involving performance-sensitive code,
  memory ownership, concurrency, or systems-level integration.
---

- ownership and lifetime boundaries across stack, heap, and shared resources
- RAII usage, exception safety guarantees, and deterministic cleanup
- concurrency safety around locks, atomics, and cross-thread object access
- ABI or interface compatibility when touching public headers
- performance-sensitive paths where allocation or copies can regress latency
- undefined behavior risks (dangling refs, out-of-bounds, data races)
- build-system and compiler-flag assumptions affecting changed code

- validate success and failure paths for resource acquisition and release
- confirm thread-safety assumptions at touched synchronization boundaries
- check for accidental ownership transfer or lifetime extension bugs
- ensure any API signature changes preserve compatibility expectations
- call out benchmark or profiling follow-up when performance claims are inferred
