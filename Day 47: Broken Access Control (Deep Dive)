Day 47: Broken Access Control (Deep Dive)

🔐 What is Broken Access Control?
Broken Access Control occurs when a system fails to properly restrict what users can do or access.

👉 In simple words:
Users can access data or actions they should NOT be allowed to.

💥 Examples:
- Accessing another user's profile by changing ID
- Viewing admin panel without admin rights
- Editing/deleting data without permission

⚠️ Why it’s dangerous:
- Data leaks
- Unauthorized actions
- Full system compromise

🧠 Real-world scenario:
User changes:
GET /api/user/123 → /api/user/124

And gets someone else's data.

🚨 Types:
- IDOR (already covered)
- Missing role checks
- Privilege escalation
- Forced browsing (access hidden endpoints)

🛡️ Prevention:
- Always verify user permissions on backend
- Never trust frontend validation
- Use role-based access control (RBAC)
- Validate every request server-side

💡 Key Learning:
Authentication ≠ Authorization  
Just because a user is logged in doesn’t mean they can access everything.
