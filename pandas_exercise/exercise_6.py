# Find each company’s Highest price car

import pandas as pd

# data
data = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\Automobile_data.csv")

car_data = pd.DataFrame(data)

# Find each company's highest-priced car
highest_price_per_company = car_data.groupby('company')['price'].max().reset_index()

print("Highest-Priced Car per Company:")
print(highest_price_per_company)
