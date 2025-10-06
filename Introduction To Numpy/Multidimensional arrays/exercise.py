# We're going to form a three-letter word using string concatination

import numpy as np

array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']],       
                  [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']],       
                  [['S', 'T', 'U'],['V', 'W', 'Y'],['Y', 'Z', ' ']]])

word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]

print(word)