class Solution:
    def get_next_greater(self, nums: List[int], start: int) -> int:
        for i in range(start + 1, len(nums)):
            if nums[i] > nums[start]:
                return nums[i]
        
        for i in range(0, start):
            if nums[i] > nums[start]:
                return nums[i]
        
        return -1
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return [self.get_next_greater(nums, i) for i in range(len(nums))]

