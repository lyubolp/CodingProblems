class Solution:
    def reverse_word(self, word: str) -> str:
        return ''.join(list(reversed(word)))
    def reverseWords(self, s: str) -> str:
        return ' '.join([self.reverse_word(word) for word in s.split(' ')])

