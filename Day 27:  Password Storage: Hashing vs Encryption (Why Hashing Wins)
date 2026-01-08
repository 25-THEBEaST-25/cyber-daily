🔐 Password Storage: Hashing vs Encryption (Why Hashing Wins)
📌 Problem

Storing passwords insecurely is one of the most common and dangerous mistakes in applications.
If passwords are stored improperly and the database is leaked, users are instantly compromised.

🔍 Hashing vs Encryption
🔐 Hashing

One-way process (cannot be reversed)

Same input → same output

Designed for verification, not recovery

Used for: Password storage

Examples:

bcrypt ✅

Argon2 ✅

PBKDF2 ✅

🔑 Encryption

Two-way process (can be decrypted)

Requires a secret key

Designed for data recovery

Used for: Sensitive data like:

API keys

Aadhaar numbers

Credit card details

❌ Never for passwords

⚠️ Why Passwords Must NOT Be Encrypted

If passwords are encrypted:

The decryption key exists

If the key leaks → all passwords are exposed

One breach = total account takeover

This is why hashing is mandatory.

🧂 Salting (Critical Concept)

A salt is random data added to a password before hashing.

Why it matters:

Prevents rainbow table attacks

Makes identical passwords hash differently

Protects against precomputed attacks

Example:

password123 + random_salt → hash


bcrypt and Argon2 handle salting automatically ✅

🛡️ Best Practices

✅ Use bcrypt / Argon2

❌ Never store plaintext passwords

❌ Never use reversible encryption for passwords

❌ Avoid fast hashes like MD5 / SHA-1 / SHA-256 alone

✅ Add rate limiting & account lockout on login

🧠 Real-World Insight

Many major breaches didn’t happen because hackers were smart —
they happened because passwords were stored poorly.

Strong password storage can turn a breach into a non-event.
