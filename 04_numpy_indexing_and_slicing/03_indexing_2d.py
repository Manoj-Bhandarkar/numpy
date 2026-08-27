import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matrix:")
print(matrix)

# Access single elements
print("\nmatrix[0, 0]:", matrix[0, 0])
print("matrix[1, 1]:", matrix[1, 1])
print("matrix[2, 2]:", matrix[2, 2])

# Access rows
print("\nFirst Row:", matrix[0])
print("Second Row:", matrix[1])

# Access columns
print("\nFirst Column:", matrix[:, 0])
print("Second Column:", matrix[:, 1])

# Output Matrix:\
    
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# matrix[0, 0]: 10
# matrix[1, 1]: 50
# matrix[2, 2]: 90

# First Row: [10 20 30]
# Second Row: [40 50 60]

# First Column: [10 40 70]
# Second Column: [20 50 80]