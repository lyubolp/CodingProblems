class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive_nums = [num for num in nums if num > 0]
        
        count = {}
        
        for num in positive_nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
                
        for i in range(1, pow(2, 31)):
            if i not in count:
                return i

