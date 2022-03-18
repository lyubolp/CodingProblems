class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        
        start_row, end_row = ord(start[0]), ord(end[0])
        start_column, end_column = int(start[1]), int(end[1])
        
        rows = end_row - start_row + 1
        columns = end_column - start_column + 1
        
        result = [chr(start_row + row_offset) + str(start_column + column_offset) for row_offset in range(rows) for column_offset in range(columns) ]
        
        return result

