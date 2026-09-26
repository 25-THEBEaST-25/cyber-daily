# Day 23: Authentication vs Authorization – Understanding the Difference

Authentication and authorization are often used interchangeably, but they solve **two very different security problems**. Confusing them leads to serious vulnerabilities.

---

## 🔐 Authentication – Who are you?

Authentication is the process of **verifying identity**.

Examples:
- Entering username and password
- OTP verification
- Biometric login
- Token/session validation

In simple terms:
> Authentication answers: **“Are you really who you claim to be?”**

---

## 🛂 Authorization – What are you allowed to do?

Authorization determines **permissions after authentication**.

Examples:
- Can this user access the admin dashboard?
- Can this user delete another user’s data?
- Can this API endpoint be accessed with this role?

In simple terms:
> Authorization answers: **“What actions are you permitted to perform?”**

---

## 🧠 Key Difference (Important)

| Aspect | Authentication | Authorization |
|------|---------------|---------------|
| Purpose | Verify identity | Grant permissions |
| Happens | First | After authentication |
| Example | Login | Access control |
| Failure Risk | Account takeover | Privilege escalation |

**Being authenticated does NOT mean being authorized.**

---

## ⚠️ Common Developer Mistakes

- Assuming login = permission
- Missing role checks on sensitive endpoints
- Trusting client-side role data
- Not validating ownership of resources (IDOR)

These mistakes often lead to:
- Unauthorized data access
- Privilege escalation attacks
- Broken access control vulnerabilities

---

## 🧨 How Attackers Exploit This

- Accessing admin routes after normal login
- Modifying user IDs in URLs
- Bypassing role checks due to missing validation
- Reusing valid tokens for unauthorized actions

Broken authorization is one of the **most common real-world security issues**.

---

## 🛡️ How I Applied This in My Projects

- Clear separation between authentication and authorization logic
- Role-based checks before sensitive actions
- Account-level and IP-level restrictions
- Explicit permission validation instead of assumptions

This separation improves security and reduces logic flaws.

---

## 🚀 Key Takeaway

Authentication proves **who you are**.  
Authorization controls **what you can do**.

Treating them as separate concerns is essential for building secure systems.
