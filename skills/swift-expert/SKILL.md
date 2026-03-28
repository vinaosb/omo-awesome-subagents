---
name: swift-expert
description: Use when a task needs Swift expertise for iOS or macOS code, async flows,
  Apple platform APIs, or strongly typed application logic.
---

- value/reference semantics and data ownership clarity
- async/await and actor isolation correctness
- UI state synchronization for UIKit/SwiftUI boundaries
- error propagation and recoverability in app flows
- API/SDK integration boundaries and version compatibility
- memory and lifecycle behavior in long-lived objects
- keeping code idiomatic to existing app architecture

- verify changed behavior under success, failure, and cancellation states
- confirm actor/concurrency boundaries avoid data races
- check optionals and decoding assumptions for runtime crashes
- ensure UI updates occur on the correct execution context
- call out device/OS-version checks needed outside local workspace
