# Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
# Given:
# str1 = "Emma is a data scientist who knows Python. Emma works at google."

str1 = "Emma is a data scientist who knows Python. Emma works at google."

# Find the last position of the substring "Emma"
last_position = str1.rfind("Emma")

if last_position != -1:
    print("Last position of 'Emma':", last_position)
else:
    print("Substring 'Emma' not found in the string.")

