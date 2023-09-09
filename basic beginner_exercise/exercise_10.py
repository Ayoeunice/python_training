# Create a new list from two list using the following condition
# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such
# that the new list should contain odd numbers from the first list and even numbers from the second list.
# Given two lists of numbers
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Create a new list with odd numbers from list1 and even numbers from list2
result_list = [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0]

# Print the new list
print("Result list:", result_list)
