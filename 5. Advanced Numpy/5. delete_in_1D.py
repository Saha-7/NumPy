"""
np.delete(array, index, axis=None)
flattern Array
"""

import numpy as np

arr = np.array([1,2,4,5])

newArr = np.delete(arr,3)
print(newArr)


arr1 = np.array([[1,2,3,4], [5,6,7,8]])
newArr1 = np.delete(arr1, 0, axis=0) # row wise
print(newArr1)

print()

arr2 = np.array([[1,2,3,4], [5,6,7,8]])
newArr2 = np.delete(arr2, 0, axis=1) # row wise
print(newArr2)