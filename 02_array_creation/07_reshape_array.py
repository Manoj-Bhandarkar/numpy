import numpy as np

arr = np.array(range(1,10))

print(arr)

arr = arr.reshape(3,3)

print(arr)

# output
# [1 2 3 4 5 6 7 8 9]
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]