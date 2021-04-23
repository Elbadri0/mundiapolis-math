# mundiapolis-math :man_student:
Holbertonschool-mundiapolis
Tasks 

## Task 💪

<details>
<summary>View Contents</summary>

#### 0\. Slice Me Up mandatory

Complete the following source code (found below):

*   `arr1` should be the first two numbers of `arr`
*   `arr2` should be the last five numbers of `arr`
*   `arr3` should be the 2nd through 6th numbers of `arr`
*   You are not allowed to use any loops or conditional statements
*   Your program should be exactly 8 lines

#### 1\. Trim Me Down mandatory

Complete the following source code (found below):

*   `the_middle` should be a 2D matrix containing the 3rd and 4th columns of `matrix`
*   You are not allowed to use any conditional statements
*   You are only allowed to use one `for` loop
*   Your program should be exactly 6 lines

#### 2\. Size Me Please mandatory

Write a function `def matrix_shape(matrix):` that calculates the shape of a matrix:

*   You can assume all elements in the same dimension are of the same type/shape
*   The shape should be returned as a list of integers

#### 3\. Flip Me Over mandatory

Write a function `def matrix_transpose(matrix):` that returns the transpose of a 2D matrix, `matrix`:

*   You must return a new matrix
*   You can assume that `matrix` is never empty
*   You can assume all elements in the same dimension are of the same type/shape

#### 4\. Line Up mandatory

Write a function `def add_arrays(arr1, arr2):` that adds two arrays element-wise:

*   You can assume that `arr1` and `arr2` are lists of ints/floats
*   You must return a new list
*   If `arr1` and `arr2` are not the same shape, return `None`



#### 5\. Across The Planes mandatory

Write a function `def add_matrices2D(mat1, mat2):` that adds two matrices element-wise:

*   You can assume that `mat1` and `mat2` are 2D matrices containing ints/floats
*   You can assume all elements in the same dimension are of the same type/shape
*   You must return a new matrix
*   If `mat1` and `mat2` are not the same shape, return `None`

**Repo:**

*   GitHub repository: `holbertonschool-machine_learning`
*   Directory: `math/0x00-linear_algebra`
*   File: [`5-across_the_planes.py`](./5-across_the_planes.py)



#### 6\. Howdy Partner mandatory

Write a function `def cat_arrays(arr1, arr2):` that concatenates two arrays:

*   You can assume that `arr1` and `arr2` are lists of ints/floats
*   You must return a new list

#### 7\. Gettin’ Cozy mandatory

Write a function `def cat_matrices2D(mat1, mat2, axis=0):` that concatenates two matrices along a specific axis:

*   You can assume that `mat1` and `mat2` are 2D matrices containing ints/floats
*   You can assume all elements in the same dimension are of the same type/shape
*   You must return a new matrix
*   If the two matrices cannot be concatenated, return `None`


#### 8\. Ridin’ Bareback mandatory

Write a function `def mat_mul(mat1, mat2):` that performs matrix multiplication:

*   You can assume that `mat1` and `mat2` are 2D matrices containing ints/floats
*   You can assume all elements in the same dimension are of the same type/shape
*   You must return a new matrix
*   If the two matrices cannot be multiplied, return `None`


#### 9\. Let The Butcher Slice It mandatory

Complete the following source code (found below):

*   `mat1` should be the middle two rows of `matrix`
*   `mat2` should be the middle two columns of `matrix`
*   `mat3` should be the bottom-right, square, 3x3 matrix of `matrix`
*   You are not allowed to use any loops or conditional statements
*   Your program should be exactly 10 lines



#### 10\. I’ll Use My Scale mandatory

Write a function `def np_shape(matrix):` that calculates the shape of a `numpy.ndarray`:

*   You are not allowed to use any loops or conditional statements
*   You are not allowed to use `try/except` statements
*   The shape should be returned as a tuple of integers
    

#### 11\. The Western Exchange mandatory

Write a function `def np_transpose(matrix):` that transposes `matrix`:

*   You can assume that `matrix` can be interpreted as a `numpy.ndarray`
*   You are not allowed to use any loops or conditional statements
*   You must return a new `numpy.ndarray`



#### 12\. Bracing The Elements mandatory

Write a function `def np_elementwise(mat1, mat2):` that performs element-wise addition, subtraction, multiplication, and division:

*   You can assume that `mat1` and `mat2` can be interpreted as `numpy.ndarray`s
*   You should return a tuple containing the element-wise sum, difference, product, and quotient, respectively
*   You are not allowed to use any loops or conditional statements
*   You can assume that `mat1` and `mat2` are never empty

#### 13\. Cat's Got Your Tongue mandatory

Write a function `def np_cat(mat1, mat2, axis=0)` that concatenates two matrices along a specific axis:

*   You can assume that `mat1` and `mat2` can be interpreted as `numpy.ndarray`s
*   You must return a new `numpy.ndarray`
*   You are not allowed to use any loops or conditional statements
*   You may use: `import numpy as np`
*   You can assume that `mat1` and `mat2` are never empty


#### 14\. Saddle Up mandatory

Write a function `def np_matmul(mat1, mat2):` that performs matrix multiplication:

*   You can assume that `mat1` and `mat2` are `numpy.ndarray`s
*   You are not allowed to use any loops or conditional statements
*   You may use: `import numpy as np`
*   You can assume that `mat1` and `mat2` are never empty



#### 15\. Slice Like A Ninja 

Write a function `def np_slice(matrix, axes={}):` that slices a matrix along a specific axes:

*   You can assume that `matrix` is a `numpy.ndarray`
*   You must return a new `numpy.ndarray`
*   `axes` is a dictionary where the `key` is an axis to slice along and the `value` is a tuple representing the slice to make along that axis
*   You can assume that axes represents a valid slice
*   [Hint](/rltoken/e-cIWjiDH3MX5U51hGPgtw "Hint")

#### 16\. The Whole Barn 

Write a function `def add_matrices(mat1, mat2):` that adds two matrices:

*   You can assume that `mat1` and `mat2` are matrices containing ints/floats
*   You can assume all elements in the same dimension are of the same type/shape
*   You must return a new matrix
*   If matrices are not the same shape, return `None`
*   You can assume that `mat1` and `mat2` will never be empty



#### 17\. Squashed Like Sardines 

Write a function `def cat_matrices(mat1, mat2, axis=0):` that concatenates two matrices along a specific axis:

*   You can assume that `mat1` and `mat2` are matrices containing ints/floats
*   You can assume all elements in the same dimension are of the same type/shape
*   You must return a new matrix
*   If you cannot concatenate the matrices, return `None`
*   You can assume that `mat1` and `mat2` are never empty

_Note the time difference between the standard `Python3` library and the `numpy` library is an order of magnitude! When you have matrices with millions of data points, this time adds up!_

</details>

---
