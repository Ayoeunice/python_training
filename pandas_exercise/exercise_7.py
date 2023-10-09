# Find the average mileage of each car making company
import pandas as pd

#  data
data = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\Automobile_data.csv")

car_data = pd.DataFrame(data)

# Find the average mileage for each car-making company
average_mileage_per_company = car_data.groupby('company')['average-mileage'].mean().reset_index()

print("Average Mileage per Company:")
print(average_mileage_per_company)

