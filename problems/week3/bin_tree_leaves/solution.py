class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_leaves_naive(root):
    if not root:
        return []

    all_leaves = []
    while root:

        queue = [(root, None, 'none')]
        leaves = []
        while queue:
            # pop a value from the queue
            nnode, parent, bias = queue.pop(0)

            if not nnode:
                continue

            if not (nnode.left or nnode.right):
                leaves.append(nnode.val)
                # dereference that node
                if bias == 'left':
                    parent.left = None
                elif bias == 'right':
                    parent.right = None
                else:
                    root = None
                continue

            queue.append((nnode.left, nnode, 'left'))
            queue.append((nnode.right, nnode, 'right'))

        all_leaves.append(leaves)

    return all_leaves


def find_leaves_eff(root):
    if not root:
        return []

    def helper(node, leaaves):
        if not node:
            return -1

        curr_level = max(helper(node.left, leaaves), helper(node.right, leaaves)) + 1
        if len(leaaves) == curr_level:
            leaaves.append([node.val])
        else:
            leaaves[curr_level].append(node.val)
        return curr_level

    leaves = []
    helper(root, leaves)
    return leaves


if __name__ == '__main__':
    root_node = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
    print(find_leaves_eff(root_node))
