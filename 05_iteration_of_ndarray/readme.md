# Iterating NumPy Arrays

Iteration means accessing array elements one by one.

NumPy arrays can be iterated using:

1. Python `for` loop
2. Nested loops
3. `np.nditer()`
4. `np.ndenumerate()`

## 1. Iterating 1-D Array

A simple `for` loop can be used to iterate through each element.

## 2. Iterating 2-D Array

When iterating a 2-D array using a normal `for` loop, NumPy returns each row.

Nested loops can be used to access individual elements.

## 3. Iterating 3-D Array

For multidimensional arrays, multiple nested loops can be used.

However, NumPy provides better functions such as `nditer()`.

## 4. np.nditer()

`np.nditer()` is used to efficiently iterate over every element of an ndarray regardless of its dimensions.

## 5. np.ndenumerate()

`np.ndenumerate()` iterates through array elements and also provides their index positions.

## Why Iteration is Important?

Iteration is useful when:

- Processing array elements
- Performing custom operations
- Accessing multidimensional data
- Finding positions of elements
- Data preprocessing

> In NumPy, vectorized operations are generally preferred over Python loops for better performance.