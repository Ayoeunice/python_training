# Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
# Expected Output:
#
# Creating 5X2 array using numpy.arange
# [[100 110]
#  [120 130]
#  [140 150]
#  [160 170]
#  [180 190]]

import numpy as np

# Create a 5x2 array with elements from 100 to 200 with a step of 10
array = np.arange(100, 200, 10).reshape(5, 2)

# Print the array
print("Creating 5X2 array using numpy.arange")
print(array)
