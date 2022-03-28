class Solution:
    def search_rec(self, nums: List[int], target: int, start: int, end: int) -> bool:
        if end <= start:
            return nums[start] == target

        mid = (end - start) // 2 + start
        
        if nums[mid] < target:
            return self.search_rec(nums, target, mid + 1, end)
        elif nums[mid] > target:
            return self.search_rec(nums, target, start, mid - 1)
        else:
            return True
        
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return target == nums[0]
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                first = nums[:i+1]
                second = nums[i+1:]
                
                return self.search_rec(first, target, 0, len(first) - 1) or self.search_rec(second, target, 0, len(second) - 1)
        
        return target in nums

