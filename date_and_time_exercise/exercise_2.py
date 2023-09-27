# Convert string into a datetime object
# For example, You received the following date in string format.
# Please convert it into Python’s DateTime object.
# Given:
# date_string = "Feb 25 2020 4:20PM"

from datetime import datetime

# Given date string
date_string = "Feb 25 2020 4:20PM"

# Convert the date string to a datetime object
date_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')

# Print the datetime object
print("Datetime Object:", date_object)
