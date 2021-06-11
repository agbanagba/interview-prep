class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    if not root:
        return root
    
    result = []

    # basically, we need to print the rightmost node at every level in the tree
    queue = [root]
    while queue:
        result.append(queue[-1].val)
        queue = [child for node in queue for child in [node.left, node.right] if child]

    return result
