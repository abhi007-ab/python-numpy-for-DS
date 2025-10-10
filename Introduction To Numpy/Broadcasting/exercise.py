# We'll create a multiplication table via broadcasting

import numpy as np

array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) 

print(array1.shape) # (1, 10)
print(array2.shape) # (10, 1)

# For number of columns, they're compatible. 
# They either match or one of them is a 1
# For Broadcasting

print(array1 * array2)