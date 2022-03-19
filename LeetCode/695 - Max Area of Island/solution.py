class Solution:
    def bfs(self, matrix, x: int, y: int, visited) -> int:
        result = 0
        
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = [(x, y)]
        while len(queue) > 0:
            current_x, current_y = queue.pop(0)
            
            if (current_x, current_y) in visited:
                continue
            
            if 0 <= current_x < len(matrix) and 0 <= current_y < len(matrix[0]) and matrix[current_x][current_y] == 1:
                visited.add((current_x, current_y))
                result += 1
                for offset_x, offset_y in offsets:
                    next_x, next_j = current_x + offset_x, current_y + offset_y
                    queue.append((next_x, next_j))
                
        
        return result
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    result = max(result, self.bfs(grid, x, y, visited))
        
        return result

