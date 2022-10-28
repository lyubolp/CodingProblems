class Solution:
    def calculate_hourglass(self, grid: List[List[int]], start_i: int, start_j: int) -> int:
        first_row = sum(grid[start_i-1][start_j-1:start_j+2])
        second_row = grid[start_i][start_j]
        third_row = sum(grid[start_i+1][start_j-1:start_j+2])
        
        return first_row + second_row + third_row
    
    def maxSum(self, grid: List[List[int]]) -> int:
        return max([max([self.calculate_hourglass(grid, i, j) for j in range(1, len(grid[0]) - 1)]) for i in range(1, len(grid) - 1)])

