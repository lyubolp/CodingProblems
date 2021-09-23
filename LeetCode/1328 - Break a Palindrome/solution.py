class Solution:
    def is_string_palindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        elif s[0] == s[-1]:
            return self.is_string_palindrome(s[1:-1])
        else:
            return False

    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        result = [c for c in palindrome]
        
        for i in range(len(result)):
            if result[i] != 'a':
                result[i] = 'a'
                break
        
        if len(result) == len([c for c in result if c == 'a']):
            result = [c for c in palindrome]

        if result == [c for c in palindrome]:
            result[-1] = 'b'
        
        return "".join(result)
    
if __name__ == "__main__":
    s = Solution()
    palindrome = "aba"
    print(s.breakPalindrome(palindrome))
        