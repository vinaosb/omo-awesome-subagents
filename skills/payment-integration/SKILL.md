---
name: payment-integration
description: Use when a task needs payment-flow review or implementation for checkout,
  idempotency, webhooks, retries, or settlement state handling.
---

- checkout flow correctness across authorize/capture/refund/void paths
- idempotency and retry handling for client and server payment calls
- webhook verification, ordering, and eventual consistency reconciliation
- failure-mode UX for declines, timeouts, duplicate callbacks, and partial success
- secret/key management and PCI-sensitive boundary hygiene
- multi-provider/state-machine differences and fallback behavior
- settlement and ledger synchronization for financial accuracy

- verify payment state machine covers all expected terminal and intermediate states
- confirm idempotency keys and dedupe logic prevent duplicate charge outcomes
- check webhook trust and replay-protection mechanisms
- ensure reconciliation path catches async drift between provider and internal state
- call out sandbox/provider environment validations needed pre-production
