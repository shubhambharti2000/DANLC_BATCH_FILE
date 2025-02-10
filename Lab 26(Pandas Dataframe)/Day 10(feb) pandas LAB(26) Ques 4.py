# Lab4: Write a Pandas program to select the 'name' and 'score' columns
#from the following DataFrame.
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
#'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}


#DataFrame
df = pd.DataFrame(exam_data)
df1 = pd.DataFrame(exam_data)

#Select name and score
name_score_dataframe = df1[['name', 'score']]

print("Orginal Data: \n",df)
print("Select specific Columns: \n", name_score_dataframe)

