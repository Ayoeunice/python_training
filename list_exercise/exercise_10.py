# Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# Given:
# list1 = [5, 20, 15, 20, 25, 50, 20]
list1 = [5, 20, 15, 20, 25, 50, 20]

# Use a list comprehension to create a new list without the item 20
list1 = [item for item in list1 if item != 20]

# Print the updated list
print(list1)
