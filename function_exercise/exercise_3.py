# Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition
# and subtraction.
# Also, it must return both addition and subtraction in a single return call.
# Given:
# def calculation(a, b):
# Your Code
# res = calculation(40, 10)
# print(res)

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

res = calculation(40, 10)
print(res)