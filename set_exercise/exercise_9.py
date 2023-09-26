# Remove items from set1 that are not common to both set1 and set2
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Remove items from set1 that are not common to both set1 and set2 using the &= operator
set1 &= set2

# Print the updated set1
print(set1)
