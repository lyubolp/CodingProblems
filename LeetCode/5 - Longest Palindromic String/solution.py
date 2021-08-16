class Solution:
    def palindromeExpander(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        for i in range(len(s)):
            current_result_odd = self.palindromeExpander(s, i, i)
            if len(current_result_odd) >= len(result):
                result = current_result_odd
                
            current_result_even = self.palindromeExpander(s, i, i+1)
            if len(current_result_even) >= len(result):
                result = current_result_even
            
        
        return result

