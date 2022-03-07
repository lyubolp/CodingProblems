class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        
        result = max(nums) - min(nums)
        for i in range(len(nums)):
            for j in range(i+k-1, len(nums)):
                current = abs(nums[i] - nums[j])
                result = min(result, current)
        
        return result

