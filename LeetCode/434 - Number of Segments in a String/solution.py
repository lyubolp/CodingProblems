class Solution:
    def countSegments(self, s: str) -> int:
        return len([c for c in s.split(' ') if c != ''])

