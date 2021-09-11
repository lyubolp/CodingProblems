class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([c.lower() if c.isupper() else c for c in s])

