class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = [abs(nums[i] - nums[j]) for i in range(len(nums) - 1) for j in range(i+1, len(nums))]
        return len([item for item in result if item == k])

