# Day 17: Input Validation & Sanitization

## What is Input Validation?
Ensuring user input matches expected format, type, and length before processing.

## What is Input Sanitization?
Cleaning or escaping input to remove harmful characters or code.

## Why It Matters
- Prevents XSS
- Prevents SQL Injection
- Prevents Command Injection

## Example: XSS
If user input is rendered without escaping, attackers can inject scripts.

## Best Practices
- Validate on backend, not only frontend
- Use allowlists instead of blocklists
- Escape output before rendering
- Use prepared statements for DB queries

## Real-World Impact
Many breaches happen due to trusting user input.
