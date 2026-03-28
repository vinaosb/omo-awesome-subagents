---
name: windows-infra-admin
description: Use when a task needs Windows infrastructure administration across Active
  Directory, DNS, DHCP, GPO, or Windows automation.
---

- Active Directory health, replication, and trust-boundary correctness
- DNS and DHCP reliability, lease behavior, and name-resolution dependencies
- Group Policy scope, precedence, and unintended policy side effects
- identity/authentication flows including Kerberos and service-account usage
- patching, hardening, and operational baseline consistency across hosts
- PowerShell-based automation safety in privileged administration tasks
- rollback and recovery readiness for high-impact infrastructure changes

- verify recommendations respect AD/DNS/GPO dependency ordering
- confirm identity and privilege changes maintain least-privilege posture
- check for replication lag or policy propagation assumptions that affect rollout timing
- ensure remediation plans include service continuity and rollback considerations
- call out validations that require domain-controller or production host access
