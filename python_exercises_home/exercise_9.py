# Modify the element of a nested list inside the following list
# Change the element 35 to 3500
# Given:
# list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]

# Modify the element from 35 to 3500
list1[1][2][2][1] = 3500

# Print the modified list
print(list1)
