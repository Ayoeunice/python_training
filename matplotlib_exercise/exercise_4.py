# Read toothpaste sales data of each month and show it using a scatter plot
# Also, add a grid in the plot. gridline style should “–“.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("company_sales_data.csv")


# Assuming your CSV has columns 'Month', 'X', and 'Y'.
# You may need to adjust these column names according to your data.
x_values = df['month_number']
y_values = df['toothpaste']

# Create a scatter plot
plt.scatter(x_values, y_values, label='Tooth paste sales data', color='blue', marker='o')

# Add a grid with style '--'
plt.grid(True, linestyle='--')

# Add labels and title
plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.title('Toothpaste sales data')

# Show legend
plt.legend()

# Show the plot
plt.show()

