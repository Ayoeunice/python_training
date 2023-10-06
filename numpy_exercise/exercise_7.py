# Sort following NumPy array
# Case 1: Sort array by the second row
# Case 2: Sort the array by the second column
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

import numpy as np

# Define the sampleArray
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
# print the original Array
print(" Original Array :")
print(sampleArray)
# Sort the array by the second row
sortedArrayBySecondRow = sampleArray[:, sampleArray[1, :].argsort()]

# Print the sorted array
print("Sorting Original Array by Second Row:")
print(sortedArrayBySecondRow)
import numpy as np

# Define the sampleArray
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Sort the array by the second column
sortedArrayBySecondColumn = sampleArray[sampleArray[:, 1].argsort()]

# Print the sorted array
print("Sorting Original Array by Second Column:")
print(sortedArrayBySecondColumn)
