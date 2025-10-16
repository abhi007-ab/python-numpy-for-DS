import numpy as np

vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

# Addition
print(vector1 + vector2)    # [ 7  9 11 13 15]

# Multiplication
print(vector1 * vector2)    # [ 6 14 24 36 50]

# dot product
print(np.dot(vector1, vector2))   # 130


# Angle in Vectors Databases
angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
print(angle)   # 0.26554161733900966


# Vectorized Operations
# Operations on arrays without loops and perform operation on individual elements

restaurant_types = np.array(['biryani', 'chinese', 'pizza', 'burger', 'cafe'])
vectorized_upper = np.vectorize(str.upper)
print(vectorized_upper(restaurant_types))  
  # ['BIRYANI' 'CHINESE' 'PIZZA' 'BURGER' 'CAFE']