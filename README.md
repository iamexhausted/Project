# Program to solve equations

When you start a program, you can see that there are entries where you can input number of rows(number of equations) and columns(number of variables) of matrix(system of equations).
If rows = N and columns = M, matrix will be of size N x M. 

Note: The maximum number of columns is 26.

Note: These entries cannot be empty. The entries should be either integers or decimal numbers (it should contain point instead of comma) and do not contain any other symbols. Also variables will be from 'a' to 'z'.

So, the equations will look like:

#a + #b + ... + #z = #        , where # is a number.
...

Note: The rightmost column always contains numbers after equal sign.

Now, if entries are specified, you can click on "Create Matrix" button to create matrix. It will create a matrix of a specified size. You should input numbers(coefficients) and then click on "Solution" button. It will row reduce the matrix and show solutions of the matrix(equations).

Note: A created matrix will contain entries with real numbers.

After you click on "Create Matrix" button again it will clear all entries(and if new values specified, resize it) and delete rref matrix(second matrix) as well as other things that are below or to the right of it.
