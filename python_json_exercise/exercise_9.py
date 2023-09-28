# Parse the following JSON to get all the values of a key ‘name’ within an array
# [
#    {
#       "id":1,
#       "name":"name1",
#       "color":[
#          "red",
#          "green"
#       ]
#    },
#    {
#       "id":2,
#       "name":"name2",
#       "color":[
#          "pink",
#          "yellow"
#       ]
#    }
# ]
# Expected Output:
#
# ["name1", "name2"]

import json

# JSON data
json_data = '[{"id":1,"name":"name1","color":["red","green"]},{"id":2,"name":"name2","color":["pink","yellow"]}]'

# Parse the JSON data
data = json.loads(json_data)

# Extract all 'name' values into a list
names = [item['name'] for item in data]

# Print the list of 'name' values
print(names)

