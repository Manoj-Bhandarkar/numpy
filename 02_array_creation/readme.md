# NumPy `array()` Function

## What is `np.array()`?

`np.array()` is used to convert Python objects into a NumPy `ndarray`.

An `ndarray` (N-dimensional array) is the core data structure of NumPy. It provides fast numerical operations, efficient memory usage, and supports vectorized computations.

## Syntax

```python
import numpy as np

np.array(object, dtype=None)
```

### Parameters

- **object** – Any Python object such as:
  - int
  - float
  - string
  - list
  - tuple
  - range
  - set
  - dictionary
- **dtype** *(optional)* – Specifies the data type of the array.

---

# Converting Different Python Objects

## 1. Integer → ndarray

```python
import numpy as np

arr = np.array(10)

print(arr)
print(arr.ndim)
```

### Output

```text
10
0
```

### Notes

- Creates a **0-dimensional array (scalar array)**.
- Shape is `()`.
- Size is `1`.

---

## 2. Float → ndarray

```python
arr = np.array(12.5)
```

### Notes

- Creates a 0-D array.
- Default dtype is `float64`.

---

## 3. String → ndarray

```python
arr = np.array("Python")
```

### Notes

- Creates a 0-D array.
- dtype becomes `<U6` because the string contains 6 Unicode characters.

---

## 4. Range → ndarray

```python
arr = np.array(range(6))
```

Output

```text
[0 1 2 3 4 5]
```

### Notes

- Creates a **1-D array**
- Shape → `(6,)`
- Size → `6`

---

## 5. List → ndarray

```python
numbers = [10,20,30,40]

arr = np.array(numbers)
```

### Notes

- Creates a **1-D array**
- All elements have the same data type.
- Supports vectorized operations.

---

## 6. Using dtype

```python
arr = np.array([10,20,30], dtype=float)
```

Output

```text
[10. 20. 30.]
```

### Notes

- Converts every element to float.
- Useful when calculations require decimal values.

---

## 7. Reshaping an Array

```python
arr = np.array(range(1,10))

arr = arr.reshape(3,3)
```

Output

```text
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

### Notes

- Changes the array's dimensions.
- Total number of elements must remain the same.

Example

✅ 9 → 3 × 3

❌ 9 → 2 × 5

---

## 8. Tuple → ndarray

```python
matrix = (
    (10,20,30),
    (40,50,60),
    (70,80,90)
)

arr = np.array(matrix)
```

### Notes

- Creates a **2-D array**
- Shape → `(3,3)`

---

## 9. Set → ndarray

```python
arr = np.array({10,20,30})
```

### Notes

- NumPy treats the entire set as one Python object.
- Result is a **0-D object array**.
- Sets are unordered.

---

## 10. Dictionary → ndarray

```python
arr = np.array({1:"Python",2:"Java"})
```

### Notes

- Dictionary is stored as a single object.
- Creates a **0-D object array**.

---

# ndarray Attributes

| Attribute | Description |
|-----------|-------------|
| ndim      | Number of dimensions |
| shape     | Shape of array |
| size      | Total number of elements |
| dtype     | Data type of elements |

Example

```python
arr = np.array([10,20,30])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

Output

```text
1
(3,)
3
int64
```

---

# Summary

| Python Object | NumPy Result |
|---------------|--------------|
| int           | 0-D ndarray |
| float         | 0-D ndarray |
| string        | 0-D ndarray |
| list          | 1-D ndarray |
| tuple         | 2-D ndarray |
| range         | 1-D ndarray |
| set           | 0-D object array |
| dictionary    | 0-D object array |

---

# Key Interview Points

### What is ndarray?

An ndarray is the primary data structure in NumPy used to store homogeneous data efficiently.

---

### Why use ndarray instead of Python List?

- Faster execution
- Less memory usage
- Supports vectorized operations
- Easy reshaping
- Built-in mathematical functions

---

### What is a 0-D array?

A scalar stored as an ndarray.

Example

```python
np.array(10)
```

Output

```text
array(10)
```

---

### What is dtype?

`dtype` specifies the data type of array elements.

Example

```python
np.array([1,2,3], dtype=float)
```

Output

```text
array([1., 2., 3.])
```

---

## Best Practice

- Use **list** or **tuple** when creating arrays.
- Avoid using **set** and **dictionary** directly with `np.array()` because they produce object arrays instead of numerical arrays.