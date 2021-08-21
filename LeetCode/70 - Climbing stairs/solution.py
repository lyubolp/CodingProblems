class Solution:
    def __init__(self):
        self.calculated = {}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if n - 1 in self.calculated:
            first = self.calculated[n-1]
        else:
            first = self.climbStairs(n - 1)
            self.calculated[n-1] = first
            
        if n - 2 in self.calculated:
            second = self.calculated[n-2]
        else:
            second = self.climbStairs(n - 2)
            self.calculated[n - 2] = second
        
        return first + second

