#  Assign a different name to function and call it through the new name
# Below is the function display_student(name, age).
# Assign a new name show_student(name, age) to it and call it using the new name.
# Given:
# def display_student(name, age):
#     print(name, age)
# display_student("Emma", 26)
# You should be able to call the same function using
# show_student(name, age)

def display_student(name, age):
    print(name, age)

# Assign a new name to the function
show_student = display_student

# Call the function using the new name
show_student("Emma", 26)

