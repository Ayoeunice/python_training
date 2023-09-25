# Remove and add item in a list
# Write a program to remove the item present at index 4 and
# add it to the 2nd position and at the end of the list.
# Given:
# list1 = [54, 44, 27, 79, 91, 41]
# Expected Output:
#
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

list1 = [54, 44, 27, 79, 91, 41]

# Remove the item at index 4 and store it in a variable
removed_item = list1.pop(4)

# Print the list after removing the element at index 4
print("List After removing element at index 4", list1)

# Add the removed item to the 2nd position (index 2)
list1.insert(2, removed_item)

# Print the list after adding the element at index 2
print("List after Adding element at index 2", list1)

# Add the removed item to the end of the list
list1.append(removed_item)

# Print the list after adding the element at the last position
print("List after Adding element at last", list1)
