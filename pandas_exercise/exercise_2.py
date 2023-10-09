# Clean the dataset and update the CSV file
# Replace all column values which contain ?, n.a, or NaN.
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\Automobile_data.csv")

# Replace unwanted values (? or n.a or NaN) with NaN
df.replace(['?', 'n.a', 'NaN'], pd.NA, inplace=True)

# Save the cleaned DataFrame back to the CSV file
df.to_csv('cleaned_dataset.csv', index=False)

# Optionally, you can print the cleaned DataFrame
print("Cleaned DataFrame:")
print(df)
