class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        
        result = [num for num in nums if count[num] == 1 and num - 1 not in count and num + 1 not in count]
        return result

