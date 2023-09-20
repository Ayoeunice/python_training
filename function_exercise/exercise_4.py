# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# Given:
# showEmployee("Ben", 12000)
# showEmployee("Jessa")

def show_employee(name, salary=9000):
    print(f"Employee Name: {name}")
    print(f"Employee Salary: {salary}")

# Call the function with both name and salary
show_employee("Ben", 12000)

# Call the function with only the name (salary will default to 9000)
show_employee("Jessa")
