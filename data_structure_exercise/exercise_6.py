# Find the intersection (common) of two sets and remove those elements from the first set
# Given:
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Find the intersection of the two sets
intersection_set = first_set.intersection(second_set)

# Remove the common elements from the first set
first_set -= intersection_set
# second_set -= intersection_set
# Print the updated first_set
print("Updated first_set:", first_set)
# print("Updated second_set:", second_set)
print("Intersection set:", intersection_set)
