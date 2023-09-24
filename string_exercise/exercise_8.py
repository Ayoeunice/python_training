# Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
# Given:
# str1 = "Welcome to USA. usa awesome, isn't it?"
import re

str1 = "Welcome to USA. usa awesome, isn't it?"

# Use regular expression to find all occurrences of "USA" (case-insensitive)
pattern = re.compile(r'usa', re.IGNORECASE)
occurrences = pattern.findall(str1)

# Count the number of occurrences
count = len(occurrences)

print("The USA count is:", count)


