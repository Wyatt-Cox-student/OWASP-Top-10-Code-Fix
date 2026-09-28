import hashlib
import secrets
import base64

def hash_password(password):
    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )

    salt_encoded = base64.b64encode(salt).decode()
    hash_encoded = base64.b64encode(password_hash).decode()

    return salt_encoded + ":" + hash_encoded


password = "ExamplePassword123"

hashed_password = hash_password(password)

print("Password:", password)
print("Stored Hash:", hashed_password)