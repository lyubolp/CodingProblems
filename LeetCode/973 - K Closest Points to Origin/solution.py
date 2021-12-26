class Solution:
    def calculate_distance(self, point: List[int]) -> float:
        return sqrt(point[0] ** 2 + point[1] ** 2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: self.calculate_distance(p))    
        return points[:k]

