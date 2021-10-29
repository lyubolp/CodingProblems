class Solution:
    def __init__(self):
        self.MAX = 100000
    
    def is_move_valid(self, i: int, j: int, len_i: int, len_j: int) -> bool:
        return 0 <= i < len_i and 0 <= j < len_j
    
    def bfs(self, grid: List[List[int]], result: List[List[int]], start: (int, int)):
        queue = [(start, 0)]
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        
        next_moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        while len(queue) > 0:
            current_pos, day = queue.pop(0)
            i, j = current_pos
            
            if visited[i][j]:
                continue
                
            if grid[i][j] > 0:
                visited[i][j] = True
                result[i][j] = min(result[i][j], day)
                for offset_i, offset_j in next_moves:
                    next_i = i + offset_i
                    next_j = j + offset_j
                    
                    if self.is_move_valid(next_i, next_j, len(grid), len(grid[0])):
                        queue.append(((next_i, next_j), day + 1))
            
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = []
        
        starts = []
        
        for i, row in enumerate(grid):
            current = []
            for j, item in enumerate(row):
                if item == 2:
                    starts.append((i, j))
                    current.append(0)
                elif item == 1:
                    current.append(self.MAX)
                else:
                    current.append(0)
                    
            
            result.append(current)
        
        
        for start in starts:
            self.bfs(grid, result, start)
        
        final_res = max(sum(result, []))
        return final_res if final_res != self.MAX else -1

