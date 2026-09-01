# NumPy Array Manipulation

NumPy provides several functions to change the structure and shape of arrays.

Array manipulation is useful in:

- Data preprocessing
- Machine Learning
- Deep Learning
- Data transformation
- Image processing
- Scientific computing

---

## Topics Covered

1. reshape()
2. resize()
3. flatten()
4. ravel()
5. transpose()

---

# 1. reshape()
The `reshape()` function is used to change the shape of an array without changing its data.
### Syntax
```python
numpy.reshape(array, new_shape)
```
import numpy as np
arr = np.arange(12)
new_arr = arr.reshape(3, 4)
print(new_arr)
Output:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

# 2. resize()
The resize() function changes the shape and size of an array.
If the new size is larger, NumPy repeats the existing elements.
### Syntax
```python
numpy.resize(array, new_shape)
```
import numpy as np
arr = np.array([1, 2, 3, 4])
new_arr = np.resize(arr, (3, 3))
print(new_arr)

# 3. flatten()
The flatten() function converts a multidimensional array into a one-dimensional array.
It returns a copy of the original array.
### Syntax
```python
array.flatten()
```
arr = np.array([[1, 2], [3, 4]])
result = arr.flatten()
print(result)
Output:
[1 2 3 4]

# 4. ravel()
The ravel() function converts a multidimensional array into a one-dimensional array.
Unlike flatten(), ravel() usually returns a view of the original array.
### Syntax
```python
numpy.ravel(array)
```
arr = np.array([[1, 2], [3, 4]])
result = arr.ravel()
print(result)
Output:
[1 2 3 4]

# 5. transpose()
The transpose() function converts rows into columns and columns into rows.
### Syntax
```python
numpy.transpose(array)
or
array.T
```
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)
Output:

[[1 4]
 [2 5]
 [3 6]]