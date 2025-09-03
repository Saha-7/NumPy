## Data Type Change

import numpy as np


arr1 = np.array([1,2,3,"4",5,6,"7",8])
arr2 = np.array([1.1, 2.2, 3.54, 4.22])

newarr1 = arr1.astype(int)
newarr2 = arr2.astype(int)



print(newarr1)
print(newarr2)