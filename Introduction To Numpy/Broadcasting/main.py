# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the large array's shape.

# The dimensions have the same size.
# OR
# One of the dimensions has a size of 1.

import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)  # (1, 4)
print(array2.shape)  # (4, 1)

print(array1 * array2)