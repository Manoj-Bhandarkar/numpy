import numpy as np

# Student marks initialized to passing marks
marks = np.full(10, 35)
print("Marks:")
print(marks)

# Weekly temperature initialized to 25°C
temperature = np.full(7, 25)
print("\nTemperature:")
print(temperature)

# Salary initialized to 50000
salary = np.full(5, 50000)
print("\nSalary:")
print(salary)

# Gray image (pixel value 128)
image = np.full((3, 3, 3), 128)
print("\nImage Shape:")
print(image.shape)

# Boolean mask
mask = np.full((2, 3), True)
print("\nMask:")
print(mask)

# output:
# Marks:
# [35 35 35 35 35 35 35 35 35 35]

# Temperature:
# [25 25 25 25 25 25 25]

# Salary:
# [50000 50000 50000 50000 50000]

# Image Shape:
# (3, 3, 3)

# Mask:
# [[ True  True  True]
#  [ True  True  True]]
