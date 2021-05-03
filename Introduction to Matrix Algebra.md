# **Introduction to Matrix Algebra**

## Introduction

A **matrix** is an ordered collection of numbers that facilities mathematical operations and is used in a number of fields in science, mathematics, and engineering. Common fields in which **matricies** (plural of matrix) and their applications are prevalent are: solving systems of linear equations in electrical, mechanical, and chemical engineering. In control and aerospace engineering, matricies are used to describe the state of a physical system and to study its motion in time and space. In data science, matricies are used to store and manipulate large sets of data. In game development, matricies are used to animate things that change on the players screen. There are of course many more applications but before we begin the study of a matrix, we will first define some terms.

## Matrix

A **matrix** (plural **matricies**) is simply a collection of numbers arranged in rectangular form. A matrix with *m* rows and *n* columns is called an *m-by-n matrix* and can be written as follows:  

![Matrix](m_by_n_Matrix.png "Matrix")

Let's take a *2-by-2* matrix **A** as an example:

![2-by-2 Matrix](A_matrix.png "2-by-2 Matrix")

The number of rows and columns are also known as the **dimensions** of the matrix

When referring to an element inside a matrix (**A**), we denote the element at row *i* and column *j* as *a*<sub>*i*,*j*</sub> 

A *1-by-n matrix* is called a **row vector**:

![Row Vector](row_vector.png "Row Vector")

Similarly, an *m-by-1 matrix* is called a **column vector**:

![Column Vector](column_vector.png "Column Vector")

A matrix where the number of rows equals the number of columns, an *n-by-n matrix*, is called a **square matrix**.

A *1-by-1 matrix* is known as a **scalar** and is simply written as a traditional number and is treated as such.

We will introduce more types of matricies as we need them later in this article.

## Matrix Operations

Now that we have introduced matricies, we will explore the types of operations we can perform on them.

Two matricies are considered **equal** if their corresponding elements are equal.

Matricies have a special operation called a **transpose** in which an element located in row *i* and column *j* is placed at row *j* and column *i*. This operation inverts the dimensions of the matrix. The transpose operation is denoted by placing a **T** as a superscript on the original matrix.  

The transpose of matrix **A** is: 

![Matrix A](matrix_transpose_A.png "Matrix A")  

![A Transpose](matrix_transpose_ATranspose.png "A Transpose")

We can extend the idea of addition to matricies. Two matricies are added together by simply adding the elements of one matrix to the corresponding elements of another matrix.

Let's take the addition of matricies **A** and **B** as an example:  

![Matrix Addition](matrix_addition.png "Matrix Addition")  


It is important to note the following properties for matrix addition:

* Matrix addition is only possible if the dimensions of the matricies are the same. The addition of two matricies of different dimensions is undefined.
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
* Scalar multiplication is also distributive for matricies: *k*(**A** + **B**) = *k***A** + *k***B**

The more complex of the two multiplication operations available is matrix multiplication.
First, a very important rule:
> **The multiplication of the two matricies **A** and **B** is only possible if the column dimension of matrix A is the same as the row dimension of matrix B**. 

This operation will produce a matrix (call it **C**) with the same number of rows as matrix A and the same number of columns as matrix **B**. For example, if matrix **A** is a *m-by-3* matrix, **B** must be a *3-by-n* matrix and this will generate an *m-by-n* matrix. Carrying out the matrix multiplication **C** = **A** **B** is done by the following formula:

![Elements of Matrix Multiplication](matrix_multiplication_elements.png "Elements of Matrix Multiplication")

It is actually easier to see how this works when you consider the following example:

![Matrix Multiplication](matrix_multiplication_symbolic.png "Matrix Multiplication")

Let's do this with some numbers:  

![Matrix Multiplication](matrix_multiplication_numeric.png "Matrix Multiplication")

![Matrix Multiplication](matrix_multiplication_example.png "Matrix Multiplication")

As you can see, matrix multiplication is tedious and impractical to perform manually and such a task is better suited for a computer than a human. Later on in this article we will see how this operation is done in Python using the NumPy library. 

Matrix multiplication has the following properties:
* Matrix multiplication is associative: (**A** **B**) **C** = **A** (**B** **C**)
* Matrix multiplication is distributive: **A**(**B** + **C**) = **A** **B** + **A** **C**
* And most importantly remember that matrix multiplication **IS NOT** commutative!

There exists a special kind of square matrix knows as the **identity matrix**. This is a square matrix that contains ones on the main diagonal and zeros everywhere else. Since an identity matrix is necessarily sqaure (*n-by-n*), we need only one number (*n*) to specify its dimensions. We denote a general identity matrix by **I** and an *n-by-n* identity matrix as **I**<sub>**n**</sub>. It looks like this:

![Identity Matrix](general_id_matrix.png "Identity Matrix")

Multiplication by an identity matrix yields the original matrix and this is one of the few times where matrix multplication is commutative!
* **A** **I** = **I** **A** = **A**

Another special matrix we will consider is the **inverse matrix** of a general matrix **A** denoted as **A**<sup>-1</sup>. This inverse matrix is only defined for square matricies and bears the special property:
* **A** **A**<sup>-1</sup> = **A**<sup>-1</sup> **A** = **I**

However, generating an inverse matrix for **A** is a fairly complex task that merits its own article and consequently is beyond the scope of this introductory lesson on matrix algebra. Often times courses in linear algebra devote one full lecture solely to calculating the inverse of a matrix. As with matrix multiplication, the calculation of an inverse matrix is not practical to be performed by a human and thus the use of a computer is necessary in order to obtain the matrix inverse. We will see how to do this Python later in this article.

## Applications of Matricies: System of Linear Equations

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

We will show the how to use matricies to solve systems of equations later in this article after some properties and techniques are introduced.

This is also just one application of matrix.



















