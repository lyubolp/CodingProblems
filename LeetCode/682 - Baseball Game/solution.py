class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        
        for op in ops:
            if op == '+':
                result.append(result[-1] + result[-2])
            elif op == 'D':
                result.append(result[-1] * 2)
            elif op == 'C':
                result.pop(-1)
            else:
                result.append(int(op))
        
        return sum(result)
