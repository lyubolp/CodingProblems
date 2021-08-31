class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        
        for num in nums:
            if num in seen:
                del seen[num]
            else:
                seen[num] = 1
                
        return list(seen.keys())[0]

