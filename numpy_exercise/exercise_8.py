# Print max from axis 0 and min from axis 1 from the following 2-D array.
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

import numpy as np

# Define the sampleArray
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print("Printing Original Array:")
print(sampleArray)
# Find the maximum along axis 0 (maximum values for each column)
max_values_axis0 = np.max(sampleArray, axis=0)

# Find the minimum along axis 1 (minimum values for each row)
min_values_axis1 = np.min(sampleArray, axis=1)

# Print the maximum values along axis 0
print("Printing amax Of Axis 0:")
print(max_values_axis0)

# Print the minimum values along axis 1
print("\n Printing amin Of Axis 1:")
print(min_values_axis1)

