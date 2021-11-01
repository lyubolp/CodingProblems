class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        
        while n > 1:
            highest_bit = int(log2(n))
            n -= pow(2, highest_bit)
            result += 1
        
        if n == 1:
            result += 1
            
        return result

