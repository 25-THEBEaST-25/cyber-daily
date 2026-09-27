# Cyber Daily

A daily cybersecurity learning log focused on practical security concepts, real-world attack surfaces, and defensive thinking.

This repository documents my consistent practice in cybersecurity — one focused topic per day.

## Why Cyber Daily?

Security is not learned in bursts — it’s built through consistency.

This repo represents:
- Daily threat-model thinking
- Hands-on experimentation
- Concept reinforcement through writing

## Structure

Each entry lives in its own `dayNN-topic.md` file at the repo root (Day 7 keeps its own folder,
`day07-rate-limiting/README.md`, from before this naming pass). Entries aren't always
strictly cybersecurity — a few days are reflections, milestones, or general problem-solving
practice — but each one is documented below as-is.

## Index

| Day | Topic |
|-----|-------|
| 01 | [What is Phishing?](day01-phishing.md) — basics of phishing attacks and how attackers trick users |
| 02 | [What is Malware?](day02-malware.md) — virus, worm, trojan, ransomware basics |
| 03 | [What is SQL Injection?](day03-sql-injection.md) — basics of SQL injection |
| 04 | [Why SQL Injection Is Dangerous](day04-sql-injection-impact.md) — real-world impact of SQLi |
| 05 | [Password Attacks (Basics)](day05-password-attacks.md) — brute-force fundamentals |
| 06 | [Password Attacks](day06-password-attacks.md) — brute-force attack deep dive |
| 07 | [Rate Limiting & Temporary Blocks](day07-rate-limiting/README.md) — rate limiting and temporary IP blocks against brute force/credential stuffing |
| 08 | [Authentication vs Authorization](day08-authentication-vs-authorization.md) — the core difference between the two |
| 09 | [Rate Limiting & Brute Force Protection](day09-rate-limiting-brute-force-protection.md) — restricting request/login attempt rates |
| 10 | [Account Lockout vs Rate Limiting vs IP Blocking](day10-account-lockout-vs-rate-limiting.md) — comparing brute-force defenses |
| 11 | [CAPTCHA & Human Verification](day11-captcha-human-verification.md) — CAPTCHA's role in auth security |
| 12 | [Secure File Hosting & Download Safety](day12-secure-file-hosting-download-safety.md) — a GitHub Pages case study |
| 13 | [Session Management & Cookie Security](day13-session-management-cookie-security.md) — how sessions and cookies work securely |
| 14 | [JWT vs Session-Based Authentication](day14-jwt-vs-session-based-authentication.md) — comparing the two auth models |
| 15 | [OAuth 2.0 Authentication Flow](day15-oauth2-authentication-flow.md) — how OAuth 2.0 delegates access without sharing passwords |
| 16 | [Access Tokens vs Refresh Tokens](day16-access-tokens-vs-refresh-tokens.md) — how the two token types balance security and UX |
| 17 | [Input Validation & Sanitization](day17-input-validation.md) — validating and sanitizing user input |
| 18 | [Authentication Bypass & Logic Flaws](day18-authentication-bypass.md) — bypassing auth via logic weaknesses |
| 19 | [Security Misconfigurations I've Seen](day19-security-misconfigurations-ive-seen.md) — real misconfigurations noticed while building |
| 20 | [Input Validation & Sanitization](day20-input-validation-sanitization.md) — revisited with a practical security focus |
| 21 | [Authentication vs Authorization](day21-authentication-vs-authorization.md) — revisited |
| 22 | [What Have I Learned So Far](day22-what-have-i-learned-so-far.md) — reflection on the learning journey |
| 23 | [Authentication vs Authorization](day23-authentication-vs-authorization.md) — understanding the difference in depth |
| 24 | [Sign Flipping Attacks & Parity-Based Logic Abuse](day24-sign-flipping-parity-based-logic-abuse.md) — exploiting logical/mathematical invariants |
| 25 | [Password Reset & Account Recovery Security](day25-password-reset-account-recovery-security.md) — securing recovery flows |
| 26 | [Tree Splitting, Subtree Sums & Optimization Thinking](day26-tree-splitting-subtree-sums-optimization-thinking.md) — algorithmic problem-solving practice (not security-specific) |
| 27 | [Password Storage: Hashing vs Encryption](day27-password-storage-hashing-vs-encryption.md) — why hashing wins for password storage |
| 28 | [Why "Security Tools" Don't Make You a Security Engineer](day28-why-security-tools-dont-make-you-a-security-engineer.md) — a mindset reflection |
| 29 | [Minimum Privilege Principle (PoLP)](day29-minimum-privilege-principle-polp.md) — why over-permissioning is dangerous |
| 30 | [Attack Surface Reduction (ASR)](day30-attack-surface-reduction-asr.md) — shrinking what attackers can touch |
| 31 | [Let's Celebrate](day31-lets-celebrate.md) — 31-day milestone reflection |
| 32 | [Binary Search on Answer & Precision Thinking](day32-binary-search-on-answer.md) — algorithmic problem-solving practice (not security-specific) |
| 33 | [Security Misconfiguration](day33-security-misconfiguration.md) — what it is and why it happens |
| 34 | [Cross-Site Request Forgery (CSRF)](day34-cross-site-request-forgery-csrf.md) — attacking and defending against CSRF |
| 35 | [Secure Password Storage (Hashing + Salting)](day35-secure-password-storage-hashing-salting.md) — common storage mistakes |
| 36 | [SSH Security Basics](day36-ssh-security-basics.md) — hardening and safe practices |
| 37 | [MFA vs 2FA](day37-mfa-vs-2fa.md) — differences and common bypasses |
| 38 | [Bug Bounty Basics](day38-bug-bounty-basics.md) — recon → find → report workflow |
| 39 | [VAPT Basics + Scanning Tools](day39-vapt-basics-scanning-tools.md) — vulnerability assessment and penetration testing basics |
| 40 | [Keep the Grind](day40-keep-the-grind.md) — short update on ongoing project/repo maintenance |
| 41 | [Live Cyber Attack Map](day41-live-cyber-attack-map.md) — observations from watching real-time global attack traffic |
| 42 | [Ethical Hacking – Access Control Weaknesses](day42-ethical-hacking-access-control-weaknesses.md) — common access control flaws |
| 43 | [Reflection on a Learning Gap](day43-reflection-refocus-on-goals.md) — refocusing on cybersecurity goals after a break |
| 44 | [Reignition](day44-reignition.md) — returning to the series after a hiatus |
| 45 | [Back Again](day45-back-again.md) — a short note on resuming the series |
| 45 | [Broken Authentication (Deep Dive)](day45-broken-authentication-deep-dive.md) — a deeper look at broken authentication issues |
| 46 | [IDOR (Insecure Direct Object Reference)](day46-idor-deep-dive.md) — deep dive with examples |
| 47 | [Broken Access Control (Deep Dive)](day47-broken-access-control-deep-dive.md) — how access control fails in practice |
| 48 | [Social Engineering Attacks](day48-social-engineering-attacks.md) — attacks that rely on human psychology |
| 49 | [Port Scanning & Reconnaissance](day49-port-scanning-reconnaissance.md) — scanning fundamentals, paired with the [`range_scanner.py`](range_scanner.py) tool |
| 50 | [Major Milestone](day50-major-milestone.md) — 50 days of cybersecurity learning |
| 51 | [API Security & BOLA](day51-api-security-bola.md) — Broken Object Level Authorization in APIs |
| 52 | [Business Logic Vulnerabilities (BLV)](day52-business-logic-vulnerabilities-blv.md) — deep dive into logic-based flaws |
| 53 | [Refresh Token Rotation & Token Theft Detection](day53-refresh-token-rotation.md) — modern token security practices |

## Tools

- [`range_scanner.py`](range_scanner.py) — a simple TCP port-range scanner written for Day 49's
  port scanning & reconnaissance topic.
