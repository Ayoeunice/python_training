# Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'History': 75
}

# Get the key with the minimum value using min() and a custom key function
key_with_minimum_value = min(sample_dict, key=lambda k: sample_dict[k])

# Print the key with the minimum value
print("Key with minimum value:", key_with_minimum_value)

