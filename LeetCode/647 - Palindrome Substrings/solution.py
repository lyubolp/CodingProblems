class Solution:
    def expand_palindrome(self, s: str, left: int, right: int) -> int:
        result = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
        
        return result
        
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        palindromes = 0
        for i in range(len(s)):
            palindromes += self.expand_palindrome(s, i, i)
            palindromes += self.expand_palindrome(s, i, i+1)
            
        return palindromes

