class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([pattern for pattern in patterns if pattern in word])

