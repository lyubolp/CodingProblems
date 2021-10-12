# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def get_middle(self, start: int, end: int) -> int:
        return (end + start) // 2
    def guessNumber(self, n: int) -> int:
        
        start = 1
        end = n
        
        current_guess = self.get_middle(start, end)
        result = guess(current_guess)
        
        while result != 0:
            if result == 1:
                start = current_guess + 1
            else:
                end = current_guess - 1
                
            current_guess = self.get_middle(start, end)
            result = guess(current_guess)
            
        return current_guess

