import numpy as np

array = np.array('A')   # 0 dimensional array

array = np.array(['A', 'B', 'C'])  # 1 dimensional array

array = np.array([['A', 'B', 'C'],     # 2 dimensional array
                  ['D', 'E', 'F'],     # rows & columns
                  ['G', 'H', 'I']])



array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']],       # 3 dimensional array
                  [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']],       # depth,rows & columns
                  [['S', 'T', 'U'],['V', 'W', 'Y'],['Y', 'Z', ' ']]])


# print(array.ndim)

# print(array.shape)

 # Multidimensional Indexing
print(array[0, 0, 0])   # A
print(array[0, 0, 1])   # B
print(array[0, 1, 0])   # D