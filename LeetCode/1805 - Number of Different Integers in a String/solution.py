class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ints = "".join([c if c.isnumeric() else " " for c in word]).strip().split(' ')
        ints = [int(item) for item in ints if item != '']
        return len(set(ints))

