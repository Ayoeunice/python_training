# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7]
numbers = [1, 2, 3, 4, 5, 6, 7]

# Use a list comprehension to square each item
squared_numbers = [x ** 2 for x in numbers]

# Print the squared numbers
print(squared_numbers)
