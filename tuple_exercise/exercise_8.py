# Sort a tuple of tuples by 2nd item
# Given:
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

# Sort the tuple of tuples by the second item (integer) in each inner tuple
sorted_tuple = tuple(sorted(tuple1, key=lambda x: x[1]))

# Print the sorted tuple
print(sorted_tuple)
