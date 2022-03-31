class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        
        moves_map = {
            'U': (1, 0),
            'R': (0, 1),
            'D': (-1, 0),
            'L': (0, -1)
        }
        
        for move in moves:
            offset_x, offset_y = moves_map[move]
            x += offset_x
            y += offset_y
        
        return x == 0 and y == 0

