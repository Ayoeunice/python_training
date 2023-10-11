# Read face cream and facewash product sales data and show it using the bar chart
# The bar chart should display the number of units sold per month for each product.
# Add a separate bar for each product in the same chart.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
columns = ["facewash", "facecream", "total_units", "month_number"]
df = pd.read_csv("company_sales_data.csv", usecols=columns)
#df = df.pivot(index='month_number', columns='sales', values='total_units')
#df = df.reset_index()

#prepare data array for plotting
labels = df['month_number']
category1 = df['facecream']
category2 = df['facewash']

#set x-axis ticks label location
x = np.arange(len(labels))

#set bar width
width = 0.28
#plot the chart
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, category1, width, edgecolor='white', label='Face cream sales data')
rects2 = ax.bar(x, category2, width, edgecolor='white', label='Face wash sales data')

#set chart title
ax.set_title('Facewash and facecream sales data', pad=50)

#set chart legend
ax.legend(loc=(0,1.04), ncol=2)

#set y-axis title
ax.set_ylabel('Sales units in numbers')
#set x-axis title
ax.set_xlabel('Month Number')
#set y-axis label
ax.tick_params(labelleft=True)

#set x-axis tick and label
ax.set_xticks(x, labels)

#show grid below the bars
ax.grid(axis='y')

#format y-axis tick labels
def number_formatter(x, pos):
    if x >= 1e6:
        s = '{:1.0f}M'.format(x*1e-6)
    elif x < 1e6 and x >= 1e3:
        s = '{:1.0f}K'.format(x*1e-3)
    else:
        s = '{:1.0f}'.format(x)
    return s
ax.yaxis.set_major_formatter(number_formatter)

plt.legend()
#adjust chart margin and layout
fig.tight_layout()

#show chart
plt.show()



