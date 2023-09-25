# Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:
#
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# Remove duplicates and create a list of unique items
unique_items = list(set(sample_list))

# Create a tuple from the unique items
unique_tuple = tuple(unique_items)

# Find the minimum and maximum numbers in the tuple
min_number = min(unique_tuple)
max_number = max(unique_tuple)

# Print the results
print("unique items:", unique_items)
print("tuple:", unique_tuple)
print("min:", min_number)
print("max:", max_number)
