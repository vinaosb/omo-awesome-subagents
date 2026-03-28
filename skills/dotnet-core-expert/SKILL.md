---
name: dotnet-core-expert
description: Use when a task needs modern .NET and ASP.NET Core expertise for APIs,
  hosting, middleware, or cross-platform application behavior.
---

- middleware ordering and request pipeline behavior
- hosting/configuration boundaries across environments
- DI lifetimes and service resolution correctness
- API contract stability, model binding, and validation behavior
- logging/telemetry clarity for operational debugging
- authn/authz enforcement and policy mapping in touched routes
- cross-platform runtime implications of changed code paths

- verify changed endpoint behavior for valid and invalid inputs
- confirm middleware/auth changes do not bypass existing protections
- check configuration fallbacks and environment-variable assumptions
- ensure serialization or contract changes are backward-compatible or documented
- call out deployment/runtime verification needed outside local workspace
