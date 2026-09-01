import numpy as np

print("=" * 60)
print("STUDENT MARKS DATA TRANSFORMATION")
print("=" * 60)

# Rows = Students
# Columns = Subjects

marks = np.array([
    [85, 90, 78],
    [76, 88, 92],
    [95, 89, 94],
    [70, 75, 80]
])

print("\nOriginal Marks Matrix")
print("Rows    -> Students")
print("Columns -> Subjects")

print(marks)

print("\nShape:", marks.shape)


# Flatten data for processing
flat_marks = marks.flatten()

print("\nAll Marks in 1-D:")
print(flat_marks)


# Calculate average marks
average = np.mean(marks)

print("\nAverage Marks:", average)


# Transpose matrix
subject_wise = marks.T

print("\nSubject Wise Data:")
print(subject_wise)


# Reshape data
reshaped = marks.reshape(2, 6)

print("\nReshaped Data (2 x 6):")
print(reshaped)


print("\nHighest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))


# ============================================================
# STUDENT MARKS DATA TRANSFORMATION
# ============================================================

# Original Marks Matrix
# Rows    -> Students
# Columns -> Subjects
# [[85 90 78]
#  [76 88 92]
#  [95 89 94]
#  [70 75 80]]

# Shape: (4, 3)

# All Marks in 1-D:
# [85 90 78 76 88 92 95 89 94 70 75 80]

# Average Marks: 84.33333333333333

# Subject Wise Data:
# [[85 76 95 70]
#  [90 88 89 75]
#  [78 92 94 80]]

# Reshaped Data (2 x 6):
# [[85 90 78 76 88 92]
#  [95 89 94 70 75 80]]

# Highest Marks: 95
# Lowest Marks: 70