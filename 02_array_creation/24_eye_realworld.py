"""
Real-World Example:
Identity Matrix in Image Processing

Identity matrices are used in image processing,
computer vision, and linear algebra operations.
"""

import numpy as np

# Sample image matrix (grayscale image)
image = np.array([
    [120, 150, 180],
    [200, 220, 240],
    [100, 130, 160]
])

# Identity matrix
identity = np.eye(3, dtype=int)

# Multiplying by identity matrix
result = image @ identity

print("Original Image Matrix:")
print(image)

print("\nIdentity Matrix:")
print(identity)

print("\nAfter Multiplication:")
print(result)

print("\nAre both matrices equal?", np.array_equal(image, result))

# Output
# Original Image Matrix:
# [[120 150 180]
#  [200 220 240]
#  [100 130 160]]

# Identity Matrix:
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# After Multiplication:
# [[120 150 180]
#  [200 220 240]
#  [100 130 160]]

# Are both matrices equal? True