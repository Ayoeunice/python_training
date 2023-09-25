# Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:
# speed =
# {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# Initialize an empty list to store unique values
unique_values = []

# Iterate through the values of the dictionary
for value in speed.values():
    # Check if the value is not already in the unique_values list
    if value not in unique_values:
        # If not, add it to the list
        unique_values.append(value)

# Print the list of unique values
print("Unique values:", unique_values)
