import numpy as np

matrix = (
    (10,20,30),
    (40,50,60),
    (70,80,90)
)

arr = np.array(matrix)

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

# output
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# 2
# (3, 3)
# 9
# int64