# Day 4: Why SQL Injection Is Dangerous (Real-World Impact) (hehe didn't post for 2 days was busy)

Today I learned why SQL Injection is considered one of the most dangerous web application vulnerabilities.

SQL Injection happens when a hacker is able to insert malicious SQL queries into input fields like login forms, search boxes, or URLs. If a website does not properly validate user input, the attacker can directly talk to the database.

## Why It Is So Dangerous

- Hackers can bypass login systems without knowing the password.
- Entire databases can be leaked including usernames, emails, and passwords.
- Data can be modified or deleted.
- Admin access can be gained.
- Some attacks even let hackers take control of the server.

## Real-World Example

In many old websites, attackers used SQL Injection to extract millions of user records. This included personal data, emails, and even payment details. These breaches happened only because developers trusted user input.

## Key Lesson

Any application that takes user input and connects to a database must:
- Use prepared statements
- Sanitize user inputs
- Never directly insert user input into SQL queries

SQL Injection teaches us that even small coding mistakes can lead to massive security disasters.
