Search a 2D m x n sorted matrix. The matrix has the following properties. a. Integers in each row are sorted from left
to right b. The first integer of each row is greater than the last integer of the previous row.

Questions:

1. Really don't have any questions.

Naive Approach:
Linear search through n and m looking for a target.

Time Complexity - O(nm)
Space Complexity - O(1)

Efficient Approach:
Binary search with a twist. Modelling the 2D matrix into a 1D array, a binary search can easily be used to solve this
problem.  
The length of the 1D array will be n*m, and we can resolve and index k into i and j values of the 2D array where

        i = k // len(matrix[0])
        j = k % len(matrix[0])

Time Complexity - O(logr) where r=n * m   
Space Complexity - O(1)

