class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = []
        base = ord('a') - 1
        
        for i in range(n):
            offset = (k % 26 if k % 26 != 0 else 26) if k > (n - i - 1) * 26 else 1
            
            result.append(chr(base + offset))
            k -= offset
        
        return "".join(result)

