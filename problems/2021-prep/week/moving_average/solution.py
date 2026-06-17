class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.vals = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.vals) == self.size:
            self.vals.pop(0)

        self.vals.append(val)
        return sum(self.vals) / len(self.vals)


if __name__ == '__main__':
    obj = MovingAverage(3)
    print(obj.next(1))
    print(obj.next(10))
    print(obj.next(3))
    print(obj.next(5))
