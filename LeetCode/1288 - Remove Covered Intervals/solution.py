class Solution:
    def is_interval_covered(self, intervals: List[List[int]], target: int):
        for i, interval in enumerate(intervals):
            if i != target and interval[0] <= intervals[target][0] and intervals[target][1] <= interval[1]:
                return True
        
        return False
                
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        return len([interval for i, interval in enumerate(intervals) if not self.is_interval_covered(intervals, i)])

