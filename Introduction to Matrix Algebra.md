# **Introduction to Matrix Algebra**

## Introduction

A **matrix** is an ordered collection of numbers that facilitates mathematical operations that are necessary in a number of fields in science, mathematics, and engineering. A common use of a matrix and its applications is the solution of systems of linear equations in electrical, mechanical, and chemical engineering. In control and aerospace engineering, **matrices** (plural of matrix) are used to describe the state of a physical system and to study its motion in time and space. In data science, matrices are used to store and manipulate large sets of data. Computer scientists and software engineers use matrices in fields like game development and cyber security. These are just a few of the many applications of matrix algebra. Before we begin the study of a matrix, we must first define some important terms.

## Matrix

A **matrix** (plural **matrices**) is simply a collection of numbers arranged in rectangular form. A matrix with *m* rows and *n* columns is called an *m-by-n matrix* and can be written as follows:  

![Matrix](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/m_by_n_Matrix.png "Matrix")

Let's take a *2-by-2* matrix **A** as an example:

![2-by-2 Matrix](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/A_matrix.png "2-by-2 Matrix")

The number of rows and columns are also known as the **dimensions** of the matrix.

When referring to an element inside a matrix (**A**), we denote the element at row *i* and column *j* as *a*<sub>*i*,*j*</sub>. 

A *1-by-n matrix* is called a **row vector**:

![Row Vector](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/row_vector.png "Row Vector")

Similarly, an *m-by-1 matrix* is called a **column vector**:

![Column Vector](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/column_vector.png "Column Vector")

A matrix where the number of rows equals the number of columns, an *n-by-n matrix*, is called a **square matrix**.

A *1-by-1 matrix* is known as a **scalar** and is simply written as a traditional number and is treated as such.

We will introduce more types of matrices as we need them later in this article.

## Matrix Operations

Now that we have introduced matrices, we will explore the types of operations we can perform on them.

Two matrices are considered **equal** if their corresponding elements are equal.


We can extend the idea of addition to matrices. Two matrices are added together by simply adding the elements of one matrix to the corresponding elements of another matrix.

Let's take the addition of matrices **A** and **B** as an example:  

![Matrix Addition](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/matrix_addition.png "Matrix Addition")  


It is important to note the following properties for matrix addition:

* Matrix addition is only possible if the dimensions of the matrices are the same. The addition of two matrices of different dimensions is undefined.
* Matrix addition is commutative: **A** + **B** = **B** + **A**
* Matrix addition is associative: (**A** + **B**) + **C** = **A** + (**B** + **C**)

Matrix subtraction works in the exact same way as matrix addition and is subject to the same properties with the exception that matrix subtraction is *NOT* commutative.


There are two forms of matrix multiplication
* Multiplication by a scalar
* Multiplication by another matrix

In order to multiply matrix **A** by a scalar *k* (remember, a scalar is just a number) one simply multiplies each element of the matrix by the number *k*:

![Scalar Multiplication](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/scalar_multiplication.png "Scalar Multiplication")

The following properties hold for scalar multiplication:
* Scalar multiplication is distributive for scalars: (*k* + *q*)**A** = *k***A** + *q***A**
* Scalar multiplication is also distributive for matrices: *k*(**A** + **B**) = *k***A** + *k***B**

The more complex of the two multiplication operations available is matrix multiplication.
First, a very important rule:
> **The multiplication of the two matrices **A** and **B** is only possible if the column dimension of matrix A is the same as the row dimension of matrix B**. 

This operation will produce a matrix (call it **C**) with the same number of rows as matrix A and the same number of columns as matrix **B**. For example, if matrix **A** is a *m-by-3* matrix, **B** must be a *3-by-n* matrix and this will generate an *m-by-n* matrix. Carrying out the matrix multiplication **C** = **A** **B** is done by the following formula:

![Elements of Matrix Multiplication](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/matrix_multiplication_elements.png "Elements of Matrix Multiplication")

It is actually easier to see how this works when you consider the following example:

![Matrix Multiplication](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/matrix_multiplication_symbolic.png "Matrix Multiplication")

Let's do this with some numbers:  

![Matrix Multiplication](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/matrix_multiplication_numeric.png "Matrix Multiplication")

![Matrix Multiplication](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/matrix_multiplication_example.png "Matrix Multiplication")

