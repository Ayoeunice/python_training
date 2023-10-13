# Display all duplicate items from a list
# Given:
# sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

# Create an empty list to store duplicate items
duplicates = []

# Create a set to keep track of items seen so far
seen = set()

# Iterate through the list
for item in sample_list:
    if item in seen and item not in duplicates:
        # If the item has been seen before but not already added to duplicates
        duplicates.append(item)
    else:
        seen.add(item)

# Print the list of duplicate items
print(duplicates)
