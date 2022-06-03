class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.sums = [reduce(lambda acc, item: acc + [acc[-1] + item], row, [0])[1:] for row in matrix]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(self.sums[i][col2] - (self.sums[i][col1 - 1] if col1 != 0 else 0) for i in range(row1, row2 + 1))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

