class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = [c for c in s if c == 'A']
        
        if len(absent) >= 2:
            return False
        
        for i in range(2, len(s)):
            if s[i] == 'L' and s[i-1] == 'L' and s[i - 2] == 'L':
                return False
            
        return True

