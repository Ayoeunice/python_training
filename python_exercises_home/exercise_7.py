# Print the following number pattern
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# Number of rows in the pattern
n = 6

# Loop to print the pattern
for i in range(1, n + 1):
    for j in range(n, i, -1):
        print(i, end=" ")
    print()
