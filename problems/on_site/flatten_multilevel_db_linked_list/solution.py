

class Node(object):

    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head):
    if not head:
        return None

    node = head

    while node:

        if node.child:

            # get the last node in the childs db linked list and set the next to tmp_node
            last_node = node.child
            while last_node.next:
                last_node = last_node.next

            if node.next:
                node.next.prev = last_node
            last_node.next = node.next

            node.child.prev = node
            node.next = node.child

            node.child = None

        node = node.next

    return head


def flatten_dfs(head):
    if not head:
        return head

    # basically if node has a child
    stack = [hd]
    while stack:
        node = stack.pop()


if __name__ == '__main__':
    hd, two, three, four, five, six = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)
    seven, eight, nine, ten = Node(7), Node(8), Node(9), Node(10)
    eleven, twelve = Node(11), Node(12)
    hd.next = two
    two.prev = hd

    three.prev = two
    two.next = three
    three.next = four
    three.child = seven

    four.prev = three
    four.next = five
    five.prev = four
    five.next = six
    six.prev = five

    seven.next = eight
    eight.prev = seven
    eight.next = nine
    eight.child = eleven
    nine.prev = eight
    nine.next = ten
    ten.prev = nine

    eleven.next = twelve
    twelve.prev = eleven

    flatten(hd)

    hd = Node(1, child=Node(2, child=Node(3)))
    flatten(hd)
    while hd:
        print(hd.val)
        hd = hd.next
