class Solution:
    def rotate_number(self, number: str) -> str:
        rotate = {
            '0': '0',
            '1': '1',
            '2': '5',
            '3': '*',
            '4': '*',
            '5': '2',
            '6': '9',
            '7': '*',
            '8': '8',
            '9': '6'
        }
        
        return "".join([rotate[c] for c in number])
    def is_number_good(self, number: str) -> bool:
        
        rotated = self.rotate_number(number)
        
        if '*' in rotated:
            return False
        
        return number != rotated
    
    def rotatedDigits(self, n: int) -> int:
        nums = [str(i) for i in range(n+1)]
        result = [self.is_number_good(num) for num in nums]
        
        return len([item for item in result if item])
 
