# Check type of an object
# Write a program to determine which class a given Bus object belongs to.
#
# Given:
#
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Check the class of the School_bus object
class_name = type(School_bus).__name__

print(f"The object School_bus belongs to the class {class_name}")
