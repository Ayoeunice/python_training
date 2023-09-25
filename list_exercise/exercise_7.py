# Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Find the sublist containing 6000
sublist = list1[2][2]

# Check if 6000 is in the sublist
if 6000 in sublist:
    # Find the index of 6000 in the sublist
    index = sublist.index(6000)

    # Insert 7000 after 6000
    sublist.insert(index + 1, 7000)

# Print the updated list
print(list1)
