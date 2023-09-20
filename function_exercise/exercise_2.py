# Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.
#Function call:
# call function with 3 arguments
#func1(20, 40, 60)

# call function with 2 arguments
#func1(80, 100)

def func1(*args):
    for arg in args:
        print(arg)

# Call the function with 3 arguments
func1(20, 40, 60)

func1(80, 100)

