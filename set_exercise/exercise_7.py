# Check if two sets have any elements in common. If yes, display the common elements
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Find the common elements using the & operator
common_elements = set1 & set2

# Check if there are common elements and display them
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements.")
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# Find the common elements using the intersection() method
# common_elements = set1.intersection(set2)

# Check if there are common elements and display them
# if common_elements:
   # print("Common elements:", common_elements)
#else:
   # print("No common elements.")
