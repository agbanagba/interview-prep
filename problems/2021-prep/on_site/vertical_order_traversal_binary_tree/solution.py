class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root):
    if not root:
        return []

    queue = [(root, 0, 0)]
    levels = {}

    vert_min, vert_max = 0, 0

    while queue:
        # col is represents level here
        node, row, col = queue.pop(0)

        if node:
            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))

            vert_min = min(vert_min, col)
            vert_max = max(vert_max, col)

            if col in levels:
                levels[col].append((node.val, row))
            else:
                levels[col] = [(node.val, row)]

    # This step will be O(n).
    result = []
    for idx in range(vert_min, vert_max + 1):
        level = sorted(levels[idx], key=lambda x: (x[1], x[0]))
        result.append([item[0] for item in level])

    return result


if __name__ == '__main__':
    rt = TreeNode(3, left=TreeNode(1, left=TreeNode(0), right=TreeNode(4)), right=TreeNode(4, left=(TreeNode(2))))
    print(vertical_traversal(rt))
