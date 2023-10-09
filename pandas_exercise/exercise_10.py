# Merge two data frames using the following condition
# Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
#
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
import pandas as pd

# Create data frames from the given dictionaries
Car_Price = {'company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}

df1 = pd.DataFrame(Car_Price)
df2 = pd.DataFrame(car_Horsepower)

# Merge the data frames based on the "Company" column
merged_df = pd.merge(df1, df2, on='company')

# Print the merged data frame
print(merged_df)
