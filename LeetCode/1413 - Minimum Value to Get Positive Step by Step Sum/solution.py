class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        needed_start = 1
        for i in range(1, len(nums) + 1):
            
            if needed_start - nums[-i] > 0:
                needed_start -= nums[-i]
            else:
                needed_start = 1
            
        return needed_start

