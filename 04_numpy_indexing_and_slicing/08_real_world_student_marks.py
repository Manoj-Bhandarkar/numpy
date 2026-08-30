import numpy as np

# Student marks
marks = np.array([45, 78, 35, 90, 67, 30, 88, 55])

print("Student Marks:")
print(marks)

# Students who passed
passed = marks[marks >= 40]

print("\nPassed Students Marks:")
print(passed)

# Students who failed
failed = marks[marks < 40]

print("\nFailed Students Marks:")
print(failed)

# High scorers
high_scorers = marks[marks >= 75]

print("\nHigh Scorers:")
print(high_scorers)

# Update a corrected mark
marks[2] = 40

print("\nUpdated Marks:")
print(marks)

# Student Marks:
# [45 78 35 90 67 30 88 55]

# Passed Students Marks:
# [45 78 90 67 88 55]

# Failed Students Marks:
# [35 30]

# High Scorers:
# [78 90 88]

# Updated Marks:
# [45 78 40 90 67 30 88 55]