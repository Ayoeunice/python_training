# Convert the following JSON into Vehicle Object
# { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }
# For example, we should be able to access Vehicle Object using the dot operator like this.
# vehicleObj.name, vehicleObj.engine, vehicleObj.price

import json

# Define the Vehicle class
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

# JSON data
json_data = '{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}'

# Deserialize the JSON data into a dictionary
data_dict = json.loads(json_data)

# Create a Vehicle object using the dictionary
vehicle_obj = Vehicle(**data_dict)

# Access Vehicle object properties using dot notation
print("Name:", vehicle_obj.name)
print("Engine:", vehicle_obj.engine)
print("Price:", vehicle_obj.price)
