Given the root of a binary tree, return all root-to-leafs paths in **any order**

Questions: None to be honest


Approach:
We are trying to get to the leaf nodes. We keep saving our path until we get to 
the leaf node in which case we add the leaf to the save path from previous calls and return
Using a recursive approach, we can solve this.

Base case: when we get to the leaf node, we append to path and return 

Continuity to base case: we add node path to prev path and call left and right


Time Complexity - O(n)
Space Complexity - O(n)
