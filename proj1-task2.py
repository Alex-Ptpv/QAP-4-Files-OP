import matplotlib.pyplot as mat_plt

# create an empty list to store the monthly sales
sales = []

# get the sales for each month from the user
for month in range(1, 13):
    sales_amount = int(input("Enter sales amount for month {}: ".format(month)))
    sales.append(sales_amount)

# create a list of month names
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# create a bar chart of the monthly sales
mat_plt.bar(months, sales)

# set the title and labels for the chart
mat_plt.title('Total Sales by Month')
mat_plt.xlabel('Month')
mat_plt.ylabel('Sales ($)')

# show the chart
mat_plt.show()