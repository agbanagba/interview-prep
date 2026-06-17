

class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        
        if capacity <= 0:
            raise ValueError()
        
        self.cap = capacity
        self.map = {}
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
        node = self.map.get(key)
        if node is None:
            return -1
        # we just acccessed the node, move to front
        self._remove(node)
        self._push_front(node)
        return node.val

    def put(self, key, val):
        # if node is present in the linkedlist, 
        # update it's value, remove from current position and push to 
        # front
        node = self.map.get(key)
        if node is not None:
            node.val = val
            self._remove(node)
            self._push_front(node)
            return
        
        # if not present, and we've reached capacity, evict node before tail
        if len(self.map) >= self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

        # Then add new entry
        node = Node(key, val)
        self.map[key] = node
        self._push_front(node)
        

# To make this thread safe, we could have a single coarse lock. The problem
# is that every operation serializes on one lock and under high load, 
# the lock becomes the bottleneck.

# A better way is to have several shards for the key space. so we have a 
# sharded LRU that takes a capacity and number of shards. 

class ShardedLRU:
    def __init__(self, capacity, shards=10):
        self.n = shards
        per = max(1, capacity // shards)
        self.shards = [LRUCache(per) for _ in range(shards)]

    def _shard(self, key):
        return self.shards[hash(key) % self.n]
    
    def get(self, key):
        return self._shard(key).get(key)
    
    def put(self, key, val):
        self._shard(key).put(key, val)