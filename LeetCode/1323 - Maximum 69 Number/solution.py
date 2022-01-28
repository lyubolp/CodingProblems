class Solution:
    def maximum69Number (self, num: int) -> int:
        is_changed = False
        result = []
        for c in str(num):
            if c == '6' and not is_changed:
                result.append('9')
                is_changed = True
            else:
                result.append(c)
                
        return int("".join(result))

