# Calculate the cube of all numbers from 1 to a given number
# Write a program to print the cube of all numbers from 1 to a given number
# Given:
# input_number = 6
# Get the input from the user
try:
    input_number = int(input("Enter a number: "))

    if input_number < 1:
        print("Please enter a positive integer.")
    else:
        print("Cubes of numbers from 1 to", input_number, ":")
        for num in range(1, input_number + 1):
            cube = num ** 3
            print(f"Current number is {num} : and the cube is {cube}")

except ValueError:
    print("Invalid input. Please enter a positive integer.")
