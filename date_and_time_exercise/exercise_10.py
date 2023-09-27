# Calculate number of days between two given dates
# Given:
# # 2020-02-25
# date_1 = datetime(2020, 2, 25)
# 2020-09-17
# date_2 = datetime(2020, 9, 17)

from datetime import datetime

# Given dates
date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

# Calculate the number of days between the two dates
delta = date_2 - date_1
days_between = delta.days

# Print the number of days
# print("Number of Days Between the Dates:", days_between)
print(days_between)
