
#4. Write a NumPy program to convert a list and tuple into arrays.
# Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8] 
# Input: my_tuple = ([8, 4, 6], [1, 2, 3])

import numpy as np

# Convert list to array
list = [1, 2, 3, 4, 5, 6, 7, 8]
array_list = np.array(list)
print("Array from List:", array_list)

# Convert tuple to array
my_tuple = ([8, 4, 6], [1, 2, 3])
tuple_array = np.array(my_tuple)
print("Array from Tuple:\n", tuple_array)
