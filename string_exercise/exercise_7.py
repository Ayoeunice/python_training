# String characters balance Test
# Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.
# Given:
# Case 1:
# s1 = "Yn"
# s2 = "PYnative"

# Case 2:
# s1 = "Ynf"
# s2 = "PYnative"

def are_strings_balanced(s1, s2):
    # Convert both strings to lowercase for case-insensitive comparison
    s1 = s1.lower()
    s2 = s2.lower()

    # Create a dictionary to count characters in s2
    char_count = {}

    # Count characters in s2
    for char in s2:
        char_count[char] = char_count.get(char, 0) + 1

    # Check if all characters in s1 are present in s2
    for char in s1:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True

# Test cases
s1_case1 = "Yn"
s2_case1 = "PYnative"
s1_case2 = "Ynf"
s2_case2 = "PYnative"

result_case1 = are_strings_balanced(s1_case1, s2_case1)
result_case2 = are_strings_balanced(s1_case2, s2_case2)

# print("Case 1: Are s1 and s2 balanced?", result_case1)
# print("Case 2: Are s1 and s2 balanced?", result_case2)
print(result_case1)
print(result_case2)
