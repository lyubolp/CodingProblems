class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_negative = False
        
        if x < 0:
            is_negative = True
            x = abs(x)
        
        while x >= 10: 
            digit = x % 10
            res = res * 10 + digit
            x = x // 10
        
        res = res * 10 + x
        
        if is_negative: 
            res = res * -1
        
        if not (pow(-2, 31) <=res<= pow(2, 31) - 1):
            return 0
        return res
            
        
