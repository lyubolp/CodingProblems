class Solution:
    def search_rec(self, nums: List[int], target: int, start: int, end: int):
        if end <= start:
            if nums[start] == target:
                return start
            else:
                return -1
        
        # 2, 3, 4, 5, 6
        mid = (end - start) // 2 + start
        
        if nums[mid] < target:
            return self.search_rec(nums, target, mid + 1, end)
        elif nums[mid] > target:
            return self.search_rec(nums, target, start, mid - 1)
        else:
            return mid
        
    def search(self, nums: List[int], target: int) -> int:
        return self.search_rec(nums, target, 0, len(nums) - 1)

