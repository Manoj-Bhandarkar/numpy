import numpy as np

A = np.array([
    [10, 20],
    [30, 40]
])

B = np.array([
    [1, 2],
    [3, 4]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nAddition:")
print(A + B)

# Matrix Subtraction
print("\nSubtraction:")
print(A - B)

# Element-wise Multiplication
print("\nElement-wise Multiplication:")
print(A * B)

# Element-wise Division
print("\nElement-wise Division:")
print(A / B)

# Matrix A:
# [[10 20]
#  [30 40]]

# Matrix B:
# [[1 2]
#  [3 4]]

# Addition:
# [[11 22]
#  [33 44]]

# Subtraction:
# [[ 9 18]
#  [27 36]]

# Element-wise Multiplication:
# [[ 10  40]
#  [ 90 160]]

# Element-wise Division:
# [[10. 10.]
#  [10. 10.]]