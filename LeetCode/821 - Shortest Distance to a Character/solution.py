class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes = [i for i, ch in enumerate(s) if ch == c]
        return [min([abs(i - val) for val in indexes]) for i, ch in enumerate(s)]

