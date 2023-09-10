# Display Fibonacci series up to 10 terms

a, b = 0, 1

n = 10

print("Fibonacci series up to 10 terms:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

