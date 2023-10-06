# Roll dice in such a way that every time you get the same number
# Dice has 6 numbers (from 1 to 6).
# Roll dice in such a way that every time you must get the same output number. do this 5 times.

# Import the random module
import random

# Set the desired number
desired_number = 5

# Roll the die 5 times, getting the same number each time
for _ in range(5):
    result = desired_number
    print("Roll {}: {}".format(_ + 1, result))
