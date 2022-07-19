class Solution:
    def generate_next_row(self, row: List[int]) -> List[int]:
        row = [0] + row + [0]
        return [row[i] + row[i+1] for i in range(len(row) - 1)]
                
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for i in range(numRows - 1):
            result.append(self.generate_next_row(result[-1]))
        
        return result
