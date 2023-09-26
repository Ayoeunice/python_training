# Swap two tuples in Python
# Given:
# tuple1 = (11, 22)
# tuple2 = (99, 88)
tuple1 = (11, 22)
tuple2 = (99, 88)

# Swap the values of tuple1 and tuple2 using a temporary variable
temp = tuple1
tuple1 = tuple2
tuple2 = temp

# Print the swapped tuples
print("Swapped tuple1:", tuple1)
print("Swapped tuple2:", tuple2)
