# Create an inner function
# Question description: -
# Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
# Create an inner function inside an outer function that will concatenate x and y.
# At last, an outer function will join the word 'developer' to it.
# Expected Output: -
# EmmaKellyDevelopers

def outer_function(x, y):
    def inner_function():
        return x + y

    result = inner_function() + 'Developer'
    return result

x = 'Emma'
y = 'Kelly'

output = outer_function(x, y)
print(output)

