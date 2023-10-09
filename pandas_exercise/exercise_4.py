# Print All Toyota Cars details

import pandas as pd

#  data
data = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\Automobile_data.csv")


car_data = pd.DataFrame(data)

# Filter and print details of all Toyota cars
toyota_cars = car_data[car_data['company'] == 'toyota']

print("Details of Toyota Cars:")
print(toyota_cars)
