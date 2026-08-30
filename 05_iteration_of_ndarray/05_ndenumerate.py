import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("Original Matrix:")
print(matrix)
print("\nIndex and Value:")
for index, value in np.ndenumerate(matrix):
    print("Index:", index, "Value:", value)

# Original Matrix:
# [[10 20 30]
#  [40 50 60]]

# Index and Value:
# Index: (0, 0) Value: 10
# Index: (0, 1) Value: 20
# Index: (0, 2) Value: 30
# Index: (1, 0) Value: 40
# Index: (1, 1) Value: 50
# Index: (1, 2) Value: 60