import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

print("\nMean:")
print(np.mean(arr))

print("\nMedian:")
print(np.median(arr))


# Example with even number of elements
arr2 = np.array([10, 20, 30, 40])

print("\nSecond Array:")
print(arr2)

print("\nMean:")
print(np.mean(arr2))

print("\nMedian:")
print(np.median(arr2))

# Array:
# [10 20 30 40 50]

# Mean:
# 30.0

# Median:
# 30.0

# Second Array:
# [10 20 30 40]

# Mean:
# 25.0

# Median:
# 25.0