class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        
        for item in nums:
            if item not in count:
                count[item] = 1
            else:
                count[item] += 1
        
        return [i for i in range(1, len(nums) + 1) if i not in count]

