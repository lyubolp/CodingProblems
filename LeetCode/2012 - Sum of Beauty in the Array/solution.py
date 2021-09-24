class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        right = [None] * len(nums)
        l = len(nums)
        right[l - 1] = nums[l - 1]
        for i in range(l - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
            
        left = [None] * len(nums)
        left[0] = nums[0]
        for i in range(1, l):
            left[i] = max(left[i - 1], nums[i])
            
        sum = 0
        for i in range(1, l - 1):
            if left[i - 1] < nums[i] < right[i + 1]:
                sum += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                sum += 1
            
        return sum

