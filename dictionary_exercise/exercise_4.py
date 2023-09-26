#  Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.
# Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Initialize the dictionary with default values for each employee
employee_defaults = {employee: defaults.copy() for employee in employees}

# Print the resulting dictionary
print(employee_defaults)
