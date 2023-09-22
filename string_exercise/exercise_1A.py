# Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
# Given:
# str1 = "James"

str1 = "James"

# Check if the length of the input string is at least 3 characters
if len(str1) >= 3:
    # Get the first character using str1[0]
    first_character = str1[0]

    # Calculate the index of the middle character
    middle_index = len(str1) // 2

    # Get the middle character using str1[middle_index]
    middle_character = str1[middle_index]

    # Get the last character using str1[-1]
    last_character = str1[-1]

    # Create a new string using the first, middle, and last characters
    new_string = first_character + middle_character + last_character

    print("New string:", new_string)
else:
    print("Input string should have at least 3 characters.")
