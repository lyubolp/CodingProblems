class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        bracket_pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for current_bracket in s:
            if current_bracket in bracket_pairs.keys():
                if len(brackets) == 0:
                    return False
                
                last_bracket = brackets.pop()
                
                if last_bracket != bracket_pairs[current_bracket]:
                    return False
            else:
                brackets.append(current_bracket)
        return len(brackets) == 0
        
