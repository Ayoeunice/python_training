# Write a program to print multiplication table of a given number
# Get the input from the user
try:
    num = int(input("Enter a number to print its multiplication table: "))

    #print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        product = num * i
        print(product)
        #print(f"{num} x {i} = {product}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

