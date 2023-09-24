# Calculate the sum and average of the digits present in a string
# Given a string s1, write
# a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
# Given:
# str1 = "PYnative29@#8496"

str1 = "PYnative29@#8496"

# Initialize variables for sum and count of digits
digit_sum = 0
digit_count = 0

# Iterate through each character in the string
for char in str1:
    if char.isdigit():
        # If the character is a digit, add it to the sum and increment the count
        digit_sum += int(char)
        digit_count += 1

# Calculate the average (avoid division by zero)
average = digit_sum / digit_count if digit_count > 0 else 0

print("Sum is:", digit_sum, "Average is ", average)
# print("Average is :", average)

