# Generate 3 random integers between 100 and 999 which is divisible by 5

import random

random_integers = []

# Generate 3 random integers
while len(random_integers) < 3:
    x = random.randint(100, 999)
    if x % 5 == 0:
        random_integers.append(x)

# Print the generated random integers
print(random_integers)
