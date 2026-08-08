# Splitting the ndarray

NumPy provides functions to split a single ndarray into multiple smaller arrays.

Splitting is useful when we want to divide a large dataset or matrix into smaller parts for processing.

## Splitting Functions

NumPy provides the following important splitting functions:

1. `np.split()`
2. `np.array_split()`
3. `np.vsplit()`
4. `np.hsplit()`
5. `np.dsplit()`

---

## 1. split()
np.split() divides an array into equal-sized sub-arrays.
### Syntax

```python
numpy.split(array, indices_or_sections, axis=0)
---

## 2. array_split()

np.array_split() is similar to np.split(), but it can also divide an array into unequal-sized parts.
---


## 3. vsplit()

np.vsplit() splits an array vertically along the rows.

It is mainly used with 2-D or higher-dimensional arrays.
---
numpy.vsplit(array, sections)
---
    
