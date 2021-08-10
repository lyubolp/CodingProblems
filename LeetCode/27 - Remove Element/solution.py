class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        empty_index = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[empty_index] = nums[empty_index], nums[i]
                empty_index += 1
        
        return empty_index

