import numpy as np


# Example: A 3D array with shape (2, 2, 3)
# That means:

# 2 blocks (depth)
# each block has 2 rows
# each row has 3 columns

arr = np.array([
    [   # First block
        [1, 2, 3],
        [4, 5, 6]
    ],
    [   # Second block
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(arr)
print("Shape:", arr.shape)
