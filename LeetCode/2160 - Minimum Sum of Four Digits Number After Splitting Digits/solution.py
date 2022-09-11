class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(str(num))
        
        first = nums[0] + nums[2]
        second = nums[1] + nums[3]
        
        return int(first) + int(second)

