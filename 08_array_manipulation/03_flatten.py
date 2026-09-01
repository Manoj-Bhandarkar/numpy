import numpy as np

print("=" * 50)
print("FLATTEN ARRAY")
print("=" * 50)

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original Array:")
print(arr)

print("\nShape:", arr.shape)


# Convert 2-D to 1-D
flat_arr = arr.flatten()

print("\nFlattened Array:")
print(flat_arr)

print("Shape:", flat_arr.shape)


# Check copy behavior
flat_arr[0] = 999

print("\nModified Flattened Array:")
print(flat_arr)

print("\nOriginal Array:")
print(arr)

print("\nNote: flatten() creates a COPY.")

# ==================================================
# FLATTEN ARRAY
# ==================================================
# Original Array:
# [[10 20 30]
#  [40 50 60]]

# Shape: (2, 3)

# Flattened Array:
# [10 20 30 40 50 60]
# Shape: (6,)

# Modified Flattened Array:
# [999  20  30  40  50  60]

# Original Array:
# [[10 20 30]
#  [40 50 60]]

# Note: flatten() creates a COPY.