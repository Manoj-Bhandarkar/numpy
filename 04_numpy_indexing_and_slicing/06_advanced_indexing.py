import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:", arr)

# Select multiple elements using index list
result = arr[[0, 2, 4]]
print("Selected Elements:", result)

# Using ndarray as index
indices = np.array([1, 3, 5])
result = arr[indices]
print("Using Index Array:", result)

# Original Array: [10 20 30 40 50 60]
# Selected Elements: [10 30 50]
# Using Index Array: [20 40 60]