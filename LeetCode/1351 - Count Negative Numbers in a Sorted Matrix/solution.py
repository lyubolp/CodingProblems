class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for row in grid:
            for i, item in enumerate(row):
                if item < 0:
                    result += len(row) - i
                    break
        
        return result

