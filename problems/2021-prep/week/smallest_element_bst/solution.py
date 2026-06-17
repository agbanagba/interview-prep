class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest_element(root, k):
    if not root:
        return

    def inorder(node):
        # Building a list of values from inorder traversal of the tree
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    return inorder(root)[k - 1]


def kth_smallest_element_v1(root, k):
    if not root:
        return
    nums = [0, 0]
    inorder_v1(root, nums, k)
    return nums[1]


def inorder_v1(node, nums, n):
    """
    This version remembers where we are by tracking two things: where we are in the traversal and
    the kth smallest element in a bst.
    """
    if not node:
        return

    inorder_v1(node.left, nums, n)
    nums[0] += 1
    if nums[0] == n:
        nums[1] = node.val
        return
    inorder_v1(node.right, nums, n)


def kth_smallest_v2(root, k):
    pass


if __name__ == '__main__':
    bst = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    print(kth_smallest_element(bst, 1))
    # print(inorder(bst))
