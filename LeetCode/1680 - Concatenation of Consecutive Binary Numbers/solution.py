class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = ['{0:b}'.format(i) for i in range(1, n+1)]
        concatenated = ''.join(result)
        
        return int(concatenated, base=2) % (10 ** 9 + 7)

