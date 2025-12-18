# Day 10 – Account Lockout vs Rate Limiting vs IP Blocking 🔐

Modern authentication systems use multiple defenses to stop brute-force
and credential-stuffing attacks. Each control solves a different problem.

---

## 1️⃣ Rate Limiting
Rate limiting restricts how many requests are allowed in a given time window.

🔹 Applied to:
- IP address
- API endpoint
- User session

🔹 Purpose:
- Prevent rapid automated attacks
- Slow down brute-force attempts

🔹 Example:
- Max 5 login attempts per minute per IP

---

## 2️⃣ IP Blocking
IP blocking completely denies access from a suspicious IP address.

🔹 Applied to:
- Malicious or abusive IPs

🔹 Types:
- Temporary IP block (cooldown-based)
- Permanent IP ban (after repeated violations)

🔹 Purpose:
- Stop repeated abuse from the same source

---

## 3️⃣ Account Lockout
Account lockout disables login for a specific user account after multiple failures.

🔹 Applied to:
- Username / account

🔹 Purpose:
- Protect accounts from credential-stuffing
- Works even if attacker rotates IPs

🔹 Example:
- Lock account after 5 failed password attempts

---

## 🔥 Key Differences

| Feature | Rate Limiting | IP Blocking | Account Lockout |
|------|-------------|------------|----------------|
| Scope | Request level | IP address | User account |
| Stops fast attacks | ✅ | ✅ | ❌ |
| Stops IP rotation | ❌ | ❌ | ✅ |
| Protects specific user | ❌ | ❌ | ✅ |

---

## 🧠 Security Insight
No single control is enough.

Real-world systems use:
- Rate limiting to slow attackers
- IP blocking to stop abusive sources
- Account lockout to protect users

This layered approach is called **Defense in Depth**.
