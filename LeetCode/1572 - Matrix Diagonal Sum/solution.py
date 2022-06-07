class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = sum([row[i] + row[-i-1] for i, row in enumerate(mat)])
        
        if len(mat) % 2 != 0:
            result -= mat[len(mat) // 2][len(mat) // 2]
        
        return result

