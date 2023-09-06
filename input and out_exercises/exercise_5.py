# Accept a list of 5 float numbers as an input from the user
floatNumbers = []
n = int(input("Enter the list size : "))


for i in range(0, 5):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)

print("User List is ", floatNumbers)
