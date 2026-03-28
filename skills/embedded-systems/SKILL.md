---
name: embedded-systems
description: Use when a task needs embedded or hardware-adjacent work involving device
  constraints, firmware boundaries, timing, or low-level integration.
---

- timing and resource constraints (CPU, memory, power) on target hardware
- hardware-software boundary correctness for drivers, buses, and interrupts
- real-time behavior and determinism under normal and error conditions
- state-machine safety for startup, runtime, and failure recovery flows
- firmware update/rollback and version compatibility constraints
- diagnostic visibility for field failures with limited telemetry
- robustness against noisy inputs and transient hardware faults

- verify behavior assumptions against target hardware/resource constraints
- confirm interrupt/concurrency changes preserve deterministic timing
- check failure-mode handling for watchdog, reset, and recovery paths
- ensure firmware compatibility and upgrade safety are explicit
- call out bench/device-level validations required outside repository context
