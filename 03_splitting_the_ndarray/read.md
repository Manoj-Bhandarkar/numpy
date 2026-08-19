# Splitting the ndarray

NumPy provides functions to split a single ndarray into multiple smaller arrays. Splitting is useful when we want to divide a large dataset or matrix into smaller parts for parallel processing or specific analysis.

---

## Splitting Functions

NumPy provides the following important splitting functions:

1. `np.split()` — Splits an array into multiple sub-arrays of equal size.
2. `np.array_split()` — Splits an array into equal or unequal-sized sub-arrays.
3. `np.vsplit()` — Splits an array vertically (row-wise).
4. `np.hsplit()` — Splits an array horizontally (column-wise).
5. `np.dsplit()` — Splits an array along the 3rd axis (depth-wise).

---

## 1. np.split()

`np.split()` divides an array into **equal-sized** sub-arrays. If an equal split is not possible, it raises a `ValueError`.

### Syntax
```python
numpy.split(array, indices_or_sections, axis=0)
```

### Parameters
* **`array`**: The source ndarray to be split.
* **`indices_or_sections`**: 
  * If an integer \(N\), the array will be split into \(N\) equal arrays along the axis.
  * If a 1-D array of sorted integers, the entries indicate where the array is split.
* **`axis`**: The axis along which to split (default is `0`).

---

## 2. np.array_split()

`np.array_split()` is similar to `np.split()`, but it **allows unequal-sized splits**. If the array size cannot be divided equally, the remaining elements are distributed among the sub-arrays from the beginning.

### Syntax
```python
numpy.array_split(array, indices_or_sections, axis=0)
```

---

## 3. np.vsplit()

`np.vsplit()` splits an array **vertically** along the rows (axis 0). It is equivalent to `np.split(..., axis=0)`.

* It is mainly used with 2-D or higher-dimensional arrays.
* The array must be split into equal sections, otherwise a `ValueError` is raised.

### Syntax
```python
numpy.vsplit(array, sections)
```
