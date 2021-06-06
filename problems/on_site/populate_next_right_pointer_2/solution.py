class Node(object):

    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    def process_child(child_node, prev_node, leftmost_node):
        if child_node:

            if prev:
                prev.next = child_node
            else:
                leftmost_node = child_node
            prev_node = child_node
        return prev_node, leftmost_node

    if not root:
        return root

    leftmost = root
    while leftmost:
        prev, curr = None, leftmost
        leftmost = None
        while curr:
            prev, leftmost = process_child(curr.left, prev, leftmost)
            prev, leftmost = process_child(curr.right, prev, leftmost)
            curr = curr.next
    return root


if __name__ == '__main__':
    left_rt = Node(2, left=Node(4), right=Node(5))
    right_rt = Node(3, right=Node(7))

    left_rt1 = Node(2, left=Node(4))
    right_rt1 = Node(3, right=Node(7))

    left_rt2 = Node(2, left=Node(4))
    right_rt2 = Node(3)

    left_rt3 = Node(2, right=Node(4, left=Node(5)))
    right_rt3 = Node(3, left=Node(7), right=Node(8))

    left_rt4 = Node(2)
    right_rt4 = Node(3, left=Node(4), right=Node(5))

    left_rt5 = Node(2)
    right_rt5 = None

    left_rt6 = Node(2, left=Node(4, left=Node(7)), right=Node(5))
    right_rt6 = Node(3, right=Node(6, right=Node(8)))

    rt = Node(1, left=left_rt6, right=right_rt6)
    connect(rt)
