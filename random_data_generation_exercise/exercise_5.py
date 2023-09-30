# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only.
# No numbers and a special symbol.

import random
import string

# Define the characters to choose from
characters = string.ascii_letters

# Generate a random string of length 5
random_string = ''.join(random.choice(characters) for _ in range(5))

print("Random string:", random_string)
