from typing import List
class Solution:
    def shift_str(self, s: str, n: int) -> str:
        target = (ord(s) + n - 97) % 26
        return chr(target + 97)
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = [c for c in s]

        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        for i in range(len(shifts)):
            result[i] = self.shift_str(result[i], shifts[i])
            
        return "".join(result)

if __name__ == "__main__":
    o = Solution()
    s = "abc"
    # s = "bad"
    
    shifts = [3, 5, 9]
    # shifts = [10,20,30]

    # N = |shifts|, S = |s|

    print(o.shiftingLetters(s, shifts))