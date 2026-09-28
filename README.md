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

3. Cryptographic Failures – Java

Security Flaw:
The code uses MD5 to hash passwords. MD5 is outdated and too fast for secure password storage, which makes password guessing attacks easier.

Fix:
I replaced MD5 with PBKDF2 and added a randomly generated salt to the password hash.

How the Fix Improves Security:
PBKDF2 is designed to make password guessing more difficult, and the random salt helps prevent attackers from using precomputed hashes against multiple passwords.

OWASP Reference:
OWASP A02: Cryptographic Failures
https://top10.owasp.org/2021/A02_2021-Cryptographic_Failures/

4. CryptographicFailures – Python

Security Flaw:
The code uses SHA-1 directly to hash passwords. SHA-1 is too fast and is not recommended for secure password storage.

Fix:
I replaced SHA-1 with PBKDF2 using SHA-256 and added a randomly generated salt.

How the Fix Improves Security:
PBKDF2 makes password guessing slower, while the random salt helps prevent attackers from using precomputed hashes against stored passwords.

OWASP Reference:
OWASP A02: Cryptographic Failures
https://top10.owasp.org/2021/A02_2021-Cryptographic_Failures/

5. Injection – Java SQL Injection
Security Flaw:
The program places the username directly into the SQL query. An attacker could enter SQL commands as input and possibly change what the query does.
Fix:
I replaced the normal SQL statement with a PreparedStatement and used a parameter for the username.
How the Fix Improves Security:
The database treats the username as data instead of executable SQL, which helps prevent SQL injection attacks.
OWASP Reference:
OWASP A03: Injection
https://top10.owasp.org/2021/A03_2021-Injection/

6. Injection – JavaScript NoSQL Injection
Security Flaw:
The application directly trusts the username sent through the query parameters. An attacker could send unexpected values or objects instead of a normal username.
Fix:
I added input validation to make sure the username is a string, uses allowed characters, and has a reasonable length.
How the Fix Improves Security:
Invalid or unexpected input is rejected before it reaches the database, reducing the chance of NoSQL injection.
OWASP Reference:
OWASP A03: Injection
https://top10.owasp.org/2021/A03_2021-Injection/

7. Insecure Design – Password Reset
Security Flaw:
The password reset system only requires an email address and a new password. Anyone who knows another user's email could potentially reset that person's password.
Fix:
I changed the design to require a temporary reset token and made sure the new password is securely hashed before being stored.
How the Fix Improves Security:
A user must now prove they received a valid reset token before changing the password, which helps prevent unauthorized password resets.
OWASP Reference:
OWASP A04: Insecure Design
https://owasp.org/Top10/en/A04_2021-Insecure_Design/

8. Software and Data Integrity Failures
Security Flaw:
The website loads a JavaScript file from an outside CDN without checking whether the file has been modified.
Fix:
I added Subresource Integrity, or SRI, so the browser can verify the file using a cryptographic hash before running it.
How the Fix Improves Security:
If the external JavaScript file is changed or compromised, the hash will no longer match and the browser can refuse to run it.
OWASP Reference:
OWASP A08: Software and Data Integrity Failures
https://top10.owasp.org/2021/A08_2021-Software_and_Data_Integrity_Failures/

9. Server-Side Request Forgery (SSRF)
Security Flaw:
The application sends a request to any URL entered by the user. This could allow someone to make the server request internal or restricted resources.
Fix:
I added an allowlist of approved websites, required HTTPS, disabled automatic redirects, and added a request timeout.
How the Fix Improves Security:
The server can now only make requests to approved destinations instead of blindly trusting URLs supplied by the user.
OWASP Reference:
OWASP A10: Server-Side Request Forgery
https://top10.owasp.org/2021/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/

10. Identification and Authentication Failures – Java

Security Flaw:
The original code directly compares the entered password to the stored password, which suggests that passwords may be stored in plain text.

Fix:
I changed the code to hash passwords using PBKDF2 with a random salt and verify the entered password against the stored hash.

How the Fix Improves Security:
The actual password is no longer stored directly. If the stored password data is stolen, attackers would only have the salted password hash instead of the original password.

OWASP Reference:
OWASP A07: Identification and Authentication Failures
https://top10.owasp.org/2021/A07_2021-Identification_and_Authentication_Failures/