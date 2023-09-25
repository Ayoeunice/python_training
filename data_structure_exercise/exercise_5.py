# Create a Python set such that it shows the element from both lists in a pair
# Given:
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

# Create a set of pairs using a set comprehension
pairs_set = {(x, y) for x, y in zip(first_list, second_list)}

# Print the set of pairs
print(pairs_set)
