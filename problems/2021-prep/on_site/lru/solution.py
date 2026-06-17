import math


class Node(object):

    def __init__(self, key=math.inf, value=math.inf, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        self.map = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove_node(node)
        self.add_node(node)
        return node.value

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove_node(node)
            self.add_node(node)
        else:
            if len(self.map) >= self.capacity:
                tail = self.pop_tail()
                self.map.pop(tail.key)

            node = Node(key, value)
            self.map[key] = node
            self.add_node(node)

    def pop_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 0)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))  # expecting -1 here
    cache.put(4, 4)