As you can see, matrix multiplication is tedious and impractical to perform manually, therefore we require the use of a computer. Later on in this article we will see how this operation is done in Python using the NumPy library. 

Matrix multiplication has the following properties:
* Matrix multiplication is associative: (**A** **B**) **C** = **A** (**B** **C**)
* Matrix multiplication is distributive: **A**(**B** + **C**) = **A** **B** + **A** **C**
* And most importantly, remember that matrix multiplication **IS NOT** commutative!

There exists a special kind of square matrix knows as the **identity matrix**. This is a square matrix that contains ones on the main diagonal and zeros everywhere else. Since an identity matrix is necessarily sqaure (*n-by-n*), we need only one number (*n*) to specify its dimensions. We denote a general identity matrix by **I** and an *n-by-n* identity matrix as **I**<sub>**n**</sub>. It looks like this:

![Identity Matrix](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/general_id_matrix.png "Identity Matrix")

A *3-by-3* identity matrix:

![Identity Matrix](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/identity_matrix_3.png "Identity Matrix")

Multiplication by an identity matrix yields the original matrix. This is one of the few times where matrix multplication is commutative!
* **A** **I** = **I** **A** = **A**

Another special matrix we will consider is the **inverse matrix** of a general matrix **A** denoted as **A**<sup>-1</sup>. This inverse matrix is only defined for square matrices and bears the special property:
* **A** **A**<sup>-1</sup> = **A**<sup>-1</sup> **A** = **I**

However, generating an inverse matrix for **A** is a fairly complex task that is beyond the scope of this introductory lesson on matrix algebra. The procedure for computing an inverse matrix merits its own dedicated article. Often times, courses in linear algebra devote one full lecture solely to calculating the inverse of a matrix. As with matrix multiplication, manually performing the calculation of an inverse matrix is not practical, therefore we resort to using a computer to perform this computation for us. We will see how to do this in Python later in this article.

## Matrix Algebra in Python

When dealing with large matrices, the use of a computer is necessary to carry out the operations mentioned in the previous section. There are many software packages available that facilitate matrix operations. For many common computer languages, libraries exist that allow us to work with matrices efficiently. The language we will be using is Python (Python3) and the NumPy library. We assume you are familiar with basic Python syntax and how to write Python code. We also assume you know how to download and install libraries using the `pip` command.   

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

![Matrix](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/matrix_A.png "Matrix")  
Note that a 2D matrix is simply represented as an array that contains other arrays as elements.

Accessing the element at row *i* and column *j* is done by writing `A[i][j]`. However please keep in mind that while in mathematics counting starts at `1`, in computer science counting starts at `0`; therefore the first element in matrix **A** is `A[0][0]` *not* `A[1][1]`

Adding/subtracting two matrices uses the same syntax as adding two variables: 

```python
C = A + B
# or C = A - B
```

Scalar multiplication (assuming *k* is a number):
```python
B = k*A
```

To multiply two matrices, we do not use the * operator as we did in scalar multiplication because that would just perform element-wise multiplication. We write `np.matmul(A,B)` to compute matrix multiplication as described earlier. Remember to make sure the column dimension of matrix **A** is the same as the row dimension as matrix **B** or you will get an error.

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
The python function to find the inverse of a matrix is located in the `linalg` submodule of NumPy. The following code demonstrates the inversion of a matrix:

```python
import numpy as np
A = np.array([[1,3,2],[4,5,6],[8,7,9]])
AInv = np.linalg.inv(a)
print(AInv)

'''
This will output: 
 [[ 0.2        -0.86666667  0.53333333]
 [ 0.8        -0.46666667  0.13333333]
 [-0.8         1.13333333 -0.46666667]]
'''
```

## Applications of Matrices: System of Linear Equations

In many fields of engineering, math, and science, linear equations are ubiquitous and important. As you learned in algebra class, a linear equation is presented in the form *ax + by = c*. A *system of linear equations* is a collection of linear equations. An example of this is:

>2x + 4y = 18  
4x - 2y = 16

As you learned in algebra class, this system of two linear equations can be solved by the elimination technique to yield a solution of *x = 5* and *y = 2*.  
In general, you can have a system of infintely many equations as long as you have as many equations as unknowns. Writing a system of equations as we have shown previously is fine for a small number of equations, but will become awkward and hard to read as the number of equations increases. To solve this problem, we can write systems of equations compactly using a ***matrix***. To illustrate this, let's take the following system as an example:

