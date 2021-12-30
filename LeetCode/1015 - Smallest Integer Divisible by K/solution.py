class Solution:
    def is_number_divisible(self, num: int, k: int) -> bool:
        return num % k == 0
    def smallestRepunitDivByK(self, k: int) -> int:
        if self.is_number_divisible(k, 2) or self.is_number_divisible(k, 5):
            return -1
        
        number = 1
        for i in range(100000):
            if self.is_number_divisible(number, k):
                return int(log10(number)) + 1
            else:
                number = number * 10 + 1
                
        return -1

