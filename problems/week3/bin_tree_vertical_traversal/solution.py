class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_vertical(root):
    if not root:
        return []

    queue = [(root, 0)]
    levels = {}

    while queue:

        node, level = queue.pop(0)

        if node:
            queue.append((node.left, level - 1))
            queue.append((node.right, level + 1))

            if level in levels:
                levels[level].append(node.val)
            else:
                levels[level] = [node.val]

    # since we are sorting the key here, it will add O(nlogn) to the running time
    return [levels[idx] for idx in sorted(levels.keys())]


if __name__ == '__main__':
    zero_node = TreeNode(0, right=TreeNode(2), left=TreeNode(5))
    root = TreeNode(3, left=TreeNode(9, left=TreeNode(4), right=zero_node),
                    right=TreeNode(8, left=TreeNode(1), right=TreeNode(7)))
    print(traverse_vertical(root))
