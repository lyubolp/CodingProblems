class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 0:
            return ''
        
        stack = [s[0]]
        
        for c in s[1:]:
            if len(stack) > 0 and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)

