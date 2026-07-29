"""
Matrix Addition:
Python Lists vs NumPy Arrays
"""

import numpy as np

#---------------------without NumPy---------------------
print("=" * 50)
print("WITHOUT NUMPY")
print("=" * 50)

matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[0])):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

print("Matrix A")
print(matrix_a)

print("\nMatrix B")
print(matrix_b)

print("\nResult")
for row in result:
    print(row)

#---------------------with NumPy---------------------
print("\n" + "=" * 50)
print("WITH NUMPY")
print("=" * 50)

arr_a = np.array(matrix_a)
arr_b = np.array(matrix_b)

print("Matrix A")
print(arr_a)

print("\nMatrix B")
print(arr_b)

print("\nResult")
print(arr_a + arr_b)


#---------------------Output---------------------
# ==================================================
# WITHOUT NUMPY
# ==================================================
# Matrix A
# [[1, 2], [3, 4]]

# Matrix B
# [[5, 6], [7, 8]]

# Result
# [6, 8]
# [10, 12]

# ==================================================
# WITH NUMPY
# ==================================================
# Matrix A
# [[1 2]
#  [3 4]]

# Matrix B
# [[5 6]
#  [7 8]]

# Result
# [[ 6  8]
#  [10 12]]