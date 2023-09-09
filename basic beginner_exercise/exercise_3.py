# Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

string = input("Enter a string: ")
# Iterate over the string and print characters at even index positions
for index in range(0, len(string), 2):
    print(string[index], end=' ')

print()  # Print a newline to format the output

