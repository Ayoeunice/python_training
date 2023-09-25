# Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list,
# and if it is present, replace it with 200. Only update the first occurrence of an item.
# Given:
# list1 = [5, 10, 15, 20, 25, 50, 20]
list1 = [5, 10, 15, 20, 25, 50, 20]

# Find the index of the first occurrence of 20 in the list
index_to_replace = list1.index(20)

# Replace the value at the found index with 200
list1[index_to_replace] = 200

# Print the updated list
print(list1)
