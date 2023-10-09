# From the given dataset print the first and last five rows

# importing pandas module
import pandas as pd

# reading csv file
data = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\Automobile_data.csv")

# displaying  dataframe
data.head()
# print(data)
# C:\Users\AYO\Github\python_training\pandas_exercise
# df = pd.DataFrame(data, columns=["company", "price"])
#  print(df)

# Print the first five rows
print("First Five Rows:")
print(data.head())

# Print the last five rows
print("\nLast Five Rows:")
print(data.tail())
