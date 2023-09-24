# Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
# Given:
# str1 = "Emma25 is Data scientist50 and AI Expert"

import re

str1 = "Emma25 is Data scientist50 and AI Expert"

# Split the string into words
words = str1.split()

# Initialize a list to store words with both alphabets and numbers
words_with_alphabets_and_numbers = []

# Define a regular expression pattern for a word containing both alphabets and numbers
pattern = re.compile(r'[a-zA-Z]+\d+|\d+[a-zA-Z]+')

# Check each word in the list
for word in words:
    if pattern.match(word):
        words_with_alphabets_and_numbers.append(word)

# print("Words with both alphabets and numbers:", words_with_alphabets_and_numbers)
print(words_with_alphabets_and_numbers)
