class Solution:
    def findComplement(self, num: int) -> int:
        num_in_binary = format(num, 'b')
        complement = ['0' if c == '1' else '1' for c in num_in_binary]
        return int("".join(complement), base=2)

