class Solution:
    def shift_right(self, nums: List[int], i: int):
        for i in range(i, len(nums) - 1):
            nums[i] = nums[i + 1]
            
    def removeDuplicates(self, nums: List[int]) -> int:
        current_number = nums[0]
        current_count = 1
        
        removed = 0
        i = 1
        
        while i < len(nums) - removed:
            if current_number == nums[i]:
                current_count += 1
                
                if current_count > 2:
                    self.shift_right(nums, i)
                    removed += 1
                else:
                    i += 1
            else:
                current_number = nums[i]
                current_count = 1
                
                i += 1
        return len(nums) - removed

