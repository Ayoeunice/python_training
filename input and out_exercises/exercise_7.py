# Accept any three string from one input() call
# Accept multiple strings as input and split them into a list
input_string = input("Enter three Names Emma Jessa Kelly: ")
strings = input_string.split()
if len(strings) != 3:
    print("Please enter exactly three strings.")
else:
    Emma, Jessa, Kelly = strings

    print("Name 1:", Emma)
    print("Name 2:", Jessa)
    print("Name 3:", Kelly)
