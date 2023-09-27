# Subtract a week (7 days)  from a given date in Python
# Given:
# given_date = datetime(2020, 2, 25)

from datetime import datetime, timedelta

# Given date
given_date = datetime(2020, 2, 25)

# Subtract a week (7 days)
new_date = given_date - timedelta(days=7)

# Print the new date
print("Original Date:", given_date)
print("New Date (after subtracting a week(7 days)):", new_date)
