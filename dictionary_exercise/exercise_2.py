# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Use the update() method to merge dict2 into dict1
dict1.update(dict2)

# Print the merged dictionary (dict1)
print(dict1)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Use dictionary unpacking to merge dict2 into dict1 (Python 3.5+)
# merged_dict = {**dict1, **dict2}

# Print the merged dictionary (merged_dict)
# print(merged_dict)

