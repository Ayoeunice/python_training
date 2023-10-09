# Sort all cars by Price column
import pandas as pd

#  data
data = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\Automobile_data.csv")
car_data = pd.DataFrame(data)

# Sort all cars by the 'Price' column
# sorted_cars = car_data.sort_values(by='price')
sorted_cars = car_data.sort_values(by='price', ascending=False)

print("Cars Sorted by Price:")
print(sorted_cars)

