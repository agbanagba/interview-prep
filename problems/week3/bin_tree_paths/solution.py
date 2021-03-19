class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root):
    if not root:
        return []

    paths = []

    def helper(node, prev_path):
        if not (node.right or node.left):
            paths.append(f'{prev_path}{node.val}')
            return

        # Build path
        path = f"{node.val}->" if prev_path == "" else f"{prev_path}{node.val}->"
        if node.right:
            helper(node.right, path)

        if node.left:
            helper(node.left, path)

    helper(root, "")
    return paths


if __name__ == '__main__':
    root_node = TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3))
    print(binary_tree_paths(root_node))