>2x + 6y + z = 7  
x + 2y - z = -1  
5x + 7y - 4z = 9

We can first break this down to look like this:

![Equation 1](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/equation1.png "Equation 1")

Take note of the patterns in the alignment of the numbers.

This system of equations can be elegantly represented using a matrix:

 ![Matrix](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/Matrix_1.png "matrix")

Systems of linear equations are written in the form **A** **x** = **b**.

In this case:

![A](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/A_matrix_linear_equations.png "A")

![x](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/x_vector.png "x")

![b](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/b_vector.png "b")

To solve this, we first generate the inverse matrix **A**<sup>-1</sup> and then multiply both sides of the equation, *on the left*, by **A**<sup>-1</sup>. Remember, matrix multiplication is **not** commutative.

![Ax=b](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/eq1.png "Ax=b")

![Ax=b](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/eq2.png "Ax=b")

![Ax=b](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/eq3.png "Ax=b")

Let's solve this in Python:
```python
import numpy as np
A = np.array([[2,6,1], [1,2,-1], [5,7,-4]]) # input matrix A
b = np.array([7,-1,9]) # input matrix b
AInv = np.linalg.inv(A) # calculate inverse matrix of A
x = np.matmul(AInv, b) # solve system of equations by left-multiplying b by A-inverse
print(x) # print result

# This will output [10 -3 5]
```
Please note that the solution to a linear system only works if the equations are *linearly independent*. That means that no equation is a multiple, or a combination of, any other equation. Trying to solve this set of equations:
>2x + 6y + z = 7  
4x + 12y +2z = 14   
5x + 7y - 4z = 9

will produce non-sense values as the equations in this system are not linearly independent; the second equation is two-times the first. Determining whether or not a system is linearly independent is outside the scope of this lesson. For now, we will assume they are.

## Applications of Matrices: Data Encryption

Another common application of matrix algebra is in the cyber security domain. Data can be structured in a matrix and encryption algorithms are used to generate a new matrix with encrypted data. After the data are transferred, decryption algorithms are used to recover the original data from the encrypted matrix. To show how this is done, we present an encryption technique that is based on matrix multiplication to encrypt data. While this algorithm is primitive and is not suited for real-world applications, it does show the importance of matrices in the cyber security field.

In order to see how this works, we will first define the encryption matrix **E** which is a square matrix consisting of random numbers and the corresponding decryption matrix **D** which is simply the inverse of **E**. Using **E** and **D** to encrypt and decrypt something takes advantage of the property **D** **E** = **I**. To encrypt a matrix **x**, we generate matrix **y** by left-multiplying **E**. To recover the original matrix **x**, we left-multiply **y** by **D**.

![Decryption](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/y_matrix.png "Decryption")  
![Encryption](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/x_matrix.png "Encryption")

Suppose we wish to encrypt the string "*hello world*". We must first define encryption matrix **E** and decryption matrix **D**:

![Encryption Key](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/encryption_key.png "Encryption Key")  
![Decryption Key](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/decryption_key.png "Decryption Key")

Note that the matrix can be of any size, as long as it is square.

Remember that in order to multiply two matrices, the column dimension of the left matrix must match the row dimension of the right matrix. Therefore in order to multiply a matrix by the *2-by-2* matrix **E**, we need a *2-by-n* matrix. Let's first convert the string into a row vector

![Hello World](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/string_row_vector.png "Hello World")

Since the string *hello world* contains eleven characters (including the space) and we need a *2-by-n* matrix, we need to break the string down into two rows and distribute the characters as evenly as possible. We pad with 0's if we need more characters.

![Hello World](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/hello_matrix.png "Hello World")

