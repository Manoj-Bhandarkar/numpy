import numpy as np

print("=" * 50)
print("TRANSPOSE ARRAY")
print("=" * 50)

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original Matrix:")
print(arr)

print("\nOriginal Shape:", arr.shape)


# Method 1
transpose_arr = np.transpose(arr)

print("\nTranspose using np.transpose():")
print(transpose_arr)

print("Shape:", transpose_arr.shape)


# Method 2
transpose_arr2 = arr.T

print("\nTranspose using .T:")
print(transpose_arr2)


# Example with square matrix
matrix = np.array([
    [1, 2],
    [3, 4]
])

print("\nSquare Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)

# ==================================================
# TRANSPOSE ARRAY
# ==================================================
# Original Matrix:
# [[10 20 30]
#  [40 50 60]]

# Original Shape: (2, 3)

# Transpose using np.transpose():
# [[10 40]
#  [20 50]
#  [30 60]]
# Shape: (3, 2)

# Transpose using .T:
# [[10 40]
#  [20 50]
#  [30 60]]

# Square Matrix:
# [[1 2]
#  [3 4]]

# Transpose:
# [[1 3]
#  [2 4]]
# PS D:\project_repo\numpy> 