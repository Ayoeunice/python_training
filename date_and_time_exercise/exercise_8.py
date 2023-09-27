# Convert the following datetime into a string
# Given:
# given_date = datetime(2020, 2, 25)

from datetime import datetime

# Given date
given_date = datetime(2020, 2, 25)

# Convert the datetime object to a string with a specific format
date_string = given_date.strftime("%Y-%m-%d")

# Print the string
print("Date as String:", date_string)

