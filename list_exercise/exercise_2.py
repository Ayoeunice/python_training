# Concatenate two lists index-wise
# Write a program to add two lists index-wise.
# Create a new list that contains the 0th index item from both the list, then the 1st index item, and
# so on till the last element. any leftover items will get added at the end of the new list.
# Given:
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Initialize an empty list to store the concatenated result
concatenated_list = []

# Determine the length of the shorter list
min_length = min(len(list1), len(list2))

# Iterate through both lists simultaneously and concatenate items
for i in range(min_length):
    concatenated_item = list1[i] + list2[i]
    concatenated_list.append(concatenated_item)

# Add any leftover items from the longer list to the end
if len(list1) > len(list2):
    concatenated_list.extend(list1[min_length:])
else:
    concatenated_list.extend(list2[min_length:])

# Print the concatenated list
print(concatenated_list)
