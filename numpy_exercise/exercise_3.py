# Following is the provided numPy array. Return array of items by taking the third column from all rows
# sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
# Expected Output:
# Printing Input Array
# [[11 22 33]
#  [44 55 66]
#  [77 88 99]]
# Printing array of items in the third column from all rows

import numpy as np

# Define the sampleArray
sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# Print the input array
print("Printing Input Array")
print(sampleArray)

# Extract the third column using array slicing
third_column = sampleArray[:, 2]

# Print the array of items in the third column from all rows
print("Printing array of items in the third column from all rows")
print(third_column)
