class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        sorted_until = 0
        
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                
                nums[sorted_until], nums[i] = nums[i], nums[sorted_until]
                sorted_until += 1
        nums[sorted_until], nums[-1] = nums[-1], nums[sorted_until]
        return sorted_until + 1
        
