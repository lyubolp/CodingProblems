class Solution:
    def intersect_two_intervals(self, first: List[int], second: List[int]) -> List[int]:
        return [max(first[0], second[0]), min(first[1], second[1])]
            
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = [[self.intersect_two_intervals(first, second) for second in secondList if first[1] >= second[0] and second[1] >= first[0]] for first in firstList]
    
        
        return sum(result, [])

