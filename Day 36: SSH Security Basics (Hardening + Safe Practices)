# Cyber Daily — Day 36 ✅  
**Topic:** SSH Security Basics (Hardening + Safe Practices)  
**Date:** 20-01-2026  

---

## 🔥 What I learned today
SSH (Secure Shell) is a secure way to remotely access a server/computer over a network.  
It encrypts communication so attackers can’t easily sniff usernames/passwords.

---

## 🛡️ Why SSH security matters
If SSH is weak, attackers can:
- brute force passwords
- steal credentials
- gain remote access to the system
- install malware / crypto miners
- move deeper inside the network

---

## ✅ Best Practices to Secure SSH
### 1) Use Key-Based Authentication (instead of passwords)
Passwords can be guessed/brute-forced.  
SSH keys are way stronger.

✅ Recommended:
- Generate key pair
- Keep private key safe
- Use public key on server

---

### 2) Disable Root Login
If attackers crack the root account, it’s game over.

✅ Safer approach:
- login with normal user
- use `sudo` for admin tasks

---

### 3) Change Default Port (Optional)
SSH default port = **22**  
Changing it doesn’t “secure” fully, but reduces random automated attacks.

---

### 4) Limit Login Attempts (Rate Limiting)
Stops brute force by blocking repeated failed logins.

Example tools:
- `fail2ban`
- firewall rules

---

### 5) Allow Only Specific Users
If only 1–2 users need SSH access, block the rest.

✅ Whitelisting users reduces attack surface.

---

### 6) Disable Password Login (after keys are set)
Best hardening step.

✅ Only allow SSH key login.

---

## 💻 Mini Practice / Commands
```bash
# Check SSH service status (Linux)
sudo systemctl status ssh

# Basic SSH login
ssh username@server-ip

# Generate SSH key pair
ssh-keygen -t ed25519

# Copy public key to server
ssh-copy-id username@server-ip
