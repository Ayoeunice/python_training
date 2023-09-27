# Class Inheritance
# Given:
# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class.
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):  # Default capacity is 50
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# Create a Bus object
school_bus = Bus("School Volvo", 180, 12)

# Call the seating_capacity method with the default capacity
print(school_bus.seating_capacity())  #

# Call the seating_capacity method with a custom capacity
# print(school_bus.seating_capacity(60))  #
