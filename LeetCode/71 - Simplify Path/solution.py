class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [item for item in path.split('/') if item != '']
        
        stack = []
        
        for item in path:
            if item == '..':
                if len(stack) > 0:
                    stack.pop()
            elif item == '.':
                pass
            else:
                stack.append(item)
        
        return "/" + "/".join(stack)

