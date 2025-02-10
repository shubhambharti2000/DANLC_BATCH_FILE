# Lab1: Write a Pandas program to create a dataframe from a dictionary and
#display it.
#Sample data:
#score={'Math':[78,85,96,80,86], 'English':[84,94,89,83,86],
# 'Hindi':[86,97,96,72,83]}

import pandas as pd

score = {'Math': [78, 85, 96, 80, 86], 'English': [84, 94, 89, 83, 86], 
         'Hindi': [86, 97, 96, 72, 83]}

#DataFrame
df = pd.DataFrame(score)

print(df)
