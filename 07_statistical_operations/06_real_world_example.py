import numpy as np

# Rows = Students
# Columns = Subjects

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 92, 95],
    [45, 50, 55],
    [70, 75, 82]
])

subjects = ["Python", "SQL", "Machine Learning"]

print("Student Marks:")
print(marks)

# Overall statistics
print("\nOverall Statistics")

print("Minimum Marks:", np.min(marks))
print("Maximum Marks:", np.max(marks))
print("Average Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Standard Deviation:", np.std(marks))

# Subject-wise average
print("\nSubject-wise Average:")

subject_average = np.mean(marks, axis=0)

for subject, average in zip(subjects, subject_average):
    print(f"{subject}: {average:.2f}")

# Student-wise average
print("\nStudent-wise Average:")

student_average = np.mean(marks, axis=1)

for index, average in enumerate(student_average, start=1):
    print(f"Student {index}: {average:.2f}")
    
    
# Student Marks:
# [[78 85 90]
#  [65 72 80]
#  [88 92 95]
#  [45 50 55]
#  [70 75 82]]

# Overall Statistics
# Minimum Marks: 45
# Maximum Marks: 95
# Average Marks: 74.8
# Median Marks: 78.0
# Standard Deviation: 14.887130907823263

# Subject-wise Average:
# Python: 69.20
# SQL: 74.80
# Machine Learning: 80.40

# Student-wise Average:
# Student 1: 84.33
# Student 2: 72.33
# Student 3: 91.67
# Student 4: 50.00
# Student 5: 75.67