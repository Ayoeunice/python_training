# Generate a random Password which meets the following conditions
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string

# Define the characters to choose from
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

# Ensure at least 2 uppercase letters
uppercase_count = 2
password = random.choices(uppercase_letters, k=uppercase_count)

# Ensure at least 1 digit
digit_count = 1
password.extend(random.choices(digits, k=digit_count))

# Ensure at least 1 special symbol
special_symbol_count = 1
password.extend(random.choices(special_symbols, k=special_symbol_count))

# Fill the remaining characters with a combination of lowercase letters, digits, and symbols
remaining_count = 10 - (uppercase_count + digit_count + special_symbol_count)
password.extend(random.choices(lowercase_letters + digits + special_symbols, k=remaining_count))

# Shuffle the characters to randomize the password
random.shuffle(password)

# Convert the list of characters into a string
password = ''.join(password)

print("Random password:", password)

