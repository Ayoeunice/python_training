# Find the day of the week of a given date
# Given:
# given_date = datetime(2020, 7, 26)
from datetime import datetime

# Given date
given_date = datetime(2020, 7, 26)

# Find the day of the week
day_of_week = given_date.strftime("%A")

# Print the day of the week
print("Day of the Week:", day_of_week)
