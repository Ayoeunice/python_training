# Read all product sales data and show it using the stack plot
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_data.csv' with the path to your CSV file containing sales data.
data = pd.read_csv('company_sales_data.csv')

# Extract the relevant data
months = data['month_number']
face_wash = data['facewash']
face_cream = data['facecream']
bathing_soap = data['bathingsoap']
shampoo = data['shampoo']
tooth_paste = data['toothpaste']
moisturizer = data['moisturizer']

plt.plot([],[], color='c', label='face Cream',  linewidth=6)
plt.plot([],[], color='m', label='Face wash',   linewidth=6)
plt.plot([],[], color='y', label='Tooth paste', linewidth=6)
plt.plot([],[], color='k', label='Bathing soap', linewidth=6)
plt.plot([],[], color='g', label='Shampoo',      linewidth=6)
plt.plot([],[], color='r', label='Moisturizer',  linewidth=6)

plt.stackplot(months, face_wash, face_cream, bathing_soap,shampoo,tooth_paste,moisturizer,colors = ['m', 'c', 'k', 'g', 'y', 'r'])

# Customize the plot
plt.title('Stack Plot of All Product Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales units in Number')
plt.legend(loc='upper left')

# Show the stack plot
plt.show()
