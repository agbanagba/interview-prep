Find peak element in a 1D array

Input = array of integers  
Output = position/index of peak

Clarifications:
1. What's the definition of a peak. e.g., if we have [a, b, c], b is a peak if b>= a and b>=c.
2. Is the array sorted and in what order. \
   -> sorted: last element in array is a peak\
   <- sorted: first element in array is a peak
   
3. Are there multiple or a single peak element in the array. I'm working with the fact that there can be multiple peaks

Approach 1:
Do a linear search and check for if item at any index obeys peak definition

Time Complexity - O(n)\
Space Complexity - O(1)

Approach 2:
Do a binary search. If the value at mid+1 > mid, then a peak will exist on the right side
and similarly if mid-1 > mid, then a peak will exist on the left side.

Note: Like a typical binary search, for small values of n in the array, it's 
not necessary but oh well. Just stating sha

Time Complexity - O(logn)
Space Complexity - O(1) using iterative approach with bin search