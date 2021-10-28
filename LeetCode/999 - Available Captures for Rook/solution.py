class Solution:
    def find_rook(self, board: List[List[str]]) -> (int, int):
        for i, row in enumerate(board):
            for j, figure in enumerate(row):
                if figure == "R":
                    return i, j
        
        # for completeness 
        return -1, -1
    def discover(self, board: List[List[str]], current_position: (int, int), direction: int) -> bool:
        # 0 - up
        # 1 - down
        # 2 - left
        # 3 - right
        i, j = current_position
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        elif board[i][j] == 'p':
            return True
        elif board[i][j] == 'B':
            return False
        else:
            next_i = i
            next_j = j
            
            if direction == 0:
                next_i -= 1
            elif direction == 1:
                next_i += 1
            elif direction == 2:
                next_j -= 1
            else:
                next_j += 1
            
            return self.discover(board, (next_i, next_j), direction)
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_x, rook_y = self.find_rook(board)
        
        result = [
            self.discover(board, (rook_x, rook_y), 0),
            self.discover(board, (rook_x, rook_y), 1),
            self.discover(board, (rook_x, rook_y), 2),
            self.discover(board, (rook_x, rook_y), 3)
        ]
        
        return len([r for r in result if r is True])

