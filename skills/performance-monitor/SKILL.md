---
name: performance-monitor
description: Use when a task needs ongoing performance-signal interpretation across
  build, runtime, or operational metrics before deeper optimization starts.
---

- metric definition integrity and comparability across periods/environments
- severity weighting by user impact and business-critical path relevance
- correlation with releases, config changes, and workload shifts
- dominant resource signal (CPU, memory, IO, latency, queueing) classification
- confidence scoring for likely owner subsystem
- alert fatigue reduction through prioritized triage output
- handoff readiness for specialist performance engineering follow-up

- verify observed movement exceeds expected baseline noise
- confirm candidate root-area ranking includes confidence and caveats
- check for confounders (traffic mix, synthetic tests, instrumentation drift)
- ensure next-step recommendation is specific and executable
- call out missing telemetry needed to avoid misrouting effort
