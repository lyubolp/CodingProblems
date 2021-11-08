class Solution:
    def calc(self, result: List[int]) -> int:
        if len(result) == 0 or len(result) == 1:
            return 1
        return sum([result[i] * result[-(i+1)] for i in range(len(result))])
    
    def numTrees(self, n: int) -> int:
        result = [0 for i in range(n+1)]
        
        result[0] = 1
        result[1] = 1
        
        for i in range(2, n+1):
            result[i] = self.calc(result[:i])
        
        return result[n]

