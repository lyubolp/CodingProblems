class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_on = 0
        result = []
        while len(a) > 0 or len(b) > 0:
            first = int(a[-1]) if len(a) > 0 else 0
            second = int(b[-1]) if len(b) > 0 else 0
            
            current_result = first + second + carry_on
            
            carry_on = 0
            
            if current_result == 2:
                result.insert(0, '0')
                carry_on = 1
            elif current_result == 3:
                result.insert(0, '1')
                carry_on = 1
            else:
                result.insert(0, str(current_result))
            
            a = a[:-1]
            b = b[:-1]
        if carry_on == 1:
            result.insert(0, str(1))
            
        return "".join(result)

