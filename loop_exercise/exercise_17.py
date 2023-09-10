# Find the sum of the series up to n terms
# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
# Given:
# number of terms
# n = 5

# Get the input for the number of terms (n)
try:
    n = int(input("Enter the number of terms (n): "))

    if n < 1:
        print("Please enter a positive integer.")
    else:
        term = int('2')
        series_sum = 0

        for i in range(n):
            series_sum += term
            term = term * 10 + 2

        print(f"The sum of the series up to {n} terms is: {series_sum}")

except ValueError:
    print("Invalid input. Please enter a positive integer.")
