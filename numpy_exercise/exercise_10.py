# Create two 2-D arrays and Plot them using matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Create the first 2-D array
array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Create the second 2-D array
array2 = np.array([[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])

# Create a figure with two subplots
plt.figure(figsize=(10, 5))

# Plot the first array in the first subplot
plt.subplot(1, 2, 1)
plt.imshow(array1, cmap='viridis')
plt.title('Array 1')

# Plot the second array in the second subplot
plt.subplot(1, 2, 2)
plt.imshow(array2, cmap='plasma')
plt.title('Array 2')

# Show the plots
plt.tight_layout()
plt.show()

