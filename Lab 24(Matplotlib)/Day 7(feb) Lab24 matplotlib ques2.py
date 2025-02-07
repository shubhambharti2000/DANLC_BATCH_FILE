#Lab2: Create a pie chart to visualize the distribution of your monthly income by
#source. You have collected data on the various sources of your income, such as
#salary, freelance work, investments, and rental income. Share your
#conclusion/analysis.
#Input:
#income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
#monthly_income = [5000, 1500, 1000, 600, 400]

import matplotlib.pyplot as plt

# Input data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create pie chart
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140)
plt.title('Monthly Income Distribution by Source')
plt.show()
