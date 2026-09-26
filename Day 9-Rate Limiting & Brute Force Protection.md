# Day 9 – Rate Limiting & Brute Force Protection

## What is Rate Limiting?
Rate limiting restricts the number of requests or login attempts a user or IP can make within a specific time window.

It helps prevent brute-force attacks and abuse of authentication systems.

## Brute Force Attacks
A brute-force attack is when an attacker repeatedly tries different passwords to gain unauthorized access.

Without rate limiting, login systems are vulnerable to such attacks.

## Real-World Implementation
- Track login attempts per IP
- Apply a time window (example: 3 attempts in 10 seconds)
- Temporarily block IPs on violation
- Escalate to permanent ban after repeated violations

## Security Note
Rate limiting combined with temporary and permanent IP blocking significantly reduces the risk of brute-force attacks.
