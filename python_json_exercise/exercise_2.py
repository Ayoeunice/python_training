# Access the value of key2 from the following JSON
# import json
# sampleJson = """{"key1": "value1", "key2": "value2"}"""
# # write code to print the value of key2

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

# Parse the JSON string
data = json.loads(sampleJson)

# Access the value associated with "key2"
value_of_key2 = data["key2"]

# Print the value
print(value_of_key2)
