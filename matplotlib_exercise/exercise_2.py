# Get total profit of all months and show line plot with the following Style properties
# Generated line plot must include following Style properties: –
# Line Style dotted and Line-color should be red
# Show legend at the lower right location.
# X label name = Month Number
# Y label name = Sold units number
# Add a circle marker.
# Line marker color as read
# Line width should be 3

import matplotlib.pyplot as plt

#  data
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.markers import MarkerStyle
plt.rcParams["figure.figsize"] = [8.00, 4.50]
plt.rcParams["figure.autolayout"] = True
# Set X and Y labels
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
columns = ["total_profit", "month_number"]
df = pd.read_csv("company_sales_data.csv", usecols=columns)
# Create a line plot with the specified style properties
marker = MarkerStyle('o', fillstyle='full')
plt.plot(df.month_number, df.total_profit, marker=marker, markerfacecolor='black', linestyle='--', color='red', linewidth=3, label='Total Profit')

# Show legend at the lower right location
plt.legend(loc='lower right')

# Add a title to the plot
plt.title('Total Profit Over Months')

# Show the plot
plt.grid(True)
plt.show()
