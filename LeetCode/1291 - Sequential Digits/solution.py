class Solution:
    def generate_next_num(self, current: int) -> int: 
        l = int(log10(current)) + 1
        last_digit = current % 10
        if last_digit == 9:
            return self.generate_initial_num(l + 1)
        else:
            return current % (10 ** (l - 1)) * 10 + last_digit + 1
    
    def generate_initial_num(self, length: int) -> int:
        result = 1
        
        while int(log10(result)) + 1 < length:
            last_digit = result % 10
            result *= 10
            result += last_digit + 1
        
        return result
            
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        current = self.generate_initial_num(int(log10(low) + 1))
        while current < low:
            current = self.generate_next_num(current)
        result = []
        while current <= high:
            result.append(current)
            current = self.generate_next_num(current)
        
        return result

