# Day 37 — MFA vs 2FA (and common bypasses)

## ✅ What is 2FA?
2FA = Two different factors used to login.
Example:
- Password (something you know)
- OTP on phone (something you have)

## ✅ What is MFA?
MFA = Multi-factor authentication (2 or more factors).
2FA is a type of MFA.

## 🔥 Factors of Authentication
1) Something you know → password / PIN  
2) Something you have → phone / OTP / authenticator app  
3) Something you are → fingerprint / face  
(Extra: somewhere you are → location sometimes)

## ✅ Stronger MFA options (best → ok)
✅ Passkeys / FIDO2 Security Key (best)  
✅ Authenticator App (TOTP)  
✅ Push approvals (ok but risky)  
⚠️ SMS OTP (weakest)

## ⚠️ Real-world bypasses (how attackers still break MFA)
- **Phishing OTPs** (fake login pages steal OTP)
- **MFA fatigue attacks** (spam push notifications until user clicks yes)
- **SIM swapping** (take control of your phone number → steal SMS OTP)
- **Session hijacking** (steal login session cookie after MFA)
- **Social engineering** (tricking support staff to reset MFA)

## ✅ Best Practices (defense)
- Prefer **passkeys / authenticator app**
- Use **anti-phishing login pages**
- Enable **device binding** and **trusted devices**
- Use **short session lifetime + secure cookies**
- Monitor suspicious login attempts & alerts

✅ Summary: MFA is strong, but not unbeatable. Real security comes from choosing strong MFA + securing sessions.
