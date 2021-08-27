class Solution:
    def __init__(self):
        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
    def letterCombinationsHelper(self, digits: str, result: List[str], current: str) -> List[str]:
        if len(digits) == 0:
            result.append(current)
            return
        
        for letter in self.mapping[digits[0]]:
            self.letterCombinationsHelper(digits[1:], result, current + letter)
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        result = []
        
        self.letterCombinationsHelper(digits, result, "")
        
        return result

