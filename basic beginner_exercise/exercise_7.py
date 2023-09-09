# Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.
input_string = "Emma is a good developer. Emma is also a writer."

substring = "Emma"

count = input_string.count(substring)

print(f" '{substring}' appeared {count} times ")
