from typing import List
class Solution:
    def has_player_won(self, moves: List[List[int]]) -> bool:
        # [[0, 0], [1, 1], [2, 2]]

        # Rows
        for row in range(3):
            current_row_moves = [move[0] for move in moves if move[0] == row]
            if len(current_row_moves) == 3:
                return True

        # Columns
        for column in range(3):
            current_column_moves = [move[1] for move in moves if move[1] == column]
            if len(current_column_moves) == 3:
                return True

        
        left_diagonal_moves = [move[0] for move in moves if move[0] == move[1]]
        if len(left_diagonal_moves) == 3:
            return True
        
        # Right diagonal
        right_diagonal_match = {
            0: 2,
            1: 1,
            2: 0
        }
        right_diagonal_moves = [move[0] for move in moves if move[1] == right_diagonal_match[move[0]]]
        if len(right_diagonal_moves) == 3:
            return True

        return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        first_player_moves = [moves[i] for i in range(len(moves)) if i % 2 == 0]
        second_player_moves = [moves[i] for i in range(len(moves)) if i % 2 != 0]

        first_player_win = self.has_player_won(first_player_moves)
        second_player_win = self.has_player_won(second_player_moves)

        if first_player_win:
            return 'A'
        elif second_player_win:
            return 'B'
        else:
            if len(moves) == 9:
                return 'Draw'
            else:
                return 'Pending'

if __name__ == "__main__":
    s = Solution()
    moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    print(s.tictactoe(moves))