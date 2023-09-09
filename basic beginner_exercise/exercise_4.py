# Remove first n characters from a string
string = input("Enter a string: ")

n = int(input("Enter the number of characters to remove: "))

if n <= len(string):

    result = string[n:]
    print("Result:", result)
else:
    print("Cannot remove more characters than the length of the string.")
