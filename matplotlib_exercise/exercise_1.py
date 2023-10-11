# C:\Users\AYO\Github\python_training\matplotlib_exercise
# Read Total profit of all months and show it using a line plot
# Total profit data provided for each month. Generated line plot must include the following properties: –
# X label name = Month Number
# Y label name = Total profit

# data = pd.read_csv(r"C:\Users\AYO\Github\python_training\pandas_exercise\company_sales_data.csv")

import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [8.00, 4.50]
plt.rcParams["figure.autolayout"] = True
# Set X and Y labels
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
# Add a title to the plot
plt.title('Total Profit Over Months')
columns = ["total_profit", "month_number"]
df = pd.read_csv("company_sales_data.csv", usecols=columns)
# print("Contents in csv file:", df)
print(df)
plt.plot(df.month_number, df.total_profit)
# plt.grid(True)
plt.show()

