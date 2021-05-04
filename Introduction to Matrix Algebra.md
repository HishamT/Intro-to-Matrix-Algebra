# **Introduction to Matrix Algebra**

## Introduction

A **matrix** is an ordered collection of numbers that facilities mathematical operations and is used in a number of fields in science, mathematics, and engineering. Common fields in which **matrices** (plural of matrix) and their applications are prevalent are: solving systems of linear equations in electrical, mechanical, and chemical engineering. In control and aerospace engineering, matrices are used to describe the state of a physical system and to study its motion in time and space. In data science, matrices are used to store and manipulate large sets of data. In game development, matrices are used to animate things that change on the players screen. There are of course many more applications but before we begin the study of a matrix, we will first define some terms.

## Matrix

A **matrix** (plural **matrices**) is simply a collection of numbers arranged in rectangular form. A matrix with *m* rows and *n* columns is called an *m-by-n matrix* and can be written as follows:  

![Matrix](m_by_n_Matrix.png "Matrix")

Let's take a *2-by-2* matrix **A** as an example:

![2-by-2 Matrix](A_matrix.png "2-by-2 Matrix")

The number of rows and columns are also known as the **dimensions** of the matrix.

When referring to an element inside a matrix (**A**), we denote the element at row *i* and column *j* as *a*<sub>*i*,*j*</sub>. 

A *1-by-n matrix* is called a **row vector**:

![Row Vector](row_vector.png "Row Vector")

Similarly, an *m-by-1 matrix* is called a **column vector**:

![Column Vector](column_vector.png "Column Vector")

A matrix where the number of rows equals the number of columns, an *n-by-n matrix*, is called a **square matrix**.

A *1-by-1 matrix* is known as a **scalar** and is simply written as a traditional number and is treated as such.

We will introduce more types of matrices as we need them later in this article.

## Matrix Operations

Now that we have introduced matrices, we will explore the types of operations we can perform on them.

Two matrices are considered **equal** if their corresponding elements are equal.


We can extend the idea of addition to matrices. Two matrices are added together by simply adding the elements of one matrix to the corresponding elements of another matrix.

Let's take the addition of matrices **A** and **B** as an example:  

![Matrix Addition](matrix_addition.png "Matrix Addition")  


It is important to note the following properties for matrix addition:

* Matrix addition is only possible if the dimensions of the matrices are the same. The addition of two matrices of different dimensions is undefined.
* Matrix addition is commutative: **A** + **B** = **B** + **A**
* Matrix addition is associative: (**A** + **B**) + **C** = **A** + (**B** + **C**)

Matrix subtraction works in the exact same way as matrix addition and is subject to the same properties with the exception that matrix subtraction is *NOT* commutative.


There are two forms of matrix multiplication
* Multiplication by a scalar
* Multiplication by another matrix

In order to multiply matrix **A** by a scalar *k* (remember, a scalar is just a number) one simply multiplies each element of the matrix by the number *k*:

![Scalar Multiplication](scalar_multiplication.png "Scalar Multiplication")

The following properties hold for scalar multiplication:
* Scalar multiplication is distributive for scalars: (*k* + *q*)**A** = *k***A** + *q***A**
* Scalar multiplication is also distributive for matrices: *k*(**A** + **B**) = *k***A** + *k***B**

The more complex of the two multiplication operations available is matrix multiplication.
First, a very important rule:
> **The multiplication of the two matrices **A** and **B** is only possible if the column dimension of matrix A is the same as the row dimension of matrix B**. 

This operation will produce a matrix (call it **C**) with the same number of rows as matrix A and the same number of columns as matrix **B**. For example, if matrix **A** is a *m-by-3* matrix, **B** must be a *3-by-n* matrix and this will generate an *m-by-n* matrix. Carrying out the matrix multiplication **C** = **A** **B** is done by the following formula:

![Elements of Matrix Multiplication](matrix_multiplication_elements.png "Elements of Matrix Multiplication")

It is actually easier to see how this works when you consider the following example:

![Matrix Multiplication](matrix_multiplication_symbolic.png "Matrix Multiplication")

Let's do this with some numbers:  

![Matrix Multiplication](matrix_multiplication_numeric.png "Matrix Multiplication")

![Matrix Multiplication](matrix_multiplication_example.png "Matrix Multiplication")

As you can see, matrix multiplication is tedious and impractical to perform manually, so we require the use of a computer. Later on in this article, we will see how this operation is done in Python using the NumPy library. 

Matrix multiplication has the following properties:
* Matrix multiplication is associative: (**A** **B**) **C** = **A** (**B** **C**)
* Matrix multiplication is distributive: **A**(**B** + **C**) = **A** **B** + **A** **C**
* And most importantly, remember that matrix multiplication **IS NOT** commutative!

