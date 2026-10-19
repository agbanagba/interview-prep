

class Connect6:

    def __init__(self, k:int) -> None:
        
        # Black 0
        # White 1
        # White 2
        # Black 3
        # Black 4
        # White 5
        # White 6
        # Black 7
        
        self.black_set = set()
        self.white_set = set()
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]


    def getTurn(self) -> str:
        total_length = len(self.black_set) + len(self.white_set)
        total_round = total_length % 4
        if total_round == 0 or total_round == 3:
            return "black"
        else:
            return "white"
        
    def placeBlack(self, x, y):
        self.black_set.add((x, y))
        return self.checkWin(x, y, self.black_set)
    
    def placeWhite(self, x, y):
        self.white_set.add((x, y))
        return self.checkWin(x, y, self.white_set)
        

    def checkWin(self, x: int, y:int, player_set: set):
        current_x = x
        current_y = y
        for i, j in self.directions:
            current_x = x + i
            current_y = y + j
            for iteration in range(5):
                if (current_x, current_y) not in player_set:
                    break
                elif (current_x, current_y) in player_set and iteration == 4:
                    return True
                
                current_x = current_x + i
                current_y = current_y + j
                
        return False
    


class Connect6CorrectWinCode:

    def __init__(self, k:int) -> None:
        
        # Black 0
        # White 1
        # White 2
        # Black 3
        # Black 4
        # White 5
        # White 6
        # Black 7
        
        self.black_set = set()
        self.white_set = set()
        self.axes = [
            [(0, 1), (0, -1)],
            [(1, 0), (-1, 0)],
            [(-1, 1), (1, -1)],
            [(-1, -1), (1, 1)]
        ]

    # O(1)
    def getTurn(self) -> str:
        total_length = len(self.black_set) + len(self.white_set)
        total_round = total_length % 4
        if total_round == 0 or total_round == 3:
            return "black"
        else:
            return "white"
        
    def placeBlack(self, x, y):
        self.black_set.add((x, y))
        return self.checkWin(x, y, self.black_set)
    
    def placeWhite(self, x, y):
        self.white_set.add((x, y))
        return self.checkWin(x, y, self.white_set)
    
    # O(1)
    # O(n) for connect n
    def checkWin(self, x: int, y: int, player_set: set) -> bool:
        for d1, d2 in self.axes:

            count = 1
            for dx, dy in (d1, d2):
                current_x = x + dx
                current_y = y + dy

                steps = 0
                # steps < 5 will be steps < n - 1 for connect n
                while (current_x, current_y) in player_set and steps < 5:
                    count += 1
                    steps += 1
                    current_x += dx
                    current_y += dy

            # This will be count >=n for connect n
            if count >= 6:
                return True
            
        return False
    
