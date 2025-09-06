"""
np.nan_to_num(array, nan=value) => default value-> 0
"""

import numpy as np

arr = np.array([10, np.nan,30, np.nan])


# newArr = np.nan_to_num(arr)
newArr = np.nan_to_num(arr, nan=1)
print(newArr)