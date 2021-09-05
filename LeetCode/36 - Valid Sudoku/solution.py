from typing import List
class Solution:
    def getBox(self, board: List[List[str]], box: int) -> List[str]:
        row_start = ((box - 1) - ((box - 1) % 3))
        column_start = ((box - 1) % 3) * 3
        return sum([row[column_start:column_start + 3] for row in board[row_start:row_start + 3]], [])
    def isValid(self, items: List[str]) -> bool:
        seen = {}
        
        for item in items:
            if item != "." and item in seen:
                return False
            else:
                seen[item] = 1
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows
        for row in board:
            if not self.isValid(row):
                return False
        
        # Columns
        columns = [[row[i] for row in board] for i in range(9)]

        for column in columns:
            if not self.isValid(column):
                return False
        
        # Boxes
        for i in range(1, 10):
            box = self.getBox(board, i)
            if not self.isValid(box):
                return False
                
        return True
        
if __name__ == "__main__":
    s = Solution()

    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]] 

    print(s.isValidSudoku(board))
