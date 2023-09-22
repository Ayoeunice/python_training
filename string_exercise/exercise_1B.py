# Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.
# Given:
# Case 1
# str1 = "JhonDipPeta"
# Output
# Dip
# Case 2
# str2 = "JaSonAy"
# Output
# Son
def get_middle_three_chars(input_str):
    # Check if the length of the input string is at least 3 characters
    if len(input_str) >= 3:
        # Calculate the starting index for the middle three characters
        start_index = (len(input_str) - 3) // 2

        # Extract the middle three characters using slicing
        middle_three_chars = input_str[start_index : start_index + 3]

        return middle_three_chars
    else:
        return "Input string should have at least 3 characters."

# Test cases
str1 = "JhonDipPeta"
str2 = "JaSonAy"

result1 = get_middle_three_chars(str1)
result2 = get_middle_three_chars(str2)

print("Case 1 Output:", result1)
print("Case 2 Output:", result2)
