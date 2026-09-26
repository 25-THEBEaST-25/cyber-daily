🔹 1. What is IDOR?
Accessing data by changing IDs (user_id, order_id, etc.)
Happens due to missing authorization checks
🔹 2. Simple Example
GET /api/user/123   → Your profile
GET /api/user/124   → Someone else’s profile 
🔹 3. Real-Life Impact
View/edit other users’ data
Account takeover (sometimes)
Financial/data breaches
🔹 4. Why it Happens
Devs check authentication but not authorization
Trusting user input too much
🔹 5. How Attackers Find It
Change IDs in URL
Intercept requests (Burp Suite mindset)
Try sequential IDs (1,2,3…)
🔹 6. Prevention
Always verify ownership on backend
Use indirect references (UUIDs)
Implement proper access control checks
