class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = str(n)
        if len(num) <= 3:
            return num
        
        result = [num[-(i+1)*3:(-i)*3] if i != 0 else num[-3:] for i in range(len(num) // 3)]
        
        if len(num) % 3 != 0:
            result.append(num[:len(num) % 3])
            
        result.reverse()
        
        return ".".join(result)

