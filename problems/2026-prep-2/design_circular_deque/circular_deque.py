

class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class CircularDequeLinkedList:

    def __init__(self, k: int):

        self.capacity = k
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        pass

    def insertLast(self, value: int) -> bool:
        pass

    def deleteFront(self) -> bool:
        pass

    def deleteLast(self) -> bool:
        pass

    def getFront(self) -> int:
        pass

    def getRear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass


class CircularDequeArray:

    def __init__(self, k: int):

        self.capacity = k
        self.queue = [0] * k
        self.size = 0

        # front index point to the index of the first element
        self.front = 0
        self.rear = k - 1


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        self.queue[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity