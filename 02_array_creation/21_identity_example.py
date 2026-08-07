import numpy as np

# Identity matrix
I = np.identity(3, dtype=int)

# Matrix
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matrix A")
print(A)

print("\nIdentity Matrix")
print(I)

print("\nA × I")
print(np.matmul(A, I))

print("\nI × A")
print(np.matmul(I, A))

# Output
# Matrix A
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# Identity Matrix
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# A × I
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# I × A
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]