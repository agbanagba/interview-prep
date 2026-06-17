class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def find_bottom_left_value(root):

    level_items = [root]
    queue = [root]
    while queue:
        queue = [child for node in queue for child in [node.left, node.right] if child]
        if queue:
            level_items = queue

    return level_items[0].val


if __name__ == '__main__':
    five_node = TreeNode(5, left=TreeNode(7))
    three_node = TreeNode(3, left=five_node, right=TreeNode(6))
    root_node = TreeNode(1, TreeNode(2, left=TreeNode(4)), three_node)
    print(find_bottom_left_value(TreeNode(1)))
