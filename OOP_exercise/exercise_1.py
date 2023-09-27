# Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Create an instance of the Vehicle class
car = Vehicle(120, 20)

# Access the instance attributes
print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)
