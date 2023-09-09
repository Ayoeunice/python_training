# Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
# Function to check if a number is a palindrome
def is_palindrome(number):

    num_str = str(number)

    reversed_str = num_str[::-1]

    return num_str == reversed_str

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} yes. given number is a palindrome number.")
else:
    print(f"{num} no. given number is not a palindrome number.")
