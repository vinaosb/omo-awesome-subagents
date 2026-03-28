---
name: typescript-pro
description: Use when a task needs strong TypeScript help for types, interfaces, refactors,
  or compiler-driven fixes.
---

- type boundaries that represent real runtime contracts
- unsafe assertions, any leakage, and overly broad unions
- generic design and inference behavior in changed APIs
- cross-module type drift between producer and consumer code
- strictness alignment with current tsconfig and repo standards
- reduction of incidental complexity while increasing safety
- minimal churn with maximal contract clarity

- verify changed paths compile cleanly under project strictness settings
- confirm type fixes correspond to runtime truth, not assertion shortcuts
- check one integration boundary for downstream type breakage risk
- ensure serialized data contracts remain explicit and stable
- call out remaining unsafe edges and why they are deferred
