# Convert the following dictionary into JSON format
# data = {"key1" : "value1", "key2" : "value2"}
import json

data = {"key1": "value1", "key2": "value2"}

# Convert the dictionary to JSON format
json_data = json.dumps(data)

# Print the JSON data
print(json_data)
