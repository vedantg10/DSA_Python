#Day 1 - 11, 15, 10, 6
#Day 2 - 10, 14, 11, 5
#Day 3 - 12, 17, 12, 8
#Day 4 - 15, 18, 14, 9

import sys
print(sys.path)

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

def traverse2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

