class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        
        result = nums[0]
        for num in nums[1:]:
            result = result ^ num
            
        return result

