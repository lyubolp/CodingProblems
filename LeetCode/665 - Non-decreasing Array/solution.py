class Solution:
    def is_array_non_decreasing(self, nums: List[int]) -> bool: 
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
            
        return True
    def checkPossibility(self, nums: List[int]) -> bool:
        # [5, 6, 10, 7, 8, 10]
        
        for i in range(len(nums)):
            if self.is_array_non_decreasing(nums[:i] + nums[i+1:]):
                return True
        
        return False

