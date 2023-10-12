# Read the total profit of each month and show it using the histogram to see the most common profit ranges
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('company_sales_data.csv')
total_profit = data['total_profit']

# Define the bin edges
bin_edges = np.arange(150000, 200000, 350000)


# Set custom tick labels for the x-axis
xtick_labels = [f"{bin_edges[i]}-{bin_edges[i+1]}" for i in range(len(bin_edges) - 1)]
plt.xticks(bin_edges, xtick_labels, rotation=45)
# plt.legend()
# Create a histogram to visualize profit ranges
plt.figure(figsize=(10, 6))
plt.hist(total_profit, label='profit data', bins=10, edgecolor='k', alpha=0.7)
plt.xlabel('Profit range in dollar')
plt.ylabel('Actual profit')
plt.title('Profit data')
plt.grid(True, linestyle='--')


# Show the plot
plt.show()
