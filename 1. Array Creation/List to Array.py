import numpy as np

arr = [1,2,3,4, "Pritam", 4.21, None]  # if all elements are same data type then only numpy can convert it to array. Otherwise it “falls back” to the generic object type.

num = [10,20,30,40]

convertedArray = np.array(arr)
convertedNum = np.array(num)


print(convertedArray)
print(type(convertedArray))

print(convertedNum.dtype)
print(type(convertedNum))