# Update set1 by adding items from set2, except common items
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Update set1 by adding items from set2, except common items, using the difference() method
set1.update(set2.difference(set1))

# Print the updated set1
print(set1)
