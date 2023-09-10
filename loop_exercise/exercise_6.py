# Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.
# Get the input number from the user
try:
    number = int(input("Enter a number: "))
    count = 0

    if number == 0:
        count = 1

    while number != 0:
        number = number // 10
        count += 1

    print(f"The total number of digits is: {count}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

