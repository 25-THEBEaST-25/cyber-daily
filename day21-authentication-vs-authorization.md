# Day 21 – Authentication vs Authorization

Authentication and authorization are often confused, but they solve
very different security problems.

## Authentication
Authentication answers the question:
**“Who are you?”**

Examples:
- Username + password
- OTP
- Biometric verification

Failure impact:
- Account takeover
- Credential stuffing
- Identity impersonation

## Authorization
Authorization answers the question:
**“What are you allowed to do?”**

Examples:
- Role-Based Access Control (RBAC)
- Admin vs user privileges
- Resource-level permissions

Failure impact:
- Privilege escalation
- Data exposure
- Unauthorized actions

## Real-World Failure Case

Many systems correctly authenticate users but fail to enforce
authorization checks consistently.

Example:
- User logs in successfully
- Backend does not verify role before accessing admin endpoint
- Leads to privilege escalation

## Key Security Insight

Authentication without proper authorization is incomplete security.
Both must be enforced independently and verified on every request.
