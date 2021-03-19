class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_level_order(root):
    if not root:
        return []

    queue = [(root, 0)]
    levels = []
    while queue:
        node, level = queue.pop(0)
        if len(levels) == level:
            levels.append([])
        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

        levels[level].append(node.val)

    return levels


if __name__ == '__main__':
    zero_node = TreeNode(0, right=TreeNode(2), left=TreeNode(5))
    root_node = TreeNode(3, left=TreeNode(9, left=TreeNode(4), right=zero_node),
                         right=TreeNode(8, left=TreeNode(1), right=TreeNode(7)))
    print(traverse_level_order(root_node))
