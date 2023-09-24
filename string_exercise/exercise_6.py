# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next,
# the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
# Given:
# s1 = "Abc"
# s2 = "Xyz"

s1 = "Abc"
s2 = "Xyz"

# Initialize an empty string for s3
s3 = ""

# Initialize indices for iterating through s1 and s2
index_s1 = 0
index_s2 = len(s2) - 1

# Iterate through both s1 and s2 in parallel
while index_s1 < len(s1) and index_s2 >= 0:
    # Add the character from s1 and s2 to s3 as per the rules
    s3 += s1[index_s1] + s2[index_s2]

    # Move the indices
    index_s1 += 1
    index_s2 -= 1

# If there are any leftover characters in s1, add them to s3
while index_s1 < len(s1):
    s3 += s1[index_s1]
    index_s1 += 1

# If there are any leftover characters in s2, add them to s3
while index_s2 >= 0:
    s3 += s2[index_s2]
    index_s2 -= 1

print("Mixed string:", s3)

