Given the root of a binary tree, return the vertical order traversal 
of its node values

A vertical order traversal is to get values on the same vertical 
column.


Approach:
We are traversing the tree based on levels but quite different from a typical
horizontal normal level traversal. In the horizontal/normal level traversal,
we keep track of a level. That's also the case here with a twist in that the root element is at level 0
and the right element of a node is `node_level + 1` and left element is `node_level - 1`

Using a BFS approach to traverse and keep track, we'll end up with a running
time of O(n) and after sorting our final values (because it will not be in asc order),
we'll end up with O(nlogn)

Time Complexity - O(nlogn)
Space Complexity - O(n)