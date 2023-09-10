# Reverse a given integer number
try:
    x = int(input("Enter an integer: "))

    y = str(x)[::-1]

    reversed_num = int(y)

    print(f"The reversed integer is: {reversed_num}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
