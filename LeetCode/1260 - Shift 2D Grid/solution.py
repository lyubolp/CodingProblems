class Solution:
    def shift_position(self, current: Tuple[int, int], size: Tuple[int, int], k: int) -> Tuple[int, int]:
        x, y = current
        m, n = size
        
        pos_1d = x * n + y
        shifted_1d = (pos_1d + k) % (m * n)
    
        return shifted_1d // n, shifted_1d % n
        
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        result = [[0 for i in range(n)] for j in range(m)]
        k = k % (m * n)
        
        for i in range(m):
            for j in range(n):
                target_i, target_j = self.shift_position((i, j), (m, n), k)
                
                result[target_i][target_j] = grid[i][j]
        
        return result

