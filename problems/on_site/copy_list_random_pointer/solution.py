class Node(object):

    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


# question for interviewer, does the linked list nodes have unique values
def copy_random_list(head):
    def traverse(hd):
        if not head:
            return head

        if hd in visited:
            return visited[hd]

        node = Node(hd.val, None, None)
        visited[hd] = node

        node.next = traverse(hd.next)
        node.random = traverse(hd.random)
        return node

    visited = {}
    return traverse(head)


def copy_iterative(head):
    if not head:
        return head

    def clone(node):
        if node:
            if node in visited:
                return visited[node]
            else:
                visited[node] = Node(node.val, None, None)
                return visited[node]

    visited = {}
    old_node = head
    new_node = Node(old_node.val, None, None)
    visited[old_node] = new_node

    while old_node:
        new_node.random = clone(old_node.random)
        new_node.next = clone(old_node.next)

        old_node = old_node.next
        new_node = new_node.next

    return visited[head]


if __name__ == '__main__':
    pass
