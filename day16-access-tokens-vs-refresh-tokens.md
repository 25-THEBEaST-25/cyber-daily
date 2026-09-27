# Day 16: Access Tokens vs Refresh Tokens

Modern authentication systems use **two types of tokens** to balance
security and user experience: **Access Tokens** and **Refresh Tokens**.

---

## What is an Access Token?
- Short-lived token (minutes)
- Sent with every API request
- Proves the user is authenticated
- If leaked, damage is limited due to short expiry

---

## What is a Refresh Token?
- Long-lived token (days or weeks)
- Used only to obtain a new access token
- Never sent with normal API requests
- Stored securely (usually HttpOnly cookies)

---

## Why Are Both Needed?
If access tokens never expired, stolen tokens would be dangerous.
If tokens expired too quickly, users would need to log in repeatedly.

Using both:
- Access tokens keep APIs secure
- Refresh tokens keep users logged in seamlessly

---

## Real-World Authentication Flow
1. User logs in successfully
2. Server issues an access token + refresh token
3. Access token expires after a short time
4. Client sends refresh token to get a new access token
5. User stays logged in without re-entering credentials

---

## Security Best Practices
- Keep access tokens short-lived
- Store refresh tokens in HttpOnly cookies
- Rotate refresh tokens after use
- Revoke refresh tokens on logout or suspicious activity
- Never store refresh tokens in localStorage

---

## Key Takeaway
Access tokens protect APIs.  
Refresh tokens protect user experience.
