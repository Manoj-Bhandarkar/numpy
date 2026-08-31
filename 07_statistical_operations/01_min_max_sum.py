
import numpy as np

arr = np.array([45, 78, 23, 90, 56, 34, 88])

print("Array:")
print(arr)

print("\nMinimum Value:")
print(np.min(arr))

print("\nMaximum Value:")
print(np.max(arr))

print("\nSum of Elements:")
print(np.sum(arr))

# Alternative functions
print("\nUsing amin():", np.amin(arr))
print("Using amax():", np.amax(arr))

# Array:
# [45 78 23 90 56 34 88]

# Minimum Value:
# 23

# Maximum Value:
# 90

# Sum of Elements:
# 414

# Using amin(): 23
# Using amax(): 90