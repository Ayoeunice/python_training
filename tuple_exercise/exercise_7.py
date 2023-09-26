# Modify the tuple
# Given is a nested tuple.
# Write a program to modify the first item (22) of a list inside a following tuple to 222
# Given:
# tuple1 = (11, [22, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)

# Convert the list inside the tuple to a mutable list
mutable_list = list(tuple1[1])

# Modify the first item of the list to 222
mutable_list[0] = 222

# Create a new tuple with the modified list
modified_tuple = (tuple1[0], mutable_list, tuple1[2], tuple1[3])

# Print the modified tuple
print(modified_tuple)
