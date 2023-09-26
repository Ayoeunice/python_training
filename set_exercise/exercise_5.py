# Remove items from the set at once
# Write a Python program to remove items 10, 20, 30 from the following set at once.
# Given:
# set1 = {10, 20, 30, 40, 50}

set1 = {10, 20, 30, 40, 50}

# Create a set containing items to remove
items_to_remove = {10, 20, 30}

# Remove the items from set1 using difference_update()
set1.difference_update(items_to_remove)

# Print the updated set1
print(set1)
