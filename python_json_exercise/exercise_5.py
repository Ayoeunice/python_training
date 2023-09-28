# Access the nested key ‘salary’ from the following JSON
# import json
#
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payble":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
#
# # write code to print the value of salary

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Parse the JSON string
data = json.loads(sampleJson)

# Access the nested key 'salary'
salary = data["company"]["employee"]["payble"]["salary"]

# Print the value of 'salary'
print(salary)

