# Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def calculate_product_or_sum(number1,number2):
    product = number1 * number2

    if product <= 1000:
        return product
    else:
        return number1 + number2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = calculate_product_or_sum(number1, number2)

print(f"The Result is : {result}")
