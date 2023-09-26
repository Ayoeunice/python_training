# Check if all items in the tuple are the same
# tuple1 = (45, 45, 45, 45)
tuple1 = (45, 45, 45, 45)

# Check if all items in the tuple are the same
all_same = all(item == tuple1[0] for item in tuple1)

# Print the result
if all_same:
    print("True.")
else:
    print("Not all items in the tuple are the same.")