We can convert a string into a row-vector of numbers where each number corresponds to the [unicode](https://home.unicode.org/) value of the character. To obtain the unicode value of a character ('a' for example) in python, we use `ord('a')`. To convert from unicode (number *x* for example) to character, we use `chr(x)`.

![Hello World](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/hello_number_matrix.png "Hello World")

After encrypting it with **E**, we get:

![Encrypted Matrix](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/encrypted_matrix.png "Encrypted Matrix")

Which corresponds to unusual characters if it was converted from unicode to character.

Multiplying **y** with **D**, will give back the original **x** matrix.

Lets do this exercise in Python.

```python
import numpy as np

E = np.array([[9,3],[2,1]]) # encryption matrix
D = np.linalg.inv(E) # decryption matrix
x = np.array([[ord('h'), ord('e'), ord('l'), ord('l'), ord('o'), ord(' ')],
[ord('w'), ord('o'),ord('r'), ord('l'), ord('d'), 0]])
# "hello world" converted to unicode
y = np.matmul(E,x) # encryption
q = np.matmul(D,y) # decryption

print(q) # output q

'''
This outputs:

[[1.04000000e+02 1.01000000e+02 1.08000000e+02 1.08000000e+02
  1.11000000e+02 3.20000000e+01]
 [1.19000000e+02 1.11000000e+02 1.14000000e+02 1.08000000e+02
  1.00000000e+02 2.84217094e-14]]
'''
```

You should notice that the output matrix **q** matches the original matrix **x**. Since the decryption matrix has decimals in it, the output will be generated as floating point values as opposed to integers. If you notice, the last value is a number on the order of 10<sup>-14</sup> which is effectively 0. In order to convert **q** back to characters, we have to use the `chr` command. Unfortunately, it only accepts integer values, therefore we must cast the elements from floating point to integer. Let's convert element `q[0][0]` as an example, we convert it to an integer by surrounding it with `int` like this: `int(q[0][0])`. There is a problem here however, because if you print `q[0][0]` you will get the value `103.99999997` which is effectively `104` but if you cast it directly, Python will truncate the decimal part and incorrectly return `103`. To fix this, we simply round the value to the nearest whole number before we convert it. This is done by using `round`. Combining everything to recover a character, we get this rather long line of code: `chr(int(round(q[0][0])))`. Let's extend the code above to convert all the numbers in **q** back to the original characters and place them in a list for printing.


```python
import numpy as np

E = np.array([[9,3],[2,1]]) # encryption matrix
D = np.linalg.inv(E) # decryption matrix
x = np.array([[ord('h'), ord('e'), ord('l'), ord('l'), ord('o'), ord(' ')],
[ord('w'), ord('o'),ord('r'), ord('l'), ord('d'), 0]])
# "hello world" converted to unicode
y = np.matmul(E,x) # encryption
q = np.matmul(D,y) # decryption

print(q) # output q

'''
This outputs:

[[1.04000000e+02 1.01000000e+02 1.08000000e+02 1.08000000e+02
  1.11000000e+02 3.20000000e+01]
 [1.19000000e+02 1.11000000e+02 1.14000000e+02 1.08000000e+02
  1.00000000e+02 2.84217094e-14]]
'''


l = []

for i in range(0, 2):
    for j in range (0, 6):
        if(round(q[i][j]) == 0): # do not include padded zeros
            break
        l.append(chr(int(round(q[i][j]))))
print(l)

'''
This outputs:

['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
'''
```

Here we conclude a basic example on how matrices can be used to encrypt and decrypt data.


## Exercises

1: Add the following two matrices **A** and **B** and multiply the result by three. Print your results.

```python
import numpy as np

A = np.array([[3,7],[1,8]])
B = np.array([[4,5],[9,2]])

# Add the two matrices and then multiply by three.
# Print your results.
```

2: Given the following system of equations:

> 3w + 2x + y + 4z = 66  
> w + 4x + 2y + 3z = 72  
> 4w + x + 5y + z = 89  
w + x + y + z = 29

Complete the following Python script to solve the system of equations for *[w, x, y, z]* and print your results.

```python
import numpy as np

# Solve system of linear equations here...
```

3: A string *x* has been encrypted using the following key:

![Encryption Key](https://raw.githubusercontent.com/HishamT/Intro-to-Matrix-Algebra/main/Q2Encryption_Key.png "Encryption Key")

The following encrypted string of random characters was generated:

```python
['ҿ', 'Ө', 'ѷ', 'Ӟ', 'Ͳ', 'Α', '̀', 'Ί']
```

Complete the following Python script to decrypt it and print your results.

```python
import numpy as np
# Use this list when converting the encrypted characters to unicode.
s = ['ҿ', 'Ө', 'ѷ', 'Ӟ', 'Ͳ', 'Α', '̀', 'Ί'] # DO NOT copy and paste the characters.

# Decrypt the string here...
```