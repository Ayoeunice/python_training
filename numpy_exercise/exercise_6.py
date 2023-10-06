# Split the array into four equal-sized sub-arrays
# Note: Create an 8X3 integer array from a range between 10 to 34
# such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.

import numpy as np

# Create an 8x3 integer array from a range between 10 to 34
array = np.arange(10, 34).reshape(8, 3)

# Print the original array
print("Original Array:")
print(array)

# Split the array into four equal-sized sub-arrays
sub_arrays = np.array_split(array, 4)

# Print the sub-arrays
print("\nSub-Arrays:")
for i, sub_array in enumerate(sub_arrays):
    print(f"Sub-Array {i + 1}:")
    print(sub_array)
