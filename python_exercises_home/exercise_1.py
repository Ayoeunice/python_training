# Reverse each word of a string
# Given:
# str = 'My Name is Jessa'
str = 'My Name is Jessa'
# Split the string into words
words = str.split()

# Reverse each word and store in a list
reversed_words = [word[::-1] for word in words]

# Join the reversed words back into a string
reversed_str = ' '.join(reversed_words)

# Print the reversed string
print(reversed_str)
