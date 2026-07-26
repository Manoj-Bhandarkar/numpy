import numpy as np

# Creating ndarray from Python list
numbers = [10, 20, 30, 40, 50]

arr = np.array(numbers)

print("Original List:", numbers)
print("NumPy Array:", arr)

print("\nType Information")
print("----------------")
print(type(numbers))
print(type(arr))

print("\nArray Information")
print("----------------")
print("Dimension :", arr.ndim)
print("Shape     :", arr.shape)
print("Size      :", arr.size)
print("Data Type :", arr.dtype)

#output:
# Original List: [10, 20, 30, 40, 50]
# NumPy Array: [10 20 30 40 50]

# Type Information
# ----------------
# <class 'list'>
# <class 'numpy.ndarray'>

# Array Information
# ----------------
# Dimension : 1
# Shape     : (5,)
# Size      : 5
# Data Type : int64