# Aggregate functions = summarize data and typically 
#                       return a single value


import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])

print(np.sum(array))  # 55
print(np.mean(array)) # 5.5 
print(np.std(array))  # 2.8722813232690143
print(np.var(array))  # 8.25
print(np.min(array))  # 1
print(np.max(array))  # 10

# this function will return the index number
print(np.argmin(array)) # 0
print(np.argmax(array)) # 9



# for summing all COLUMNS
print(np.sum(array, axis=0))  # [ 7  9 11 13 15]

# for summing all ROWS
print(np.sum(array, axis=1))  # [15 40]