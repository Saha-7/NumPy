import numpy as np

arr = np.array([10, np.inf,30, -np.inf])

clean = np.nan_to_num(arr, posinf=1000, neginf=-1000)

print(clean)