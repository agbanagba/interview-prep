Given the root of a binary tree, collect a tree's node as follows a. Collect all leaf nodes b. Remove all leaf nodes c.
Repeat until the tree is empty

Question

1. Does a node have a reference to it's parent node.
2. Are all values in the tree unique

Approach:
First thing that comes to mind here is to continuously traverse the tree from root and each time, get all roots and
append to the leaves list and detach the leaf nodes from the tree.

Time Complexity - O(n^2)
Space Complexity - O(n)

Efficient Approach:

We want to be a little clever with a better approach. Using a recursive approach, we can get to the leaf and add 1 as we
come back up with a base case of -1

Time Complexity - O(n)
Space Complexity - O(n)