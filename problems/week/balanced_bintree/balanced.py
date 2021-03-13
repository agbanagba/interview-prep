class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanced(root):
    if not root:
        return True

    return abs(height(root.left) - height(root.right)) <= 1 and balanced(root.left) and balanced(root.right)


def height(node):
    if not node:
        return -1

    return max(height(node.left), height(node.right)) + 1


if __name__ == '__main__':
    rt = TreeNode(1, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print(balanced(rt))
