class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        
        if len(nums) == 1:
            return nums[0]
        
        if all([num < 0 for num in nums]):
            return max(nums)
        
        current_sum = 0
        for num in nums:
            if current_sum + num < 0:
                current_sum = 0
            else:
                current_sum += num
            
            if current_sum > result:
                result = current_sum
                    
        return result

