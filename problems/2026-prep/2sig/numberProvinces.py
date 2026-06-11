
from typing import List
from collections import deque

def findCircleNum(isConnected: List[List[int]]) -> int:
    
    n = len(isConnected)
    visited = set()
    provinces = 0

    # The State Engine: A Queue instead of Recursion
    def bfs(start_city):
        queue = deque([start_city])
        
        # CRITICAL: Always mark visited the second it goes into the queue!
        visited.add(start_city) 

        while queue:
            current_city = queue.popleft()

            # The Menu: Read my row from left to right (0 to N-1)
            for next_city in range(n):
                
                # Bouncer 1 & 2: Are we connected? And is it unvisited?
                if isConnected[current_city][next_city] == 1 and next_city not in visited:
                    # CHOOSE & EXPLORE
                    visited.add(next_city)
                    queue.append(next_city)

    # The Main Loop (Exactly the same)
    for city in range(n):
        if city not in visited:
            provinces += 1
            bfs(city)

    return provinces