There exists a special kind of square matrix knows as the **identity matrix**. This is a square matrix that contains ones on the main diagonal and zeros everywhere else. Since an identity matrix is necessarily sqaure (*n-by-n*), we need only one number (*n*) to specify its dimensions. We denote a general identity matrix by **I** and an *n-by-n* identity matrix as **I**<sub>**n**</sub>. It looks like this:

![Identity Matrix](general_id_matrix.png "Identity Matrix")

Multiplication by an identity matrix yields the original matrix and this is one of the few times where matrix multplication is commutative!
* **A** **I** = **I** **A** = **A**

Another special matrix we will consider is the **inverse matrix** of a general matrix **A** denoted as **A**<sup>-1</sup>. This inverse matrix is only defined for square matrices and bears the special property:
* **A** **A**<sup>-1</sup> = **A**<sup>-1</sup> **A** = **I**

However, generating an inverse matrix for **A** is a fairly complex task that is beyond the scope of this introductory lesson on matrix algebra and merits its own dedicated article. Often times, courses in linear algebra devote one full lecture solely to calculating the inverse of a matrix. As with matrix multiplication, the calculation of an inverse matrix is not practical to be performed by a human and thus the use of a computer is necessary. We will see how to do this in Python later in this article.

## Matrix Algebra in Python

When dealing with large matrices, the use of a computer is necessary to carry out the operations mentioned in the previous section. There are many software packages available that facilitate the maniuplation of a matrix as well as libraries that exist for common computer languages which allow us to perfomr the necessary computations. The main langauge we will be using to work with a matrix is Python (Python3) and specifically the NumPy library. We assume you are familiar with basic Python syntax and how to write Python code. We also assume you know how to download and install libraries using the `pip` command.   

In order to use NumPy, we must first import it:
```python
import numpy as np
```

A vector (1D matrix) is created in the following way:

```python
V = np.array([1,2,3])
```
This creates a row-vector with three elements. This is just a regular array.

Creating a 2D matrix:

```python
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
```

![Matrix](matrix_A.png "Matrix")  
Note that a 2D matrix is simply represented as an array that contains other arrays as elements.

Accessing the element at row *i* and column *j* is done by writing `A[i][j]`. However please keep in mind that while in mathematics counting starts at `1`, in computer science counting starts at `0`. Therefore the first element in matrix **A** is at `A[0][0]` *not* `A[1][1]`

Adding/subtracting two matrices uses the same syntax as adding two variables: 

```python
C = A + B
# or C = A - B
```

Scalar multiplication (assuming *k* is a number):
```python
B = k*A
```

To multiply two matrices, we do not use the * operator as we did in scalar multiplication as that would just do element-wise multiplication. We write `np.matmul(A,B)` to perform the matrix multiplication as described earlier. Remember to make sure the column-dimension of matrix **A** is the same as the row-dimension as matrix **B** or you will get an error.

Let's actually do the example from the previous section:

```python
import numpy as np
A = np.array([[4,6,3], [1,3,2]])
B = np.array([[1,4],[5,10],[8,12]])
C = np.matmul(A,B)
print(C)

'''
This will output:
[[ 58 112]
 [ 32  58]]
 Same as before.
'''

```
The python function to find the inverse of a matrix is located in the `linalg` submodule of numpy. The following code demonstrates the inversion of a matrix:

```python
import numpy as np
A = np.array([[1,3,2],[4,5,6],[8,7,9]])
A_inv = np.linalg.inv(a)
print(A_inv)

'''
This will output: 
 [[ 0.2        -0.86666667  0.53333333]
 [ 0.8        -0.46666667  0.13333333]
 [-0.8         1.13333333 -0.46666667]]
'''
```

## Applications of matrices: System of Linear Equations

In many fields of engineering, math, and science, linear equations are prevalent and important. As you remember from high school algebra class, a linear equation is presented in the form *ax + by = c*. Often it is necessary to obtain a solution to a *system of linear equations* which is more than one equation simultaneously. An example of this is:

>2x + 4y = 18  
4x - 2y = 16

As you learned in algebra class, this system of two linear equations can be solved by the elimination technique to yield a solution of *x = 5* and *y = 2*.  
In general, you can have a system of infintely many equations as long as you have as many equations as unknowns. Writing a system of equations as we have shown previously is fine for a small number of equations but will become awkward and hard to read as the number of equations increases. To solve this problem, we can write systems of equations compactly using a ***matrix***. To illustrate this, let's take the following system as an example:

>2x + 6y + z = 7  
x + 2y - z = -1  
5x + 7y - 4z = 9

This system of equations can be elegantly represented using a matrix:

 ![Matrix](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/Matrix_1.png "matrix")

We will show the how to use matrices to solve systems of equations later in this article after some properties and techniques are introduced.

This is also just one application of matrix.



















