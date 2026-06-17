Given the root of a binary tree, return the vertical order traversal
of its node values (level by level, left to right)

Question/Clarifications
There are really no questions here for me to ask. It's quite straightforward


Approach:

A recursive or an iterative approach here will work. All that needs to be done
is to keep track of the level we are on, so we can append that value

We use a BFS approach here to traverse the array and keep track of the level.

Time Complexity - O(n) as we touch all elements in the array
Space Complexity - O(n) - we keep a levels array