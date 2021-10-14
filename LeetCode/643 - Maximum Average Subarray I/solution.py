class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = k
        
        result = sum(nums[start:end])
        current = result
        while end < len(nums):
            current -= nums[start]
            current += nums[end]
            
            if current > result:
                result = current
                
            start += 1
            end += 1
            
        return result / (end - start)

