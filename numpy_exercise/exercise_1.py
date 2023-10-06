# Create a 4X2 integer array and Prints its attributes
# Note: The element must be a type of unsigned int16. And print the following Attributes: –
# The shape of an array.
# Array dimensions.
# The Length of each element of the array in bytes.
# Expected Output:

# Printing Array

# [[64392 31655]
 # [32579     0]
 # [49248   462]
 #[    0     0]]

# Printing NumPy array Attributes

# Array Shape is:  (4, 2)
# Array dimensions are  2
# Length of each element of array in bytes is  2

import numpy as np

# Create the 4x2 integer array with uint16 elements
array = np.array([[64392, 31655], [32579, 0], [49248, 462], [0, 0]], dtype=np.uint16)

# Print the array
print("Printing Array")
print(array)

# Print the NumPy array attributes
print("\nPrinting NumPy array Attributes")
print("Array Shape is:", array.shape)
print("Array dimensions are", array.ndim)
print("Length of each element of array in bytes is", array.itemsize)

