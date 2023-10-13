# Filter dictionary to contain keys present in the given list
# Given:
# Dictionary
# d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# Filter dict using following keys
# l1 = ['A', 'C', 'F']
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
l1 = ['A', 'C', 'F']

# Filter the dictionary using the keys in l1
filtered_dict = {key: d1[key] for key in l1 if key in d1}

# Print the filtered dictionary
print(filtered_dict)
