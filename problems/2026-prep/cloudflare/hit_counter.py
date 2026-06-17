from collections import deque

class HitCounter:

    def __init__(self):
        self.queue = deque() # stores [timestamp, count]
        self.total_hits = 0
        

    def hit(self, timestamp: int) -> None:
        # timestamp is increasing so we can check last timestamp
        if not self.queue or self.queue[-1] != timestamp:
            self.queue.append([timestamp, 1])
        else:
            self.q[-1] += 1

        self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0][0] >= 300:
            time, count = self.queue.popleft()
            self.total_hits -= count
        return self.total_hits