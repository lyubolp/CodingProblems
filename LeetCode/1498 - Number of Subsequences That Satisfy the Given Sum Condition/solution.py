class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        result = 0
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                result += 2 ** (r - l)
                l += 1
                    
        return result % (10 ** 9 + 7)

