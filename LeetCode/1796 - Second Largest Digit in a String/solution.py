class Solution:
    def secondHighest(self, s: str) -> int:
        digits = [int(c) for c in s if c.isdigit()]
        
        if len(digits) == 0:
            return -1
        
        count = {}
        
        for digit in digits:
            if digit not in count:
                count[digit] = 1
                
        uniq_digits = list(count.keys())
        
        if len(uniq_digits) == 1:
            return -1
        
        uniq_digits.sort()
        
        return uniq_digits[-2]

