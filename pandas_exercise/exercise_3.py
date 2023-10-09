# Find the most expensive car company name
# Print most expensive car’s company name and price.
import pandas as pd

# Assuming you have a DataFrame named 'car_data' with columns 'Company' and 'Price'

# Sample data
data = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\Automobile_data.csv")

car_data = pd.DataFrame(data)

# Find the row with the highest price
most_expensive_car = car_data[car_data['price'] == car_data['price'].max()]

# Extract the car company name and price
company_name = most_expensive_car.iloc[0]['company']
car_price = most_expensive_car.iloc[0]['price']

# Print the most expensive car's company name and price
print(f"Most Expensive Car: {company_name}")
print(f"Price: ${car_price}")
