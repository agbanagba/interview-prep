# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
class Node(object):

    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    if not root:
        return root
    # using the bfs approach here

    # This will be O(1) because it does not grow to n. At the end of the run, it would have held
    # n nodes in the tree
    queue = [root]

    while queue:  # running time is O(logn) precisely the height of the tree

        for i, item in enumerate(queue):
            item.next = None if i == len(queue) - 1 else queue[i + 1]

        # populate the queue with the next set of items
        queue = [child for node in queue for child in (node.left, node.right) if child]

    return root


# This solution is epic and brilliant. This is from Leetcode Solution#2
# And also we don't have to second guess the connection 2 at each level because we know the tree is
# balanced
def connect_efficient_space(root):
    if not root:
        return root

    leftmost = root
    while leftmost.left:
        head = leftmost
        while head:
            # connection 1
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root


if __name__ == '__main__':
    left_rt = Node(2, left=Node(4), right=Node(5))
    right_rt = Node(3, left=Node(6), right=Node(7))

    rt = Node(1, left=left_rt, right=right_rt)
    connect(rt)
