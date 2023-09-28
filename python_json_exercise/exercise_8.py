# Check whether following json is valid or invalid. If Invalid correct it
# {
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payble":{
#             "salary":7000
#             "bonus":800
#          }
#       }
#    }
# }
# answer
# The provided JSON is invalid because there is a missing comma between the "salary"
# and "bonus" key-value pairs. Here's the corrected JSON:

{
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}
