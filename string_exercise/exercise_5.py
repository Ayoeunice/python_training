# Count all letters, digits, and special symbols from a given string
# Given:
#
# str1 = "P@#yn26at^&i5ve"
str1 = "P@#yn26at^&i5ve"

# Initialize counters for letters, digits, and special symbols
letter_count = 0
digit_count = 0
special_symbol_count = 0

# Iterate through each character in the string
for char in str1:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_symbol_count += 1

# Print the counts
print("Chars:", letter_count)
print("Digits:", digit_count)
print("Symbols:", special_symbol_count)
