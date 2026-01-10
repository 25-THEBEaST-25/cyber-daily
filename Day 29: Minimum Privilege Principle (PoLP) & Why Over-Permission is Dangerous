 Day 29
Topic: Minimum Privilege Principle (PoLP) & Why Over-Permission is Dangerous
📌 What is the Principle of Least Privilege (PoLP)?

The Principle of Least Privilege states that a user, system, or process should have only the minimum permissions required to perform its task — nothing more.

This applies to:

Users

Applications

Services

Databases

Cloud resources

APIs

🚨 Why Over-Permission is a Serious Security Risk

Granting excessive permissions can lead to:

Privilege escalation

Lateral movement inside systems

Data breaches

Complete system compromise if one account is breached

Attackers don’t need admin access initially — they exploit over-perissioned accounts.

🧠 Real-World Example

A web app runs with admin DB access

Attacker exploits SQL Injection

Result:
❌ Full database dump
❌ Table deletion
❌ User credential theft

If PoLP was followed:

Read-only access → limited damage

⚙️ Common Violations of PoLP

Applications running as root

Using shared admin credentials

Cloud IAM roles with *:* permissions

Developers given production access unnecessarily

APIs exposing write/delete permissions by default

✅ Best Practices to Implement PoLP

Grant role-based access (RBAC)

Use separate accounts for admin and normal usage

Restrict database users to required operations (READ / WRITE)

Rotate credentials regularly

Review and audit permissions periodically

Apply temporary privilege elevation when needed

🛡️ Security Takeaway

Most breaches don’t happen because of zero-days — they happen because someone had more access than they should.

Least Privilege:

Limits blast radius

Reduces attacker impact

Makes systems resilient even after compromise
