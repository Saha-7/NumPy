"""
np.append() does not modify the original array.

It returns a new array with the added values.
"""



import numpy as np

arr = np.array([1,2,4,5])

newArr = np.append(arr,[6,7,8])

print(newArr)