class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        votes = 0
        
        for item in nums:
            if votes == 0:
                candidate = item
                votes = 1
            elif item == candidate:
                votes += 1
            else:
                votes -= 1
                
        return candidate

