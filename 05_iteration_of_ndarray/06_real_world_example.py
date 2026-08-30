import numpy as np

# Marks of students
marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 92, 95]
])
subjects = ["Python", "SQL", "Machine Learning"]
print("Student Marks Matrix:")
print(marks)
print("\nAll Marks with Position:")
for index, mark in np.ndenumerate(marks):
    student = index[0] + 1
    subject = subjects[index[1]]
    print(
        f"Student {student} | "
        f"{subject} | "
        f"Marks: {mark}"
    )

# Student Marks Matrix:
# [[78 85 90]
#  [65 72 80]
#  [88 92 95]]

# All Marks with Position:
# Student 1 | Python | Marks: 78
# Student 1 | SQL | Marks: 85
# Student 1 | Machine Learning | Marks: 90
# Student 2 | Python | Marks: 65
# Student 2 | SQL | Marks: 72
# Student 2 | Machine Learning | Marks: 80
# Student 3 | Python | Marks: 88
# Student 3 | SQL | Marks: 92
# Student 3 | Machine Learning | Marks: 95