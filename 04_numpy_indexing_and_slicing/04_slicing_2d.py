import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Matrix:")
print(matrix)

# First two rows
print("\nFirst 2 Rows:")
print(matrix[:2])

# Last two rows
print("\nLast 2 Rows:")
print(matrix[1:])

# First two columns
print("\nFirst 2 Columns:")
print(matrix[:, :2])

# Sub matrix
print("\nSub Matrix:")
print(matrix[0:2, 1:3])

# Original Matrix:
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# First 2 Rows:
# [[10 20 30]
#  [40 50 60]]

# Last 2 Rows:
# [[40 50 60]
#  [70 80 90]]

# First 2 Columns:
# [[10 20]
#  [40 50]
#  [70 80]]

# Sub Matrix:
# [[20 30]
#  [50 60]]