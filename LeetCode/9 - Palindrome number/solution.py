class Solution:
    def isStringPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        if s[0] == s[-1]:
            return self.isStringPalindrome(s[1:-1])
            
    def isPalindrome(self, x: int) -> bool:
        return self.isStringPalindrome(str(x))
        
        
            
