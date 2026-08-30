import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Matrix:")
print(matrix)

print("\nIterating Rows:")

for row in matrix:
    print(row)

print("\nIterating Individual Elements:")

for row in matrix:
    for value in row:
        print(value)

# Original Matrix:
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# Iterating Rows:
# [10 20 30]
# [40 50 60]
# [70 80 90]

# Iterating Individual Elements:
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90