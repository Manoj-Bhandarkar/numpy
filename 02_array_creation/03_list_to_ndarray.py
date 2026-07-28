import numpy as np

numbers = [10,20,30,40,50]

arr = np.array(numbers)

print(arr)

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

# output
# [10 20 30 40 50]
# 1
# (5,)
# 5
# int64