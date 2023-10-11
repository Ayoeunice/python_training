# Read all product sales data and show it  using a multiline plot
# Display the number of units sold per month for each product using multiline plots.
# (i.e., Separate Plotline for each product ).

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("company_sales_data.csv")
df.plot(x='month_number', y=['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer'], marker='o', figsize=(10, 5))
plt.ylim(bottom=500, top=15000)

plt.xlabel('Month Number')
plt.ylabel('Sales units')
plt.legend()

# Add a title to the plot
plt.title('Sales data')
# Show the plot
# plt.grid(True)
plt.show()
