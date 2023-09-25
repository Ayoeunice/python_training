# Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Use a list comprehension to remove empty strings
list1 = [item for item in list1 if item != ""]

# Print the updated list
print(list1)

