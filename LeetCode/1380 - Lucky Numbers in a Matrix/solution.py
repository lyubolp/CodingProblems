class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_rows = set([min(row) for row in matrix])
        max_cols = set([max([row[col] for row in matrix]) for col in range(len(matrix[0]))])
        
        return list(min_rows & max_cols)
 
