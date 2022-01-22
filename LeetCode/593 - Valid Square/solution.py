class Solution:
    def getDistanceBetweenTwoPoints(self, p1: List[int], p2: List[int]) -> float:
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 and p1 == p3 and p1 == p4:
            return False
        
        points = [p1, p2, p3, p4]
        
        pds = [sorted([self.getDistanceBetweenTwoPoints(source, target) for target in points]) for source in points]
        
        for pd in pds:
            if pd != pds[0]:
                return False
        
        return pds[0][0] == 0 and pds[0][1] == pds[0][2]

