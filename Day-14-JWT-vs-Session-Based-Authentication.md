# Day 14: JWT vs Session-Based Authentication

## Session-Based Authentication
- Server creates a session after login
- Session ID stored in cookies
- Server stores session data

### Pros
- Easy to revoke sessions
- More control on server side

### Cons
- Server memory usage
- Harder to scale horizontally

---

## JWT (JSON Web Token) Authentication
- Token issued after login
- Stored on client (cookie / localStorage)
- Server does NOT store session

### Pros
- Stateless (great for scaling)
- Fast authentication

### Cons
- Hard to revoke before expiry
- Token theft = full access until expiry

---

## Key Differences

| Feature | Session | JWT |
|------|------|-----|
| Server Storage | Yes | No |
| Stateless | No | Yes |
| Scalability | Medium | High |
| Revocation | Easy | Hard |

---

## Security Notes
- JWT should be short-lived
- Always use HTTPS
- Store JWT in HttpOnly cookies (not localStorage)
- Rotate secrets regularly

---

## When to Use What?
- Small apps → Sessions
- Large distributed systems → JWT
- High security → Sessions + strict controls
