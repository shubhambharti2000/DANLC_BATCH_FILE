# Using ChatGPT generate the python code to solve the same problem
#Scenario:Analyzing Sales Data
#Suppose you work for a retail company, and you have dummy data containing sales
#data for the past year. The data includes information such as SalesDate,product
#names,regions, sales quantities, prices, and dates. You have to generate a bar chart
#,pie plot on region and prices and line chart on SalesDate and prices columns.
#Further, you need to get some inference out of the chart.
#Create a ChatGPT prompt to generate the code for this scenario. Based on the code
#generated, ask ChatGPT to give the conclusion/inference.
#Note. You can provide the data to ChatGPT or ask it to use sample data

import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'SalesDate': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'Product': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product C'],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'SalesQuantity': [100, 150, 200, 120, 160, 180, 140, 170, 190, 110, 155, 175],
    'Price': [20, 25, 30, 22, 26, 28, 24, 27, 29, 21, 26, 28]
}

df = pd.DataFrame(data)

# Bar chart for sales quantities by product
plt.figure(figsize=(10, 6))
df.groupby('Product')['SalesQuantity'].sum().plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Total Sales Quantities by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales Quantity')
plt.show()

# Pie chart for distribution of sales by region
plt.figure(figsize=(8, 8))
df.groupby('Region')['SalesQuantity'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Sales by Region')
plt.ylabel('')
plt.show()

# Line chart for sales prices over time
plt.figure(figsize=(10, 6))
df.groupby('SalesDate')['Price'].mean().plot(kind='line', marker='o', linestyle='-', color='purple')
plt.title('Sales Prices Over Time')
plt.xlabel('Sales Date')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()
