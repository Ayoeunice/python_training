# Add a week (7 days) and 12 hours to a given date
# Given:
# # 2020-03-22 10:00:00
# given_date = datetime(2020, 3, 22, 10, 0, 0)
from datetime import datetime, timedelta

# Given date
given_date = datetime(2020, 3, 22, 10, 0, 0)

# Define a timedelta for a week (7 days) and 12 hours
delta = timedelta(days=7, hours=12)

# Add the timedelta to the given date
new_date = given_date + delta

# Print the new date
print("Original Date:", given_date)
print("New Date (after adding a week (7 days) and 12 hours):", new_date)
