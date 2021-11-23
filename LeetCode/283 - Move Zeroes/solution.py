class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        free_space = 0
        
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[free_space] = nums[free_space], nums[i]
                free_space += 1

