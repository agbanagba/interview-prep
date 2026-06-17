# Output winner (A or B), "Draw" or pending

# A winner is one that have all moves either horizontally, vertically or diagonally
# A pending result is when we don't have enough moves to guarantee a win and that is
from collections import Counter


def winner(moves):
    if len(moves) < 4:
        return "Pending"

    def won(player_moves):
        if len(player_moves) < 3:
            return False

        # check for horizontal win. We can get a complete board and check if at least 3 values at move[i] corresponds
        hz_moves = Counter([move[0] for move in player_moves])
        hz = max(list(hz_moves.values())) == 3

        # check for vertical win
        vert_moves = Counter([move[1] for move in player_moves])
        vert = max(list(vert_moves.values())) == 3

        # check for diagonal win
        diag = [1, 1] in player_moves and (([0, 0] in player_moves and [2, 2] in player_moves) or (
                    [0, 2] in player_moves and [2, 0] in player_moves))
        return hz or vert or diag

    # Check if A won then check if B won
    if won(moves[0:len(moves):2]):
        return 'A'
    elif won(moves[1:len(moves):2]):
        return 'B'

    return "Draw" if len(moves) == 9 else "Pending"


if __name__ == '__main__':
    mvs = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    mvs2 = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
    mvs3 = [[0, 0], [1, 2], [0, 2], [1, 1]]
    mvs4 = [[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]]
    print(winner(mvs4))
