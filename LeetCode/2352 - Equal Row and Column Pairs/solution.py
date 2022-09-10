class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [row for row in grid]    
        cols = [[row[col] for row in grid] for col in range(len(grid))]
        
        # This is a monstrosity, don't write like this
        return sum((sum((1 for col in cols if row == col)) for row in rows))

