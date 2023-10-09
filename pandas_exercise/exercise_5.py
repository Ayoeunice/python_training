# Count total cars per company
import pandas as pd

# data
data = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\Automobile_data.csv")
car_data = pd.DataFrame(data)

# Count total cars per company
car_count_per_company = car_data['company'].value_counts()

print("Total Cars per Company:")
print(car_count_per_company)

