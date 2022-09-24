class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        indexes = [i for i, item in enumerate(nums) if item == target]
        indexes_minus_start = [abs(index - start) for index in indexes]
        
        return min(indexes_minus_start)

