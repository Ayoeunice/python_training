# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

previous_number = 0

for current_number in range(0, 10):  # Iterate through the first 10 numbers (1 to 10)
    # Calculate the sum of the current and previous numbers
    sum_of_numbers = current_number + previous_number

    # Print the result
    print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {sum_of_numbers}")

    # Update the previous_number for the next iteration
    previous_number = current_number
