
class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self,capacity: int):

        if capacity <= 0:
            raise ValueError()

        self.capacity = capacity
        self.hash_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _push_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        node = self.hash_map.get(key)
        if node is None:
            return -1

        self._remove(node)
        self._push_front(node)
        return node.val

    def put(self, key, val):
        node = self.hash_map.get(key)
        if node is not None:
            node.val = val
            self._remove(node)
            self._push_front(node)
            return

        if len(self.hash_map) >= self.capacity:
            rm_node = self.tail.prev
            self._remove(rm_node)
            del self.hash_map[rm_node.key]

        # insert new node in map and linked list
        node = Node(key, val)
        self.hash_map[key] = node
        self._push_front(node)