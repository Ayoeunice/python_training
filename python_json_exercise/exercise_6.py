# Convert the following Vehicle Object into JSON
# import json
#
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
#
# # Convert it into JSON format

import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

# Create a Vehicle object
vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Convert the Vehicle object to a JSON-formatted string
vehicle_json = json.dumps(vehicle.__dict__)

# Print the JSON-formatted string
print(vehicle_json)
