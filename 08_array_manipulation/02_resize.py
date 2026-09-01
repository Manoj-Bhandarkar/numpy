import numpy as np

print("=" * 50)
print("RESIZE ARRAY")
print("=" * 50)

arr = np.array([10, 20, 30, 40])

print("Original Array:")
print(arr)

print("Original Size:", arr.size)


# Increase array size
larger_array = np.resize(arr, 8)

print("\nResize to 8 Elements:")
print(larger_array)


# Convert into 2-D array
matrix = np.resize(arr, (3, 3))

print("\nResize to 3 x 3:")
print(matrix)


# Reduce array size
smaller_array = np.resize(arr, 2)

print("\nResize to 2 Elements:")
print(smaller_array)

# ==================================================
# RESIZE ARRAY
# ==================================================
# Original Array:
# [10 20 30 40]
# Original Size: 4

# Resize to 8 Elements:
# [10 20 30 40 10 20 30 40]

# Resize to 3 x 3:
# [[10 20 30]
#  [40 10 20]
#  [30 40 10]]

# Resize to 2 Elements:
# [10 20]