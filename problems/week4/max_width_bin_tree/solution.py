class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_width_iter(root):
    if not root:
        return -1

    max_width = 0
    queue = [(root, 0)]

    while queue:
        _, first_idx = queue[0]
        _, last_idx = queue[-1]

        max_width = max(max_width, last_idx - first_idx + 1)

        # put in next level into queue with indexes
        for _ in range(len(queue)):
            node, idx = queue.pop(0)

            if node.left:
                queue.append((node.left, 2 * idx))

            if node.right:
                queue.append((node.right, 2 * idx + 1))

    return max_width


if __name__ == '__main__':
    # root = TreeNode(1, left=TreeNode(7, left=TreeNode(7), right=TreeNode(-8)), right=TreeNode(0))
    # root = TreeNode(-100, left=TreeNode(-200, left=TreeNode(-20), right=TreeNode(-5)), right=TreeNode(-300, left=TreeNode(-10)))
    # root = TreeNode(1)

    # root = TreeNode(1, left=TreeNode(1, left=TreeNode(7), right=TreeNode(-8)),
    #                 right=TreeNode(0, left=TreeNode(-7), right=TreeNode(9)))
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    print(max_width_iter(root))
