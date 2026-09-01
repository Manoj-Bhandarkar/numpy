import numpy as np

print("=" * 50)
print("RAVEL ARRAY")
print("=" * 50)

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original Array:")
print(arr)


# Convert into 1-D
ravel_arr = arr.ravel()

print("\nRavel Array:")
print(ravel_arr)


# Modify ravel array
ravel_arr[0] = 999

print("\nModified Ravel Array:")
print(ravel_arr)

print("\nOriginal Array:")
print(arr)

print("\nNote: ravel() returns a VIEW when possible.")

# ==================================================
# RAVEL ARRAY
# ==================================================
# Original Array:
# [[10 20 30]
#  [40 50 60]]

# Ravel Array:
# [10 20 30 40 50 60]

# Modified Ravel Array:
# [999  20  30  40  50  60]

# Original Array:
# [[999  20  30]
#  [ 40  50  60]]

# Note: ravel() returns a VIEW when possible.