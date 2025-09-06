"""
vstack() -> row wise
hstack() -> col wise
"""

import numpy as np

arr1 = np.array([1,2,4,5])
arr2 = np.array([6,7,8,9])


print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

