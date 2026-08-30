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

print("\nIterating using nested loops:")

for matrix in arr:
    for row in matrix:
        for value in row:
            print(value)
            

# 3D Array:
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]]

# Iterating using nested loops:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12