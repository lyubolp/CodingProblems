class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        count = [0] * 10001
        
        for num in nums:
            count[abs(num)] += 1
            
        result = []
        
        for i, num in enumerate(count):
            if num > 0:
                for j in range(num):
                    result.append(i ** 2)
                    
        return result

