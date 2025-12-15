# Day 7 — Rate Limiting & Temporary Blocks (Auth Abuse Prevention)

## What I Learned Today
Today I implemented and deeply understood how **rate limiting and temporary IP blocks**
protect authentication systems from brute-force and credential stuffing attacks.

This is a **real-world defensive mechanism** used by services like Cloudflare, AWS WAF,
Fail2Ban, and modern authentication gateways.

---

## Problem
Attackers often try:
- Rapid password guessing (brute force)
- Repeated login attempts from the same IP
- Credential stuffing using leaked passwords

Without protection, this can:
- Compromise accounts
- Exhaust server resources
- Bypass weak passwords

---

## Rate Limiting Explained
Rate limiting restricts **how many login attempts** an IP can make within a fixed time window.

Example:
- Max 3 attempts in 10 seconds
- If exceeded → IP is temporarily blocked

This slows attackers **without affecting normal users**.

---

## Temporary Block Logic
Instead of banning immediately:
- First few violations → **temporary block**
- Block expires after a cooldown period
- State is reset after timeout

This prevents false positives and allows legitimate users to retry later.

---

## Strike-Based Escalation
I also learned that real systems don’t rely on a single violation.

They track **rate-limit strikes**:
- Strike 1 → temp block
- Strike 2 → temp block
- Strike 3 → permanent ban

This balances **security + usability**.

---

## Logging & Forensics
Every login attempt was logged with:
- Timestamp
- Username
- IP address
- Outcome (FAILED / RATE_LIMIT / SUCCESS)

Logs are critical for:
- Incident investigation
- Detecting attack patterns
- Compliance and audits

Logs were intentionally excluded from GitHub using `.gitignore`
to avoid leaking sensitive data.

---

## Key Takeaway
Security is not about blocking everything.
It’s about **controlled resistance**:
- Slow attackers
- Protect users
- Preserve system availability

This exercise gave me a much clearer understanding of
how real authentication systems defend themselves in production.

---

## Tools & Concepts Used
- Python
- Time-window rate limiting
- Temporary IP blocking
- Strike counters
- Secure logging practices

---

🔐 *Defensive security is about thinking like an attacker — and acting like an engineer.*
