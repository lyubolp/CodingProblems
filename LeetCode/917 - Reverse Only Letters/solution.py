class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = ["" if c.isalpha() else c for i, c in enumerate(s)]
        letters = [c for c in s if c.isalpha()]

        for i, c in enumerate(result):
            if c == "":
                result[i] = letters[-1]
                letters.pop()
        return "".join(result)
