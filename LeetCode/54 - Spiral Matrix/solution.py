from typing import List
class Solution:
    def is_move_out_of_bounds(self, i: int, j: int, matrix: List[List[int]]) -> bool:
        return i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0])
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        
        direction = 0 # 0 - right, 1 - down, 2 - left, 3 - up
        directions = {
            0: [0, 1], 
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0]
        }
        visited = {(i, j): 1}
        result = [matrix[i][j]]
        for moves in range(len(matrix) * len(matrix[0]) - 1):
            next_i = i
            next_j = j
            
            next_i += directions[direction][0]
            next_j += directions[direction][1]
            
            if self.is_move_out_of_bounds(next_i, next_j, matrix) or (next_i, next_j) in visited:
                direction += 1
                direction %= 4
                i += directions[direction][0]
                j += directions[direction][1]
            else:
                i = next_i
                j = next_j

            visited[(i, j)] = 1
            result.append(matrix[i][j])
        return result
if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    print(s.spiralOrder(matrix))