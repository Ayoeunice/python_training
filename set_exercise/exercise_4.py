# Update the first set with items that don’t exist in the second set
# Given two Python sets, write a Python program to
# update the first set with items that exist only in the first set and not in the second set.
# Given:
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
set1 = {10, 20, 30}
set2 = {20, 40, 50}

# Update set1 with items that exist only in set1 (not in set2) using the difference() method
set1.difference_update(set2)

# Print the updated set1
print(set1)

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# Update set1 with items that exist only in set1 (not in set2) using the - operator
# set1 -= set2

# Print the updated set1
# print(set1)

