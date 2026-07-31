import numpy as np

arr = np.arange(16)

print(arr)
print("-"*20)
print(arr.reshape(4,4))
print("-"*20)
print(arr.reshape(2,2,4))
print("-"*20)
print(arr.reshape(2,2,2,2))
print("-"*20)
print(arr.reshape(16,))