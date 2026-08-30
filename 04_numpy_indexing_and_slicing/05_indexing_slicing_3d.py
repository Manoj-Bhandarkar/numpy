import numpy as np

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("3D Array:")
print(arr)

print("\nFirst Matrix:")
print(arr[0])

print("\nSecond Matrix:")
print(arr[1])

# Access single element
print("\nElement arr[1, 0, 2]:", arr[1, 0, 2])

# Slicing
print("\nFirst Row from both matrices:")
print(arr[:, 0, :])

# 3D Array:
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]]

# First Matrix:
# [[1 2 3]
#  [4 5 6]]

# Second Matrix:
# [[ 7  8  9]
#  [10 11 12]]

# Element arr[1, 0, 2]: 9

# First Row from both matrices:
# [[1 2 3]
#  [7 8 9]]