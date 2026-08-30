import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("Original Matrix:")
print(matrix)
print("\nIterating using np.nditer():")
for value in np.nditer(matrix):
    print(value)
    
# Original Matrix:
# [[10 20 30]
#  [40 50 60]]

# Iterating using np.nditer():
# 10
# 20
# 30
# 40
# 50
# 60

# another Example
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("Original Matrix:")
print(arr)
print("Iterating 3D array using nditer:")
for value in np.nditer(arr):
    print(value)

# Original Matrix:
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]
# Iterating 3D array using nditer:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8