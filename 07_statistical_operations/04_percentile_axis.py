import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:")
print(arr)

print("\n25th Percentile:")
print(np.percentile(arr, 25))

print("\n50th Percentile:")
print(np.percentile(arr, 50))

print("\n75th Percentile:")
print(np.percentile(arr, 75))


# Axis example
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nMatrix:")
print(matrix)

print("\nColumn-wise Mean (axis=0):")
print(np.mean(matrix, axis=0))

print("\nRow-wise Mean (axis=1):")
print(np.mean(matrix, axis=1))

print("\nColumn-wise Maximum:")
print(np.max(matrix, axis=0))

print("\nRow-wise Sum:")
print(np.sum(matrix, axis=1))

# Array:
# [ 10  20  30  40  50  60  70  80  90 100]

# 25th Percentile:
# 32.5

# 50th Percentile:
# 55.0

# 75th Percentile:
# 77.5

# Matrix:
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# Column-wise Mean (axis=0):
# [40. 50. 60.]

# Row-wise Mean (axis=1):
# [20. 50. 80.]

# Column-wise Maximum:
# [70 80 90]

# Row-wise Sum:
# [ 60 150 240]