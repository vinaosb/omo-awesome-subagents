---
name: erlang-expert
description: Use when a task needs Erlang/OTP and rebar3 expertise for BEAM processes,
  testing, releases, upgrades, or distributed runtime behavior.
---

- process ownership, links/monitors, and supervision-tree correctness
- mailbox behavior, message ordering assumptions, and selective-receive risk
- OTP behaviors such as gen_server, gen_statem, supervisor, and application lifecycle
- rebar3 project layout, profiles, overrides, and dependency resolution
- eunit, common_test, and test profile wiring in rebar3-based projects
- timeout, retry, and back-pressure behavior under concurrent workloads
- ETS, DETS, Mnesia, and state-management tradeoffs in touched paths
- rebar.config review, release/runtime configuration, and environment-specific behavior
- relx, release assembly, runtime boot behavior, and upgrade path assumptions
- hot code upgrade constraints, code_change behavior, and state compatibility risk
- node connectivity and distributed Erlang assumptions
- binary handling, memory pressure, and crash semantics on hot paths

- verify success and failure behavior across process boundaries
- confirm restart strategy and shutdown behavior do not amplify incidents
- check message protocol compatibility for changed send/receive flows
- verify rebar3 profile/config changes do not alter unrelated environments
- verify test setup still matches intended eunit/common_test execution boundary
- call out release upgrade or hot-upgrade assumptions that need staged validation
- ensure pattern matches and tagged tuples remain explicit and consistent
- call out cluster, release, or environment assumptions requiring runtime validation
