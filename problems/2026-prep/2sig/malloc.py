from collections import defaultdict

# Two problems
# 1: LC 2502 - Design Memory Allocator
# 2. From interviewdb. Question is below



# Problem 1 - Design Memory Allocator: LC 2502
# This is the brute force solution. passes but 760ms in LC. 
#  For large calls to allocate and large sizes of n, there becomes a problem.
class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.mem[i] == 0:
                count += 1
                if count == size:
                    start = i - size + 1
                    for j in range(start, i + 1):
                        self.mem[j] = mID
                    return start
            else:
                count = 0
        return -1

    def free(self, mID: int) -> int:
        freed = 0
        for i in range(self.n):
            if self.mem[i] == mID:
                self.mem[i] = 0
                freed += 1
        return freed


# Problem 1 - Version efficient
# The brute force version uses a list and scans the list for slots. 
# we can instead use a set or list of free slots with start and length. Immediately put items in the start 
# then remove from the set. This gives O(logn) per allocate and O(k logn) per free where k is the number of intervals owned by mID
# The problem could also morph into hanling fit policy, handling fragmentation and making it thread sage. 
class Node:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.prev = None
        self.next = None


class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.head = Node(0, n) # Initial is every thing is free
        self.owned = defaultdict(list) #mID -> list of (start, end) allocated intervals


    def allocate(self, size: int, mID: int) -> int:

        # walk the free list looking for the leftmost with enough space
        node = self.head
        while node is not None: # while node will also suffice here
            if node.end - node.start >= size:
                start = node.start
                node.start += size
                
                # if the node is now empty, remove it from the linked list
                if node.start == node.end:
                    self._unlink(node)
                self.owned[mID].append((start, start + size))
                return start
            node = node.next
        return -1
    
    def free(self, mID: int) -> int:
        if mID not in self.owned:
            return 0
        
        intervals = self.owned.pop(mID)
        total_freed = 0
        for start, end in intervals:
            total_freed += end - start
            self._return_to_free(start, end)
        return total_freed


from sortedcontainers import SortedDict

class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.free = SortedDict({0: n}) # sorted dict of (start, end) free intervals
        self.owned = defaultdict(list)

    # O(k) time as we iterate the free dict to find a fit; k = number of free intervals
    def allocate(self, size: int, mID: int) -> int:
        for start, end in self.free.items():
            if end - start >= size:
                del self.free[start]
                if start + size < end:
                    self.free[start + size] = end
                self.owned[mID].append((start, start + size))
                return start
        return -1
    
    # O(mlogk) 
    # Right check is O(logk) because we use binary search because it's a sorted dict. 
    # Left check is O(logk) because bisect left is O(logk) and key lookup is also O(logk)
    # we do this m times where m is intervals owned by mID. 
    def free(self, mID: int) -> int:
        if mID not in self.owned:
            return 0
        
        total_freed = 0
        for start, end in self.owned[mID]:
            total_freed += end - start
            self._return_to_free(start, end)
        del self.owned[mID]

        return total_freed
    
    def _return_to_free(self, start, end):
        # right neighbour: a free interval starting exactly at end

        if end in self.free:
            merged_end = self.free.pop(end)
        else:
            merged_end = end

        # left neighbour: largest free interval with start < s, ending at start
        idx = self.free.bisect_left(start)
        merged_start = start
        if idx > 0:
            left_start = self.free.keys()[idx - 1]
            if self.free[left_start] == start:
                del self.free[left_start]
                merged_start = left_start

        self.free[merged_start] = merged_end

        