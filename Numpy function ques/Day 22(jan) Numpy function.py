

#Suppose you have a dataset containing daily temperature readings 
# for a city, and you want to identify days with extreme temperature
# conditions. Find days where the temperature either exceeded 35 
# degrees Celsius (hot day) or dropped below 
# 5 degrees Celsius (cold day). 

#Input:
#temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 
                     #38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])



import numpy as np

# Dataset of daily temperatures
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4, 25, 17.2, -4, -12])

# Identify hot days (temperature > 35°C)
hot_days = np.where(temperatures > 35)
cold_days = np.where(temperatures < 5)

# Creating headers for the table
print(f"{'Day':<5} {'Temperature (°C)':<20} {'Condition':<10}")

# Print hot days in table format
for day in hot_days[0]:
    print(f"{day + 1:<5} {temperatures[day]:<20} {'Hot':<10}")

# Print cold days in table format
for day in cold_days[0]:
    print(f"{day + 1:<5} {temperatures[day]:<20} {'Cold':<10}")
