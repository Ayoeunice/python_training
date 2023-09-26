# Add a list of elements to a set
# Given a Python list, Write a program to add all its elements into a given set.
# Given:
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

# Use the update() method to add elements from the list to the set
sample_set.update(sample_list)

# Print the updated set
print(sample_set)
