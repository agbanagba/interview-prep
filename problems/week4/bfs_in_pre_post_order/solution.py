class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_pre_order(root):
    """ Pre order traversal is visit node, left then right """

    queue = [root]

    while queue:

        node = queue.pop(0)
        if not node:
            continue # TODO check this out later pls.

        # Since i already have the root, I have to put in the left and then right.
        queue.append()

    return queue


def bfs_in_order(root):
    """ Pre order traversal is visit left,node, then right """
    pass


def bfs_post_order(root):
    """ Post order traversal is a visit to left, right then node """
    pass


if __name__ == '__main__':
    pass
