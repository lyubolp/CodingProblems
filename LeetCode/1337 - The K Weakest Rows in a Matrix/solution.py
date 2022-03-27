class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strength = [(i, sum(row)) for i, row in enumerate(mat)]
        row_strength.sort(key=lambda x: x[1])
        
        return [item[0] for item in row_strength][:k]

