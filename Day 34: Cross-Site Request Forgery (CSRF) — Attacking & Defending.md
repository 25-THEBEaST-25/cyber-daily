✅ Topic: Cross-Site Request Forgery (CSRF) — Attacking & Defending
1) What is CSRF?

CSRF (Cross-Site Request Forgery) is an attack where a victim is tricked into sending a request to a website where they are already logged in.

✅ The request is made using the victim’s session/cookies, so the website thinks it’s legit.

2) Why CSRF Works

CSRF works because:

Browser automatically attaches cookies

Victim is already authenticated

Server trusts the request only because cookies are present

3) Real Example (Easy to understand)

Victim is logged into bank.com
Attacker makes victim open a malicious page that silently triggers:

“Transfer money”

“Change password”

“Change email”

“Enable 2FA to attacker device”

Victim didn’t click “confirm” on bank.com, but browser still sent the request.

4) When CSRF is Dangerous

CSRF is most dangerous when:
✅ The action is state-changing (POST/PUT/DELETE)
✅ The app uses cookie-based authentication
✅ No extra verification exists (OTP / re-auth / token)

5) CSRF vs XSS (Quick Difference)

CSRF: Uses victim’s cookies to force a request

XSS: Runs attacker JS inside victim browser

🔥 XSS can sometimes bypass CSRF protections too.

✅ CSRF Defenses (Must Know)
1) CSRF Token (Best protection)

Server generates a random token and expects it in the request.

✅ Attacker cannot guess it
✅ Token must match session/user

Example:

form includes hidden input: csrf_token=...

2) SameSite Cookies

Cookie flags prevent cookies from being sent cross-site.

Recommended:

SameSite=Lax ✅ good default

SameSite=Strict ✅ strongest (but may break UX)

SameSite=None; Secure ✅ needed for cross-site usage

3) Check Origin / Referer Header

Server verifies request came from your domain.

✅ Useful extra layer
⚠️ Not the only layer (headers can be missing sometimes)

4) Require Re-auth / OTP for Critical Actions

For actions like:

changing password

changing email

enabling payments

✅ confirm via password / OTP / 2FA prompt

5) Avoid GET for State Change

❌ Wrong:
GET /transfer?to=attacker&amount=5000

✅ Right:
Use POST + token + confirmation

✅ Mini Checklist (Interview Ready)

✔ Cookie-based login? → CSRF risk high
✔ Token present? → strong protection
✔ SameSite cookies enabled? → major defense
✔ Critical actions require OTP? → reduces impact

🔥 Key Takeaway

CSRF is not “stealing your password” — it’s forcing actions using your already logged-in session.

✅ Quick Summary (1 line)

CSRF = attacker makes victim’s browser perform unauthorized actions on a trusted site using existing cookies.
