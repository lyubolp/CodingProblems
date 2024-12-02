class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        indexes = [i for i, word in enumerate(words, start=1) if word.startswith(searchWord)]

        return indexes[0] if len(indexes) > 0 else -1

