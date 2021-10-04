class Solution:
    def is_square_in(self, x: int, y: int, grid: List[List[int]]) -> bool:
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def get_perimeter_square(self, grid: List[List[int]], x: int, y: int) -> int:
        positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        land_squares = 0
        for add_x, add_y, in positions:
            new_x = x + add_x
            new_y = y + add_y
            
            if self.is_square_in(new_x, new_y, grid) and grid[new_x][new_y] == 1:
                land_squares += 1
        
        return 4 - land_squares
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result += self.get_perimeter_square(grid, i, j)  
        return result

