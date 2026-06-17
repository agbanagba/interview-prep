import threading


class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class ConcurrentHashMap:

    def __init__(self, capacity=128, num_locks=16):
        self.capacity = self.capacity
        self.buckets = [None] * capacity

        self.num_locks = num_locks
        self.locks = [threading.Lock() for _ in range(num_locks)]

    def _get_lock_and_index(self, key):
        # hash and figure out which bucket and which lock this key belongs to.
        bucket_idx = hash(key) % self.capacity
        lock_idx = hash(key) % self.num_locks
        return bucket_idx, self.locks[lock_idx]

    def get(self, key):
        bucket_idx, lock = self._get_lock_and_index(key)
        with lock:
            curr = self.buckets[bucket_idx] # this is the head of the linked list
            while curr:
                if curr.key == key:
                    return curr.value
                curr = curr.next

        return None
    

    def put(self, key, value):
        bucket_idx, lock = self._get_lock_and_index(key)

        with lock:
            head = self.buckets[bucket_idx]
            if head is None:
                self.buckets[bucket_idx] = HashNode(key, value)
                return
            
            curr = head
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                
                if curr.next is None:
                    break
                curr = curr.next

            curr.next = HashNode(key, value)

    def remove(self, key):
        bucket_idx, lock = self._get_lock_and_index(key)
        with lock:
            curr = self.buckets[bucket_idx]
            prev = None

            while curr:
                if curr.key == key:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.buckets[bucket_idx] = curr.next
                    return True
                
                prev = curr
                curr = curr.next

        return False