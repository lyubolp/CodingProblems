class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        last_symbol = 0
        for i in range(len(s)):
            if converter[s[i]] > last_symbol:
                result -= 2 * last_symbol
            result += converter[s[i]]
            last_symbol = converter[s[i]]
            
        return result
