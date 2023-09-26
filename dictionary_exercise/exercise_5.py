# Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# Given dictionary:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# Keys to extract
# keys = ["name", "salary"]

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

# Keys to extract
keys = ["name", "salary"]

# Create a new dictionary by extracting the specified keys
extracted_dict = {key: sample_dict[key] for key in keys}

# Print the extracted dictionary
print(extracted_dict)

