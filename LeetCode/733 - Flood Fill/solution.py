class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        queue = [(sr, sc)]
        
        initial = image[sr][sc]
        visited = {}
        
        next_coordinates = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(queue) > 0:
            i, j = queue.pop(0)
            
            image[i][j] = newColor
            visited[(i, j)] = 1
            
            for next_coordinate in next_coordinates:
                next_i = next_coordinate[0] + i
                next_j = next_coordinate[1] + j
                
                if 0 <= next_i < len(image) and 0 <= next_j < len(image[0]) and (next_i, next_j) not in visited and image[next_i][next_j] == initial:
                    queue.append((next_i, next_j))
            

        return image

