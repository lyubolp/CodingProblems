class Solution:
    def is_number_self_dividing(self, num: int) -> bool:
        return '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right + 1) if self.is_number_self_dividing(num)]

