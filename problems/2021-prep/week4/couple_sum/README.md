Given an array of integers, find two numbers such that they sum up to a specific 
target. Solution should return the indices and indices are not zero based

e.g., [2, 3, 4, 7]  
   Output = [2, 3]


Questions:
1. Are the numbers in the array non-negative integers?
2. Are there multiple pairs of numbers that equal the target?
3. What do we return if we don't find a pair matching our criteria? Here we will return [0, 0] since we are using a 
   non-zero index

Approach:
First approach that comes to mind is to try every combination of 
nums in indices i and j. We take i and walk to the end adding i to i + 1, i + 2 ... n
where i < len(input).

Time Complexity - O(n^2) (We are not necessarily visiting all the elements twice but it's obvious that the runtime is 
tending towards O(n^2))
Space Complexity - O(1)

Efficient Solution:
We can throw a data structure at the problem specifically a hash map.
Go to each value in the array, get the diff from the target, if that diff
exists in the hash map, then we have found both values, and we can return both non-zero indices
else we put the value with its index into the hashmap.

Time Complexity - O(n)
Space Complexity - O(n)