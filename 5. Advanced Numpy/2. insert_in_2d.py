import numpy as np

arr = np.array([[1,2],
                [5,6]])

print(arr)

print()

arr1= np.insert(arr,1,[3,4],0) # row wise
print(arr1)

print()

arr2 = np.insert(arr,1,[3,4],1) # col wise
print(arr2)

print()

arr3 = np.insert(arr,1,[3,4],axis=None) # flattern & insert
print(arr3)