OWASP Top 10 Security Assignment

This project looks at ten vulnerable code examples based on the OWASP Top 10. For each example, I identified the security problem, changed the code to make it safer, and explained how the fix improves security.

1. Broken Access Control – JavaScript

Security Flaw:
The application trusts the user ID supplied in the URL without checking whether the current user has permission to view that profile. This could allow someone to change the ID and access another user's information.

Fix:
I changed the code so it uses the ID of the authenticated user instead of accepting a user ID from the URL.

How the Fix Improves Security:
This prevents users from changing the URL to access another person's profile and keeps access limited to their own account.

OWASP Reference:
OWASP A01: Broken Access Control
https://owasp.org/Top10/en/A01_2021-Broken_Access_Control/

2. Broken Access Control – Python

Security Flaw:
The application accepts an account ID from the URL and returns that account without checking whether the current user owns it.

Fix:
I added a login requirement and changed the code to use the authenticated user's ID.

How the Fix Improves Security:
The server now decides which account the user can access instead of trusting an ID supplied by the user.

OWASP Reference:
OWASP A01: Broken Access Control
https://owasp.org/Top10/en/A01_2021-Broken_Access_Control/

