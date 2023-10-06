# Generate a random date between given start and end dates
import random
from datetime import datetime, timedelta

# Defining the start and end dates
start_date = datetime(2023, 2, 1)
end_date = datetime(2023, 10, 30)

# Calculate the difference in days between the start and end dates
date_range = end_date - start_date

# Generate a random number of days within the date range
random_days = random.randint(0, date_range.days)

# Calculate the random date by adding the random number of days to the start date
random_date = start_date + timedelta(days=random_days)

# Print the random date
print("Random Date:", random_date.strftime("%Y-%m-%d"))

