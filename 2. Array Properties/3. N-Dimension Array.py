import numpy as np


arr1 = np.array([1,2,3,4,5,6,7,8])

arr2 = np.array([[2,3,4,5], [9,8,7,6], [11, 22, 33, 44]])

arr3 = np.array([
    [   # First block
        [1, 2, 3],
        [4, 5, 6]
    ],
    [   # Second block
        [7, 8, 9],
        [10, 11, 12]
    ]
])


print("Dimension:", arr1.ndim)
print("Dimension:", arr2.ndim)
print("Dimension:", arr3.ndim)
