import collections


class TreeNode(object):

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


# target is also a TreeNode object
# I can store the parent node in the tree node
def distance_k(root, target, k):
    def dfs(node, parent=None):
        if node:
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)
    queue = collections.deque([(target, 0)])
    seen = {target}

    while queue:
        if queue[0][1] == k:
            return [node.val for node, d in queue]
        node, dist = queue.popleft()
        for n in (node.left, node.right, node.parent):
            if n and n not in seen:
                seen.add(n)
                queue.append((n, dist + 1))

    return []


if __name__ == '__main__':
    two_node = TreeNode(2, left=TreeNode(7), right=TreeNode(4))
    target = TreeNode(5, left=TreeNode(6), right=two_node)

    rt = TreeNode(3, left=target, right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)))

    print(distance_k(rt, target, 2))
