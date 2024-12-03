class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        previous = 0
        for amount, index in enumerate(spaces):
            result += s[previous:index]
            result += ' '
            previous = index
        
        result += s[previous:]
        
        return ''.join(result)

