# Return array of odd rows and even columns from below numpy array
# sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
# Expected Output:
# Printing Input Array
# [[ 3  6  9 12]
#  [15 18 21 24]
#  [27 30 33 36]
#  [39 42 45 48]
#  [51 54 57 60]]
# Printing array of odd rows and even columns
# [[ 6 12]
#  [30 36]
#  [54 60]]

import numpy as np

# Define the sampleArray
sampleArray = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])

# Print the input array
print("Printing Input Array")
print(sampleArray)

# Extract odd rows and even columns using array slicing
odd_rows_even_columns = sampleArray[::2, 1::2]

# Print the array of odd rows and even columns
print("Printing array of odd rows and even columns")
print(odd_rows_even_columns)
