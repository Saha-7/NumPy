"""
.insert(array, index, value, asix=None)
array ->
index ->
value ->
asix ->
axis=None → Flattens the array first, then inserts into the 1D version.
asix = 0 = row-wise
asix= 1 = column-wise
"""

import numpy as np

arr = np.array([1,2,4,5])

print(arr)
newArr = np.insert(arr,2,3)

print(newArr)