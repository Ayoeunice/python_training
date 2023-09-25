# Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element
# from the list l1 and even index elements from the list l2.
# Given:
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# Initialize an empty list for l3
l3 = []

# Iterate through l1 using a for loop
for i in range(len(l1)):
    # Check if the index is odd and within the bounds of l1
    if i % 2 != 0 and i < len(l1):
        l3.append(l1[i])

# Iterate through l2 using a for loop
for i in range(len(l2)):
    # Check if the index is even and within the bounds of l2
    if i % 2 == 0 and i < len(l2):
        l3.append(l2[i])

# Print the resulting list l3
print(l3)
