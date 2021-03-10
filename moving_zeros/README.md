MOVING ZEROS  
Given an array of numbers, write a function to move all 0's to the right of the array
while maintaining the relative other of non-zero elements


Naive Approach:  
a. Create a new array with same length and fill everything with zeros. Iterate the given array and 
fill the new array with the non-zero elements.  
b. Bubble the non-zero elements to the front of the array. This will leave the zeros at the end.

Efficient Approach:
In-place modification of the array using two different pointers.
