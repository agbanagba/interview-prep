import math


class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root, lower=-math.inf, upper=math.inf):
    if not root:
        return True

    if root.val <= lower or root.val >= upper:
        return False

    return is_valid_bst(root.left, lower, root.val) and is_valid_bst(root.right, root.val, upper)


if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(1))
    print(is_valid_bst(root))
