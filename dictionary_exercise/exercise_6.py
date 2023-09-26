# Delete a list of keys from a dictionary
# Given:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# Keys to remove
# keys = ["name", "salary"]

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

# Keys to remove
keys = ["name", "salary"]

# Use a dictionary comprehension to create a new dictionary without the specified keys
sample_dict = {key: value for key, value in sample_dict.items() if key not in keys}

# Print the updated dictionary
print(sample_dict)
