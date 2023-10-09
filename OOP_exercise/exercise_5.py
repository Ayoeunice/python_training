# Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Use the following code for this exercise_7.py.
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class Bus(Vehicle):
#     pass
# class Car(Vehicle):
#     pass

# Expected Output:
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

class Vehicle:
    # Class attribute "color" with a default value of "White"
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# Create instances of Bus and Car
school_bus = Bus("School Volvo", 180, 12)
audi_q5 = Car("Audi Q5", 240, 18)

# Display the attributes including the color
print(f"Color: {school_bus.color}, Vehicle name: {school_bus.name}, Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")
print(f"Color: {audi_q5.color}, Vehicle name: {audi_q5.name}, Speed: {audi_q5.max_speed}, Mileage: {audi_q5.mileage}")
