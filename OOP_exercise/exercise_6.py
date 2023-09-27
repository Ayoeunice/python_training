# Class Inheritance
# Given:
# Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.
#
# Use the following code for your parent Vehicle class.
# We need to access the parent class from inside a method of a child class.
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())
# Expected Output:
# Total Bus fare is: 5500.0

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Calculate the total fare as per the parent class's fare method
        total_fare = super().fare()

        # Add an extra 10% maintenance charge for Bus instances
        maintenance_charge = total_fare * 0.10

        # Calculate the final fare with the maintenance charge
        final_fare = total_fare + maintenance_charge

        return final_fare

# Create a Bus instance
school_bus = Bus("School Volvo", 12, 50)

# Calculate and print the total fare
print("Total Bus fare is:", school_bus.fare())
