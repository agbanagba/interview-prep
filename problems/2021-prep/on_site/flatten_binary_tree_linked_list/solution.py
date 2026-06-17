class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    node = root

    while node:

        if node.left:
            tmp_node = node.right

            # get the rightmost node of node.left and set the right node to tmp_node
            # set the right node of node to the left node.
            rightmost_node = node.left  # rightmost node of node.left
            while rightmost_node.right:
                rightmost_node = rightmost_node.right

            rightmost_node.right = tmp_node
            node.right = node.left
            node.left = None

        # if no left node, we move to the right node
        node = node.right


if __name__ == '__main__':
    two_node = TreeNode(2, left=TreeNode(3), right=TreeNode(4))
    rt = TreeNode(1, left=two_node, right=TreeNode(5, right=TreeNode(6)))

    flatten(rt)

    while rt:
        print(rt.val)
        rt = rt.right
