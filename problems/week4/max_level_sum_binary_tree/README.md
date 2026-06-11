Given the root of a binary tree, the level of it's root is 1, the level of it's
children is 2 and so on.  Return the smallest level x such that the sum 
of all values of nodes at level x is maximal.

Questions:
1. What is the range of possible values in a node? This is to figure out if we have -ve values.
2. If all levels have the same value, which should we return?
3. if the tree is empty, what should we return?


Recursive Approach:


Iterative Approach (BFS):
