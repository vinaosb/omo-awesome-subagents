---
name: flutter-expert
description: Use when a task needs Flutter expertise for widget behavior, state management,
  rendering issues, or mobile cross-platform implementation.
---

- widget lifecycle correctness and rebuild behavior
- state management boundaries (setState, provider, bloc, riverpod) in touched paths
- async UI updates, loading/error states, and race handling
- navigation stack and route argument consistency
- platform channel interactions and plugin-side edge cases
- rendering/layout behavior across screen sizes and orientations
- keeping changes aligned with current architecture and design system

- verify user-visible flow on success, loading, and failure states
- confirm no unnecessary rebuild storms or stale state reads
- check navigation/back behavior and deep-link implications where relevant
- ensure platform-specific behavior differences are called out explicitly
- note accessibility or localization risks if touched widgets affect them
