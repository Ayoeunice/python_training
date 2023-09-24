# Write a program to count occurrences of all characters within a string
# Given:
# str1 = "Apple"

str1 = "Apple"

# Initialize an empty dictionary to store character counts
char_counts = {}

# Iterate through each character in the string
for char in str1:
    # If the character is already in the dictionary, increment its count
    if char in char_counts:
        char_counts[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        char_counts[char] = 1

# Print the character counts
for char, count in char_counts.items():
    print(f"'{char}': {count}")

