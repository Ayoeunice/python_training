# Calculate the date 4 months from the current date
# Given:
# # 2020-02-25
# given_date = datetime(2020, 2, 25).date()

# pip install python-dateutil

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Given date
given_date = datetime(2020, 2, 25).date()

# Calculate the date 4 months from the given date
new_date = given_date + relativedelta(months=4)

# Print the new date
print("Original Date:", given_date)
print("New Date (4 months later):", new_date)
