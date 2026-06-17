Given an array of integers sorted in ascending order. Find the starting and ending position of a given target value. If
the target is not found return [-1, -1]

Clarifications/Questions

1. Are we guaranteed to have two instances of the target? What if just one instance is found, what do we return? I'm
   assuming that two instances of the target will be present.

Input = array of integers sorted in ascending order e,g., [1, 2, 3,3, 9, 15]
Output = positions of start and end or [-1, -1] if not present

Linear Approach:
We can use the good old fashioned linear search to look for the element.
If we find one, the next one is the next element in the array because the array is sorted.

Time Complexity - O(n)
Space Complexity - O(1)

Binary search approach:
Binary search can also work here to look for the target value. When we find the target value, 
the next target value position is either to the left or to the left because we are guaranteed that two 
instances of target will be present.

I'll be using the iterative approach here, so I can easily identify position

Time Complexity - O(logn)
Space Complexity - O(1)