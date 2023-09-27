# Determine if School_bus is also an instance of the Vehicle class
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

# Check if School_bus is an instance of the Vehicle class
is_instance = isinstance(School_bus, Vehicle)

if is_instance:
    print("School_bus is an instance of the Vehicle class")
else:
    print("School_bus is not an instance of the Vehicle class")
