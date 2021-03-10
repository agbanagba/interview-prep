Find the kth smallest element in a bst given an integer n

Tree is a binary search tree.

Input - root node of binary search tree and n  
Output - the kth smallest element

Approach:
We can do an inorder traversal to create a list and get the kth smallest element from the list. After the traversal, the
list will be sorted  
Time Complexity - O(n) we will touch every element in the tree Space Complexity - O(n)

Better Approach:
Taking this a step further. While doing the traversal, if we know where we are, we can return when we find the kth
smallest element.Doing an inorder traversal and at every step know where we are and when we are at the kth smallest
element, we return that value.

Time Complexity - Still O(n) because worst case, we'll touch all nodes \
Space Complexity - Same O(n)

