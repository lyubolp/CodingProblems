class Solution:
    def binary_search(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return nums[left]
        
        mid = left + (right - left) // 2
        
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        elif nums[mid] == nums[mid - 1]:
            if mid % 2 == 0:
                # Single number is on the left
                return self.binary_search(nums, left, mid - 2)
            else:
                return self.binary_search(nums, mid + 1, right)
                
        elif nums[mid] == nums[mid + 1]:
            if mid % 2 == 0:
                return self.binary_search(nums, mid + 2, right)
            else:
                return self.binary_search(nums, left, mid - 1)
        
            
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.binary_search(nums, 0, len(nums) - 1)

