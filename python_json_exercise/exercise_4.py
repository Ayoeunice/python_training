# Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys
#
# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# Expected Output:
#
# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# }
import json

# Input JSON data
sampleJson = {"id": 1, "name": "value2", "age": 29}

# Sort the keys alphabetically
sortedJson = dict(sorted(sampleJson.items()))

# Specify the output file name
outputFileName = "sorted_json.json"

# Write the sorted JSON data into a file with pretty formatting
with open(outputFileName, "w") as outputFile:
    json.dump(sortedJson, outputFile, indent=4)

print(f"Sorted JSON data has been written to {outputFileName}")

print(outputFileName)
