# NumPy Introduction

## What is NumPy?

NumPy (Numerical Python) is an open-source Python library used for numerical computing and efficient array processing. It provides a powerful `ndarray` (N-dimensional array) data structure that allows developers to perform mathematical and scientific computations efficiently.

NumPy is widely used in:

- Data Science
- Machine Learning
- Artificial Intelligence
- Scientific Computing
- Data Analysis
- Image Processing

---

## Brief History

- NumPy was created by **Travis Oliphant** in **2005**.
- It evolved from the earlier **Numeric** library.
- It is primarily written in **Python** and **C**.
- Today, it is one of the core libraries in the Python scientific ecosystem.

---

## Why Use NumPy?

NumPy offers several advantages over Python lists:

- Faster execution
- Lower memory usage
- Vectorized operations
- Built-in mathematical functions
- Support for 1D, 2D, and N-dimensional arrays
- Easy array reshaping and manipulation

---

## Installation

```bash
pip install numpy
```

---

## Import NumPy

```python
import numpy as np
```

Using `np` is the standard convention.

---

## The ndarray Object

The core object in NumPy is `ndarray`.

```python
import numpy as np

numbers = [10, 20, 30]

arr = np.array(numbers)

print(arr)
print(type(arr))
```

Output

```
[10 20 30]
<class 'numpy.ndarray'>
```

---

## Python List vs NumPy Array

### Python List

```python
numbers = [10, 20, 30]

# numbers + 1   # TypeError
print(numbers * 2)
```

Output

```
[10, 20, 30, 10, 20, 30]
```

### NumPy Array

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr + 1)
print(arr * 2)
```

Output

```
[11 21 31]
[20 40 60]
```

---

## Key Points

- NumPy stands for Numerical Python.
- The main data structure is `ndarray`.
- NumPy arrays are homogeneous (all elements have the same data type).
- NumPy supports vectorized operations without explicit loops.
- It is much faster and more memory-efficient than Python lists for numerical computations.