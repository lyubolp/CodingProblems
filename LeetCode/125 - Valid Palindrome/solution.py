class Solution:
    def convert_to_single_string(self, s: str) -> str:
        return "".join([c.lower() for c in s if c.isalnum()])
    def isPalindrome(self, s: str) -> bool:
        s = self.convert_to_single_string(s)
        for i in range(len(s) // 2):
            if s[i] != s[-(i+1)]:
                return False
        
        return True

