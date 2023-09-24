# Removal all characters from a string except integers
# Given:
# str1 = 'I am 25 years and 10 months old'
str1 = 'I am 25 years and 10 months old'

# Initialize an empty string to store the digits
digits_only = ''

# Iterate through each character in the string
for char in str1:
    # Check if the character is a digit
    if char.isdigit():
        digits_only += char

# print("String with only integers:", digits_only)
print(digits_only)
