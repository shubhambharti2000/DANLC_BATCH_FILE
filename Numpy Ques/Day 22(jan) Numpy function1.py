
#2. Suppose you have a dataset containing monthly sales data
# for a company, and you want to split this data into quarterly
# reports for analysis and reporting purposes. 

#Input: monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 
                          #   190, 205, 198, 210, 225])


import numpy as np

# Monthly sales data
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Reshape the array to have 4 quarters, each containing 3 months
quarterly_sales = monthly_sales.reshape(4, 3)

# Creating headers for the table
print(f"{'Quarter':<10} {'Sales (in thousands of dollars)':<30}")

# Loop through each quarter and print the sales data
for i, quarter in enumerate(quarterly_sales, start=1):
    print(f"{'Quarter ' + str(i):<10} {str(quarter):<30}")
