# Create a result array by adding the following two NumPy arrays.
# Next, modify the result array by calculating the square of each element
# arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
# arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

import numpy as np

# Define the arrays
arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

# Add the two arrays to create a result array
resultArray = arrayOne + arrayTwo

# Print the result array before modification
print("Result Array (Before Modification):")
print(resultArray)

# Calculate the square of each element in the result array
resultArraySquared = resultArray ** 2

# Print the result array after modification (squared elements)
print("\nResult Array (After Squaring):")
print(resultArraySquared)
