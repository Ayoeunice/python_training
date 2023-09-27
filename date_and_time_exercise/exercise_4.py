# Print a date in a the following format
# Day_name  Day_number  Month_name  Year
# Given:
# given_date = datetime(2020, 2, 25)
from datetime import datetime

# Given date
given_date = datetime(2020, 2, 25)

# Format the date as "Day_name Day_number Month_name Year"
formatted_date = given_date.strftime("%A %d %B %Y")

# Print the formatted date
print("Formatted Date:", formatted_date)
