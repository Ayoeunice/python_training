# Find the factorial of a given number
# Get the input from the user
try:
    num = int(input("Enter a positive integer: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(factorial)
        #print(f"The factorial of {num} is: {factorial}")

except ValueError:
    print("Invalid input. Please enter a positive integer.")
