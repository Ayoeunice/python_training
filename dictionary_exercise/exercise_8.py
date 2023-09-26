# Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
# Given:
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

# Rename the key "city" to "location"
sample_dict["location"] = sample_dict.pop("city")

# Print the updated dictionary
print(sample_dict)


