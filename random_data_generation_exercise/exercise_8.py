# Generate random secure token of 64 bytes and random URL

import secrets
import string

# Generate a random secure token of 64 bytes
secure_token = secrets.token_hex(32)

# Generate a random URL (assuming https://eunice.com as the base)
base_url = "https://eunice.com/"
random_path = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))
random_url = base_url + random_path

print("Random Secure Token (64 bytes):", secure_token)
print("Random URL:", random_url)
