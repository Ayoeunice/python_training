# Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

try:
    num = int(input("Enter number: "))

    if num < 1:
        print("Please enter a positive integer.")
    else:
        total = 0

        for i in range(1, num + 1):
            total += i

        print(f"The sum  is: {total}")

except ValueError:
    print("Invalid input. Please enter a positive integer.")
