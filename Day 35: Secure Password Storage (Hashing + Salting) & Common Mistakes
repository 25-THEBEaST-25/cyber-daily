✅ Day 35: Secure Password Storage (Hashing + Salting) & Common Mistakes
🎯 Goal

Understand how passwords should be stored securely in real-world applications and what mistakes lead to leaks.

🔑 What is Password Hashing?

Password hashing means converting a password into a fixed-length string using a one-way function.

✅ One-way = you cannot get the original password back from the hash.

Example:
password123 → 5f4dcc3b5aa765d61d8327deb882cf99 (hash)

🧂 Why Salting is Important

A salt is a random string added to the password before hashing.

✅ Benefits of Salting:

Prevents same passwords having same hash

Protects against rainbow table attacks

Makes brute force harder

Example:
password123 + X9!aP → hash output changes completely

🔥 Why Plain Hashing is Still Not Enough

Even with hashing, attackers can brute-force quickly if hashing is fast.

So we use slow hashing algorithms designed for passwords:

✅ Recommended:

bcrypt

scrypt

Argon2 (best today)

🚫 Avoid for passwords:

MD5

SHA-1

SHA-256 (fast, not meant for password storage)

⚠️ Common Real-World Mistakes

❌ Storing passwords in plaintext
❌ Using MD5/SHA without salt
❌ Same salt for every user
❌ Low cost factor in bcrypt (too fast)
❌ Logging passwords in console/server logs

✅ Best Practices

✅ Hash + Salt every password
✅ Use bcrypt/Argon2 with proper cost
✅ Store only hash (never store original password)
✅ Apply rate limiting + lockouts to stop brute force
✅ Use password policies + strength checks

💡 Mini Takeaway

Passwords should never be reversible.
If the database leaks, the attacker should still struggle hard to crack user passwords.

✅ What I’ll do next

Implement bcrypt hashing + verification in a login system

Add password strength validation

Add rate limiting to stop brute-force attacks
