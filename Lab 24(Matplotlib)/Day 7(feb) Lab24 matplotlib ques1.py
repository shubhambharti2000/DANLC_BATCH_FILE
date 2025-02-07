# Lab1: Analyze the relationship between the size of houses (measured in square
#footage) and their selling prices in a particular neighborhood. You have collected
#data on various houses in that neighborhood.Create a scatter plot using the
#below data and share your conclusion/analysis.
#Input:
#square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800,
#3000])
#selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])


import numpy as np
import matplotlib.pyplot as plt

# Input data
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

# Create scatter plot
plt.scatter(square_footage, selling_prices, color='green', marker='*')
plt.xlabel('Square Footage (sq.ft.)')
plt.ylabel('Selling Prices ($000$)')
plt.title('House Size vs. Selling Prices')
plt.grid(True)
plt.show()
