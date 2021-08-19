class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if len(s) == 0:
            return 0
        
        result = 0
        isNegative = None
        
        if s[0] == '-':
            isNegative = True
        elif s[0] == '+':
            isNegative = False
        elif s[0].isnumeric():
            result = result * 10 + int(s[0])
        else:
            return 0
            
        for c in s[1:]:
            if c.isnumeric():
                result = result * 10 + int(c)
            else:
                break
                
        if isNegative:
            result *= -1    
            
        if result < -2 ** 31:
            result = (-2 ** 31)
        elif result >= 2 ** 31:
            result = (2 ** 31) - 1
        
        
        return result

