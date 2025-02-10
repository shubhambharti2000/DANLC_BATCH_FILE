# Suppose you work for a retail company, and you have a dummy dataset containing
#sales data for the past year. The data includes information such as customer names,
#product names, sales quantities, prices, and dates. You want to perform various data
#analysis tasks like Total revenue for the year,Average revenue per sale,Best-selling
#product,Date with the highest total revenue also wants to generate product and total
#sales wise barchart using Pandas DataFrames.
#Further, you need to get some inference out of the chart.
#Create a ChatGPT prompt to generate the code for this scenario. Based on the code
#generated, ask ChatGPT to give the conclusion/inference.
#Note. You can provide the data to ChatGPT in the form of a list or dictionary or ask it to
#use sample data


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = {
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward', 'Alice', 'Bob', 'Charlie'],
    'product_name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product C', 'Product A', 'Product B'],
    'quantity': [10, 15, 20, 15, 10, 5, 20, 25],
    'price': [100, 150, 200, 100, 150, 200, 100, 150],
    'date': pd.to_datetime(['2023-01-15', '2023-02-20', '2023-03-25', '2023-04-30', '2023-05-05', '2023-06-10', '2023-07-15', '2023-08-20'])
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# 1. Calculate the total revenue for the year
df['revenue'] = df['quantity'] * df['price']
total_revenue = df['revenue'].sum()

# 2. Calculate the average revenue per sale
average_revenue_per_sale = df['revenue'].mean()

# 3. Determine the best-selling product
best_selling_product = df.groupby('product_name')['quantity'].sum().idxmax()

# 4. Identify the date with the highest total revenue
date_with_highest_revenue = df.groupby('date')['revenue'].sum().idxmax()

# 5. Generate a bar chart showing the total sales for each product
product_sales = df.groupby('product_name')['revenue'].sum()
product_sales.plot(kind='bar')
plt.title('Total Sales for Each Product')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.show()

# 6. Generate a bar chart showing the total sales for each month
monthly_sales = df.set_index('date').resample('M')['revenue'].sum()
monthly_sales.plot(kind='bar')
plt.title('Total Sales for Each Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

print(f"Total revenue for the year: {total_revenue}")
print(f"Average revenue per sale: {average_revenue_per_sale}")
print(f"Best-selling product: {best_selling_product}")
print(f"Date with the highest total revenue: {date_with_highest_revenue}")
