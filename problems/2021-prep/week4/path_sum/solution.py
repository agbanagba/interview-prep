class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum_1(root, target_sum):

    def helper(node, curr_sum):
        if not node:
            return
        curr_sum -= node.val
        if not node.left and not node.right:
            return curr_sum == 0
        return helper(node.left, curr_sum) or helper(node.right, curr_sum)

    return helper(root, target_sum) is True


def path_sum(root, target_sum):
    def helper(node, curr_sum):
        if not node:
            return

        new_sum = curr_sum + node.val
        if not (node.left or node.right):
            # This should only happen on a leaf node
            if new_sum == target_sum:
                return True

        return helper(node.left, new_sum) or helper(node.right, new_sum)

    return helper(root, 0) is True


if __name__ == '__main__':
    eigth_node = TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1)))
    four_right = TreeNode(5, left=TreeNode(12), right=TreeNode(11))
    four_node = TreeNode(4, left=TreeNode(11, left=TreeNode(11), right=TreeNode(2)), right=four_right)
    rt = TreeNode(5, left=four_node, right=eigth_node)

    second_rt = TreeNode(1, left=TreeNode(2))
    print(path_sum_1(second_rt, 1))
