# Calculate total sale data for last year for each product and show it using a Pie chart.
# In Pie chart display Number of units sold per year for each product in percentage.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv('company_sales_data.csv')
# print(df)

# Select columns you need
month_number = df['month_number'].tolist
data = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), df['bathingsoap'].sum(), df['moisturizer'].sum(), df['shampoo'].sum()]

labels = ['Facecream', 'Facewash', 'Toothpaste', 'Bathingsoap', 'Moisturizer', 'Shampoo']

plt.pie(data, labels=labels, autopct=('%1.1f%%'))
plt.axis('equal')
plt.title('Sales data')
plt.legend(loc='upper left')
plt.show()

