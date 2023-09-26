# Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary.
# Sometimes it is required to check if the given value is present.
# Write a Python program to check if value 200 exists in the following dictionary.
# Given:
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
sample_dict = {'a': 100, 'b': 200, 'c': 300}

# Value to check
value_to_check = 200

# Check if the value exists in the dictionary's values
if value_to_check in sample_dict.values():
    print(f"{value_to_check}  present in a dict.")
else:
    print(f"{value_to_check} does not exist in the dictionary values.")
