class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_level_sum_recursive(root):
    if not root:
        return -1

    def helper(node, level):

        if not node:
            return

        h_map[level] = h_map.get(level, 0) + node.val
        helper(node.left, level + 1)
        helper(node.right, level + 1)

    h_map = dict()
    helper(root, 1)

    return max(h_map, key=h_map.get)


def max_level_sum_iter(root):
    import math
    if not root:
        return -1

    curr_level = max_level = 1
    curr_sum, max_sum = 0, -math.inf

    queue = [root]

    while queue:
        # Calculate the sum of current level and push children of current level into queue
        curr_sum = sum([node.val for node in queue])
        if curr_sum > max_sum:
            max_sum, max_level = curr_sum, curr_level

        # Replace queue with all children of current level
        queue = [child for node in queue for child in [node.left, node.right] if child]
        curr_level += 1

    return max_level


if __name__ == '__main__':
    # root = TreeNode(1, left=TreeNode(7, left=TreeNode(7), right=TreeNode(-8)), right=TreeNode(0))
    # root = TreeNode(-100, left=TreeNode(-200, left=TreeNode(-20), right=TreeNode(-5)), right=TreeNode(-300, left=TreeNode(-10)))
    # root = TreeNode(1)

    # root = TreeNode(1, left=TreeNode(1, left=TreeNode(7), right=TreeNode(-8)),
    #                 right=TreeNode(0, left=TreeNode(-7), right=TreeNode(9)))
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    print(max_level_sum_iter(root))
