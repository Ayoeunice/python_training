#  Delete the second column from a given array
#  and insert the following new column in its place.
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
# newColumn = numpy.array([[10,10,10]])


import numpy as np

# Define the sampleArray
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print("Original Array:")
print(sampleArray)
# Delete the second column (index 1) from the sampleArray
sampleArray1 = np.delete(sampleArray, 1, axis=1)

# Print the modified array
print("Array after deleting column 2 on axis 1:")
print(sampleArray1)

import numpy as np

# Define the sampleArray
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
# Define the newColumn
newColumn = np.array([[10, 10, 10]])

# Delete the second column from the sampleArray
sampleArray = np.delete(sampleArray, 1, axis=1)

# Insert the newColumn in place of the deleted column
sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)

# Print the updated sampleArray
print("Array after inserting column 2 on axis 1:")
print(sampleArray)
