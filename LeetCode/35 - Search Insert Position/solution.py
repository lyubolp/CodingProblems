class Solution:
    def searchInsertHelper(self, nums: List[int], start: int, end: int, target:int) -> int:
        if start >= end:
            if start < len(nums) and nums[start] >= target:
                return start
            else:
                return start + 1
        
        mid = ((end-start) // 2) + start
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsertHelper(nums, start, mid - 1, target)
        else:
            return self.searchInsertHelper(nums, mid + 1, end, target)
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchInsertHelper(nums, 0, len(nums) - 1, target)
