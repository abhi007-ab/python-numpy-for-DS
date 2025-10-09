import numpy as np

# Scalar arithmetic

array = np.array([1, 2, 3])

print(array + 1)   # [2 3 4]
print(array - 2)   # [-1  0  1]
print(array * 3)   # [3 6 9]
print(array / 4)   # [0.25 0.5  0.75]
print(array ** 5)  # [  1  32 243]



# Vectorized math functions(single dimention)

array = np.array([1.01, 2.5, 3.99])

print(np.sqrt(array))   # [1.00498756 1.58113883 1.99749844]
print(np.round(array))  # [1. 2. 4.]
print(np.floor(array))  # [1. 2. 3.]
print(np.ceil(array))   # [2. 3. 4.]
print(np.pi)            # 3.141592653589793