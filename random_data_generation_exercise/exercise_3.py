# Generate 6 digit random secure OTP

import secrets

# Generate a 6-digit OTP
otp = ''.join([secrets.choice('0123456789') for i in range(6)])

print("6-digit secure OTP:", otp)

