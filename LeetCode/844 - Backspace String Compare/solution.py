class Solution:
    def handle_string(self, s: str) -> str:
        result = []
        
        for c in s:
            if c == '#':
                if len(result) > 0:
                    result.pop()
            else:
                result.append(c)
        
        return "".join(result)
            
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.handle_string(s)
        t = self.handle_string(t)
        
        return s == t

