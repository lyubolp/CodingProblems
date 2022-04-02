class Solution:
    def is_palindrome(self, s: str, lives: int) -> bool:
        if s == "":
            return True
        
        if s[0] != s[-1]:
            if lives > 0:
                return self.is_palindrome(s[1:], lives - 1) or self.is_palindrome(s[:-1], lives - 1)
            else:
                return False
        
        return self.is_palindrome(s[1:-1], lives)
    
    def validPalindrome(self, s: str) -> bool:
        return self.is_palindrome(s, 1)

