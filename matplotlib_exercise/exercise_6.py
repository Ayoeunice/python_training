# Read sales data of bathing soap of all months and show it using a bar chart.
# Save this plot to your hard disk

import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_data.csv' with the path to your CSV file containing sales data.
data = pd.read_csv('company_sales_data.csv')

# Assuming you have a column named 'Month' and a column named 'BathingSoapSales'.
# Replace 'BathingSoapSales' with the actual column name in your dataset.
bathing_soap_sales = data['bathingsoap']

# Create a bar chart for bathing soap sales
plt.figure(figsize=(10, 6))
plt.bar(data['month_number'], bathing_soap_sales, color='blue')
plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.title('Bathing Soap Sales data')
plt.grid(True, linestyle='--')
# Save the plot to your hard disk
plt.savefig('bathing_soap_sales_bar_chart.png')

# Show the plot
plt.show()

