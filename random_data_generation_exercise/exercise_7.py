# Calculate multiplication of two random float numbers
# Note:
# First random float number must be between 0.1 and 1
# Second random float number must be between 9.5 and 99.5

import random

# Generate the first random float number between 0.1 and 1
x = random.uniform(0.1, 1)

# Generate the second random float number between 9.5 and 99.5
y = random.uniform(9.5, 99.5)

# Calculate the multiplication
result = x * y

print(f"Random Float Number 1: {x}")
print(f"Random Float Number 2: {y}")
print(f"Multiplication Result: {result}")
