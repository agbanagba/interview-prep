class Node(object):

    def __init__(self, val, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


def deep_copy(root):
    def traverse(node):
        if not node:
            return node

        if node in visited:
            return visited[node]

        new_node = Node(node.val)
        visited[node] = new_node

        new_node.left = traverse(node.left)
        new_node.right = traverse(node.right)
        new_node.random = traverse(node.random)

        return new_node

    visited = {}
    n = traverse(root)
    return n


if __name__ == '__main__':
    seven_node = Node(7)
    right_node = Node(4, left=seven_node, random=seven_node)
    rt = Node(1, right=right_node)
    seven_node.random = rt
    print(deep_copy(rt))
