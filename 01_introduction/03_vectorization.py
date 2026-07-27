import numpy as np

marks = np.array([75, 82, 90, 68, 88])

print("Original Marks")
print(marks)

# Bonus marks
updated_marks = marks + 5

print("\nAfter Adding Bonus")
print(updated_marks)

# Pass or Fail
print("\nPass Status")
print(updated_marks >= 80)

# Increase marks by 10%
print("\nAfter 10% Increase")
print(marks * 1.10)

#----------------------Output---------------------
# Original Marks
# [75 82 90 68 88]

# After Adding Bonus
# [80 87 95 73 93]

# Pass Status
# [ True  True  True False  True]

# After 10% Increase
# [82.5 90.2 99.  74.8 96.8]