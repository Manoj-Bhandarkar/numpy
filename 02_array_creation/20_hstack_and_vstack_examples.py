import numpy as np

print("========== Student Marks ==========")

physics = np.array([[80], [75], [90]])
maths = np.array([[70], [88], [95]])

report = np.hstack((physics, maths))

print(report)

print("\n========== Monthly Sales ==========")

jan = np.array([[1000, 1200]])
feb = np.array([[1300, 1400]])
mar = np.array([[1600, 1800]])

sales = np.vstack((jan, feb, mar))

print(sales)

print("\n========== Employee Data ==========")

ids = np.array([[101], [102], [103]])
salary = np.array([[50000], [65000], [72000]])

employee = np.hstack((ids, salary))

print(employee)