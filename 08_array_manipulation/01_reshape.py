
import numpy as np

print("=" * 50)
print("RESHAPE ARRAY")
print("=" * 50)

# Create 1-D array
arr = np.arange(1, 13)

print("Original Array:")
print(arr)

print("\nOriginal Shape:", arr.shape)
print("Original Dimension:", arr.ndim)


# Convert into 2-D array
arr_2d = arr.reshape(3, 4)

print("\nAfter Reshape (3 x 4):")
print(arr_2d)

print("Shape:", arr_2d.shape)
print("Dimension:", arr_2d.ndim)


# Convert into another shape
arr_3d = arr.reshape(2, 2, 3)

print("\nAfter Reshape (2 x 2 x 3):")
print(arr_3d)

print("Shape:", arr_3d.shape)
print("Dimension:", arr_3d.ndim)


# Important Rule
print("\nTotal Elements:", arr.size)
print("3 x 4 =", 3 * 4)
print("2 x 2 x 3 =", 2 * 2 * 3)