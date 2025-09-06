"""
np.concatenate((arr1, arr2), axis=0)

For 1D arrays:
    axis=0 -> just joins arrays into one
    axis=1 -> not valid

For 2D arrays:
    axis=0 -> vertical stacking (row-wise)
    axis=1 -> horizontal stacking (column-wise)
"""



import numpy as np

arr1 = np.array([1,2,4,5])
arr2 = np.array([6,7,8,9,10])

new_arr = np.concatenate((arr1,arr2), axis=0)

print(new_arr)