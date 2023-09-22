# Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given:
# str1 = PyNaTive
str1 = "PyNaTive"

# Split the string into lowercase and uppercase characters
#lowercase_chars = [char for char in str1 if char.islower()]
#uppercase_chars = [char for char in str1 if char.isupper()]

# Sort the lowercase and uppercase characters
#lowercase_chars.sort()
#uppercase_chars.sort()

# Combine the sorted lowercase and uppercase characters
#sorted_str1 = ''.join(lowercase_chars + uppercase_chars)

#print("Arranged string:", sorted_str1) output aeivyNPT

str1 = "PyNaTive"

# Separate lowercase and uppercase letters
lowercase_chars = [char for char in str1 if char.islower()]
uppercase_chars = [char for char in str1 if char.isupper()]

# Concatenate the lowercase and uppercase characters
arranged_str1 = ''.join(lowercase_chars + uppercase_chars)

print("Arranged string:", arranged_str1)


