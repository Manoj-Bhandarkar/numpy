# NumPy Indexing and Slicing

## 1. Introduction
There are mainly two techniques used to access elements in a NumPy array:
1. Indexing
2. Slicing

---

# 2. Indexing
Indexing means accessing a specific element from an array

Using indexing in NumPy:
- Single element
- Row / Column
- Specific element from multidimensional array
can be accessed.
---

## 2.1 Indexing with 1-D Array

### Example

```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0])   # 10
print(a[2])   # 30
print(a[-1])  # 50