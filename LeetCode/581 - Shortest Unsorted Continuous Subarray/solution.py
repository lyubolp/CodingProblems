class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_index = 0
        max_index = len(nums) - 1
        
        
        while min_index < len(nums) - 1:
            
            if nums[min_index] <= min(nums[min_index + 1:]):
                min_index += 1
            else:
                break
                
        while max_index > 0:
            if nums[max_index] >= max(nums[:max_index]):
                max_index -= 1
            else:
                break
    
        return max_index - min_index + 1 if max_index > min_index else 0

