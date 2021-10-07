class Solution:
    def __init__(self):
        self.board = []
        
    def is_letter_valid(self, x: int, y: int, current_word_len: int, target_word: str) -> bool:
        return target_word[current_word_len] == self.board[x][y]
    
    def bfs(self, word: str, start_x: int, start_y: int) -> bool:
        stack = [(start_x, start_y, self.board[start_x][start_y], dict())]
        
        next_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while len(stack) > 0:
            x, y, current_word, current_visited = stack.pop()
            
            current_visited[(x, y)] = 1
            
            if current_word == word:
                return True
            
            if len(current_word) > len(word):
                continue
                
            for add_x, add_y in next_moves:
                new_x = x + add_x
                new_y = y + add_y
                if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]) and self.is_letter_valid(new_x, new_y, len(current_word), word) and (new_x, new_y) not in current_visited:
                    stack.append((new_x, new_y, current_word + self.board[new_x][new_y], current_visited.copy()))
        return False
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        
        results = []
        for i, row in enumerate(self.board):
            for j, c in enumerate(row):
                if c == word[0]:
                    results.append(self.bfs(word, i, j))
                    
        return any(results)

