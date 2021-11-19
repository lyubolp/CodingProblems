class Solution:
    def convert_to_bits(self, num: int) -> set:
        result = set()
        
        while num > 1:
            highest_bit = 2 ** int(log2(num))
            result.add(highest_bit)
            num -= highest_bit
        
        if num == 1:
            result.add(1)
        
        return result
        
    def hammingDistance(self, x: int, y: int) -> int:
        x_bits = self.convert_to_bits(x)
        y_bits = self.convert_to_bits(y)
        
        return len(x_bits ^ y_bits)

