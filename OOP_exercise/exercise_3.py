# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Given:
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#  Create a Bus object that will inherit
#  all of the variables and methods of the parent Vehicle class and display it.
# Expected Output:
# Vehicle Name: School Volvo Speed: 180 Mileage: 12

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Create a child class Bus that inherits from Vehicle
class Bus(Vehicle):
    pass

# Create a Bus object with the specified attributes
school_bus = Bus("School Volvo", 180, 12)

# Display the attributes of the Bus object as specified
print("Vehicle Name:", school_bus.name)
print("Speed:", school_bus.max_speed)
print("Mileage:", school_bus.mileage)
