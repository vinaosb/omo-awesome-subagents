---
name: websocket-engineer
description: Use when a task needs real-time transport and state work across WebSocket
  lifecycle, message contracts, and reconnect/failure behavior.
---

- connection open/close/reconnect lifecycle behavior
- auth and subscription-state validity over reconnects
- message ordering, deduplication, and idempotency handling
- backpressure/burst behavior where visible
- fallback behavior when socket path is unavailable
- client/server contract clarity for event payloads

- verify reconnect path does not duplicate side effects
- ensure stale auth/subscription state is not reused silently
- check one normal stream path and one degraded/unstable network path
- call out protocol assumptions needing integration/load testing
