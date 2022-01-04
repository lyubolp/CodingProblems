class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        length = int(log2(n)) + 1
        xor_mask = (2 ** length) - 1
        
        return n ^ xor_mask

