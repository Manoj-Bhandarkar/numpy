# NumPy Statistical Operations

NumPy provides many built-in functions to perform statistical analysis on numerical data.

Statistical operations are widely used in:

- Data Analysis
- Data Science
- Machine Learning
- Business Analytics
- Scientific Computing

## Topics Covered

1. Minimum - `np.min()` / `np.amin()`
2. Maximum - `np.max()` / `np.amax()`
3. Sum - `np.sum()`
4. Mean - `np.mean()`
5. Median - `np.median()`
6. Variance - `np.var()`
7. Standard Deviation - `np.std()`
8. Percentile - `np.percentile()`
9. Axis-based operations
10. Mode using Python `statistics` module

---

## Important Statistical Functions

| Function | Description |
|----------|-------------|
| `np.min()` | Returns minimum value |
| `np.max()` | Returns maximum value |
| `np.sum()` | Returns sum of elements |
| `np.mean()` | Returns average value |
| `np.median()` | Returns middle value |
| `np.var()` | Returns variance |
| `np.std()` | Returns standard deviation |
| `np.percentile()` | Returns percentile value |

---

## Understanding Axis

For a 2-D array:

- `axis=0` → Performs operation column-wise
- `axis=1` → Performs operation row-wise

Example:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

np.sum(arr, axis=0)
# [50 70 90]

np.sum(arr, axis=1)
# [ 60 150]