class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # [0, 1, _, _, _, _, _]
        if n == 0:
            return 0
        
        result = [0 for i in range(n+1)] 
        result[1] = 1
        for i in range(2, n+1):
            j = i // 2
            
            if i % 2 == 0:
                result[i] = result[j]
            else:
                result[i] = result[j] + result[j+1]
        
        return max(result)

