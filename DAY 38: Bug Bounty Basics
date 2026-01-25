DAY 38: Bug Bounty Basics (Recon → Find → Report)

## What is Bug Bounty?
Bug bounty means finding real security vulnerabilities in a company’s web/app systems and reporting them responsibly for rewards (money + reputation).

---

## Typical Bug Bounty Flow
### 1) Recon (Information Gathering)
Goal: find assets and attack surface.
- Subdomains
- URLs / endpoints
- Tech stack
- Parameters

✅ Tools/ideas:
- `subfinder`, `assetfinder`
- `waybackurls`, `gau`
- Google dorks (careful + legal)

---

### 2) Enumeration (Go deeper)
Goal: identify weak points.
- Login / reset password
- Profile update / file upload
- Admin panels
- APIs (mobile/web)
- Hidden endpoints (robots.txt, sitemap.xml)

---

### 3) Vulnerability Testing (Common targets)
Top vulnerabilities to check early:
- **IDOR** (changing userId/accountId and accessing others’ data)
- **Broken Access Control**
- **XSS** (reflected/stored)
- **SQL Injection** (rare but deadly)
- **SSRF**
- **File upload bypass**
- **Authentication flaws** (OTP brute force, weak reset)
- **Rate limiting missing**
- **Sensitive info leaks** (tokens, keys, debug logs)

---

## My Personal “Quick Check” List (10 mins)
1. Can I access other users’ data by changing IDs? (IDOR)
2. Is rate limiting present on login/OTP? (bruteforce)
3. Any suspicious endpoints: `/admin`, `/.env`, `/debug`?
4. Can I upload a file and execute something?
5. Any input reflecting without sanitization? (XSS)
6. Any endpoint returning too much info? (PII leakage)

---

## Real-world Impact (Why companies pay)
A simple IDOR can expose:
- Personal details (phone, address)
- Orders, payments
- Private documents
- Account takeover paths

---

## Reporting (Most important)
A good report includes:
- Clear title
- Steps to reproduce
- Proof (screenshots/video)
- Impact explanation
- Fix suggestion

---

## Fix/Prevention (What devs should do)
- Strong access control checks (server-side)
- Input validation + output encoding
- Rate limiting + lockouts
- Proper session management
- Secure file uploads
- Logging + monitoring

---

## Today’s 1-line takeaway
Bug bounty is not “hacking randomly” — it’s **methodical recon + testing + responsible reporting**.
