class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if s == '()':
            return 1
        
        open_brackets = 0
        for i, c in enumerate(s):
            if c == '(':
                open_brackets += 1
            else:
                open_brackets -= 1
                
            if open_brackets == 0 and i < len(s) - 1:
                return self.scoreOfParentheses(s[:i+1]) + self.scoreOfParentheses(s[i+1:])
        
        return 2 * self.scoreOfParentheses(s[1:-1])

