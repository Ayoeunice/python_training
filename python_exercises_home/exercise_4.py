# Reverse Dictionary mapping
# Given:
# ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

# Reverse the dictionary mapping
reversed_dict = {v: k for k, v in ascii_dict.items()}

# Print the reversed dictionary
print(reversed_dict)
