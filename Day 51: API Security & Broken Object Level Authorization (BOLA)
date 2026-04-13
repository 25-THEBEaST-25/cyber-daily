# Day 51: API Security & Broken Object Level Authorization (BOLA)

## 🚀 What is API Security?
APIs (Application Programming Interfaces) are the backbone of modern applications.  
They allow communication between frontend and backend systems.

If APIs are not secured properly, attackers can directly access sensitive data **without even using the UI**.

---

## ⚠️ What is BOLA (Broken Object Level Authorization)?

Broken Object Level Authorization (BOLA) is a vulnerability where:

> A user can access or modify resources (data) that do not belong to them by simply changing an ID.

---

## 💣 Example Attack

```http
GET /api/user/123

If an attacker changes the ID:
  GET /api/user/124
  And gets another user’s data → BOLA vulnerability exists

🔥 Why is it Dangerous?
Very common in APIs
Easy to exploit
Can lead to:
Data leakage
Account takeover
Privacy violations
🧠 Root Cause

The backend does not verify ownership of the resource

It trusts user input like:

user ID
order ID
account ID
🛠️ Vulnerable Code Example
@app.route('/api/user/<id>')
def get_user(id):
    return db.get_user(id)

❌ No authorization check
❌ Anyone can access any user’s data

✅ Secure Code Example
@app.route('/api/user/<id>')
def get_user(id):
    if current_user.id != id:
        return "Unauthorized", 403
    return db.get_user(id)

✔️ Verifies user ownership
✔️ Prevents unauthorized access

🛡️ Prevention Techniques
Always perform authorization checks on backend
Never trust client-side validation
Use authentication tokens (JWT / sessions)
Implement Role-Based Access Control (RBAC)
Log and monitor suspicious requests
🧪 How Attackers Test This
Modify IDs in API requests
Use tools like Burp Suite
Try sequential ID enumeration (1,2,3,4...)
🧩 Real-World Reference

OWASP API Security Top 10:

API1: Broken Object Level Authorization
💡 Key Takeaway

Security is not just about authentication (who you are),
but also authorization (what you are allowed to access).

📝 Commit Note

Day 51: Learned API Security & BOLA (Broken Object Level Authorization)

Understood ID-based access vulnerabilities
Explored real-world attack scenarios
Implemented secure authorization checks
Studied OWASP API Top 10 concept
💬 Personal Note

Even if I wasn’t perfectly consistent earlier, today I focused on depth.
Understanding real-world vulnerabilities like BOLA makes me stronger in cybersecurity.
