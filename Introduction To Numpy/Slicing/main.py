# Slicing in Numpy

import numpy as np

array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])


# array[start:end:step]   FOR ROWS

print(array[0:3])
print(array[1:])
print(array[0:4:2])
print(array[::2])
print(array[::-1])


# array[row, column]   FOR COLUMN

print(array[:, 1])   # [ 2  6 10 14]
print(array[:, 2])   # [ 3  7 11 15]
print(array[:, -1])  # [ 4  8 12 16]
print(array[:, ::-1])  # reverse

