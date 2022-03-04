class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0 for _ in range(query_glass + 2)] for row in range(query_row + 1)]
        glasses[0][0] = poured
        
        for i in range(query_row):
            for j in range(query_glass+1):
                to_spil = max(0, glasses[i][j] - 1)
                glasses[i+1][j] += to_spil / 2
                glasses[i+1][j+1] += to_spil / 2
        
        return min(1, glasses[query_row][query_glass])

