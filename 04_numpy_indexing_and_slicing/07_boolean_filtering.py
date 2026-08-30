import numpy as np

numbers = np.array([10, 25, 30, 45, 50, 60, 75])

print("Original Array:")
print(numbers)

# Greater than
print("\nNumbers greater than 40:")
print(numbers[numbers > 40])

# Less than
print("\nNumbers less than 50:")
print(numbers[numbers < 50])

# Even numbers
print("\nEven Numbers:")
print(numbers[numbers % 2 == 0])

# Multiple conditions
print("\nNumbers between 20 and 60:")
print(numbers[(numbers >= 20) & (numbers <= 60)])

# Original Array:
# [10 25 30 45 50 60 75]

# Numbers greater than 40:
# [45 50 60 75]

# Numbers less than 50:
# [10 25 30 45]

# Even Numbers:
# [10 30 50 60]

# Numbers between 20 and 60:
# [25 30 45 50 60]