# Access the nested key increment from the following dictionary
# Given:
# emp_dict = {
#     "company": {
#         "employee": {
#             "name": "Jess",
#             "payable": {
#                 "salary": 9000,
#                 "increment": 12
#             }
#         }
#     }
# }
emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}

# Access the nested key "increment"
increment_value = emp_dict["company"]["employee"]["payable"]["increment"]

# Print the value of "increment"
print(increment_value)
