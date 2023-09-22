# Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2,
# write a program to return a new string made of s1 and s2’s first, middle, and last characters.
# Given:
# s1 = "America"
# s2 = "Japan"

def extract_characters(input_str):
    if len(input_str) >= 3:
        first_char = input_str[0]
        middle_char_index = len(input_str) // 2
        middle_char = input_str[middle_char_index]
        last_char = input_str[-1]
        return first_char + middle_char + last_char
    else:
        return "Input string should have at least 3 characters."

s1 = "America"
s2 = "Japan"

new_string = extract_characters(s1) + extract_characters(s2)
print("New string:", new_string)
