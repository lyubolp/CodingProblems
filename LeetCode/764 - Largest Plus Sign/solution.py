from typing import List, Tuple
from copy import deepcopy
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        matrix = [[1 for i in range(n)] for j in range(n)]

        for mine in mines:
            matrix[mine[0]][mine[1]] = 0

        left = deepcopy(matrix)
        right = deepcopy(matrix)
        top = deepcopy(matrix)
        bottom = deepcopy(matrix)

        for i in range(n):
            for j in range(n):
                if i > 0 and top[i][j] != 0:
                    top[i][j] += top[i-1][j]
                if j > 0 and left[i][j] != 0:
                    left[i][j] += left[i][j-1]

                x = n - i - 1
                y = n - j - 1
                if x < n - 1 and bottom[x][y] != 0:
                    bottom[x][y] += bottom[x+1][y]
                if y < n - 1 and right[x][y] != 0:
                    right[x][y] += right[x][y+1]

        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, min(top[i][j], left[i][j], right[i][j], bottom[i][j]))
        return result

if __name__ == "__main__":
    s = Solution()
    n = 5
    mines = [[4, 2]]
    # n = 1
    # mines = [[0, 0]]
    print(s.orderOfLargestPlusSign(n, mines))
    # print(s.is_plus_valid([1, 1], mines, 1, 3))
    