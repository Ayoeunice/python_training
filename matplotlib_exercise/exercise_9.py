# Read Bathing soap facewash of all months and display it using the Subplot
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('company_sales_data.csv')

# Extract the relevant data
months = data['month_number']
bathing_soap = data['bathingsoap']
facewash = data['facewash']

# Create subplots
plt.figure(figsize=(12, 6))

# Subplot for Bathing Soap
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.plot(months, bathing_soap, marker='o', color='b')
plt.title('Sales data of Bathing Soap')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')

# Subplot for Facewash
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.plot(months, facewash, marker='o', color='g')
plt.title('Sales data of Face wash')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')

# Adjust subplot layout to avoid overlap
plt.tight_layout()

# Show the subplots
plt.show()

