# Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them
# into a dictionary in a way that item from list1 is the key and item from list2 is the value
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Create a dictionary using a dictionary comprehension
result_dict = {keys[i]: values[i] for i in range(len(keys))}

# Print the resulting dictionary
print(result_dict)
