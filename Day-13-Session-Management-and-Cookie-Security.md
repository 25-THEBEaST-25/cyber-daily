# Day 13: Session Management & Cookie Security

## What is a Session?
A session is a way for a server to remember a user after login using a unique session ID.

Usually stored in:
- Cookies (most common)
- Server-side storage (mapped via session ID)

---

## Why Cookie Security Matters
If an attacker steals a session cookie, they can impersonate the user **without knowing the password**.

This is called **session hijacking**.

---

## Important Cookie Security Flags

### 1. HttpOnly
- Prevents JavaScript access to cookies
- Protects against XSS attacks

Set-Cookie: sessionId=abc123; HttpOnly

---

### 2. Secure
- Cookie is sent only over HTTPS
- Prevents MITM attacks on HTTP

Set-Cookie: sessionId=abc123; Secure

---

### 3. SameSite
Controls cross-site cookie sending

- `Strict` → sent only to same site
- `Lax` → safe default (allows top-level navigation)
- `None` → must be Secure (used for cross-site)

Set-Cookie: sessionId=abc123; SameSite=Lax
---

## Common Session Attacks

### Session Hijacking
- Attacker steals session ID
- Logs in as victim without credentials

### Session Fixation
- Attacker forces a known session ID
- Victim logs in → attacker reuses session

---

## Best Practices
- Regenerate session ID after login
- Set HttpOnly + Secure + SameSite
- Use short session expiry
- Invalidate session on logout
- Use HTTPS everywhere

---

## Real-World Note
Many major breaches happened **without password leaks** — only stolen session cookies.
