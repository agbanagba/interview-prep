Balanced binary tree is one in which the difference in height of the left and right **subtrees** of **every node** differs in height by no
more than 1

Input - root node of a tree\
Output - boolean indicating balanced or not

Clarifications & Edge Cases

1. Empty trees are balanced
2. Root node as only node is balanced

Approach: 
Calculate the height of left node and right node of a node and, the diff should not be more
than 1.
We can recursively calculate the height of a node by recursively going to the leaf and 
adding 1 as we come back up the recursive stack.
We need to do this for **every node** and not just the root node because a Binary tree is balanced 
only when all nodes are balanced.

pseudocode:
    
    height(node):
        if not is null;
            return -1 
        
        return maximum(height(left node), height(right node)) + 1
        
    balanced(node):

        if node is null:
            node is balanced, return true

        absolute(height(left node) - height(right node)) <= 1 and balanced(left node)\
            and balanced(right node)

        
    