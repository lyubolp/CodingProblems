class Solution:
    def manhattan_distance(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_points = [(i, point) for i, point in enumerate(points) if point[0] == x or point[1] == y]
        
        if len(valid_points) == 0:
            return -1
        index_distances = [(i, self.manhattan_distance(x, y, point[0], point[1])) for i, point in valid_points]
        sorted_index_distances = sorted(index_distances, key=lambda x: (x[1], x[0]))
        
        return sorted_index_distances[0][0]

