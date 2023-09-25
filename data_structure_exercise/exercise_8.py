# Iterate a given list and
# check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# Given:
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

# Create a copy of the roll_number list to iterate over
# We create a copy to avoid modifying the list while iterating over it
roll_number_copy = roll_number.copy()

# Iterate through the copy of the list
for num in roll_number_copy:
    # Check if the element exists as a value in the dictionary
    if num not in sample_dict.values():
        # If it doesn't exist, remove it from the original list
        roll_number.remove(num)

# Print the updated roll_number list
print("After removing unwanted elements from the list:", roll_number)
