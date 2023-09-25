# Count the occurrence of each element from a list
# Write a program to iterate a given list and count the occurrence of each element
# and create a dictionary to show the count of each element.
# Given:
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Initialize an empty dictionary to store the counts
element_counts = {}

# Iterate through the list
for element in sample_list:
    # Check if the element is already in the dictionary
    if element in element_counts:
        # If yes, increment the count
        element_counts[element] += 1
    else:
        # If not, initialize the count to 1
        element_counts[element] = 1

# Print the dictionary with element counts
for element, count in element_counts.items():
    print(f"{element}: {count}")
