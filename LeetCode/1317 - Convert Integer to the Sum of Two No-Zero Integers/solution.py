class Solution:
    def is_number_no_zero(self, num: int) -> bool:
        return not '0' in str(num)
    
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if self.is_number_no_zero(i) and self.is_number_no_zero(n - i):
                return [i, n - i]

