# PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
# sampleJson = {"key1": "value1", "key2": "value2"}
import json

sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Pretty-print the JSON with custom indent and separators
pretty_json = json.dumps(sampleJson, indent=2, separators=(", ", " = "))

# Print the pretty-printed JSON
print(pretty_json)
