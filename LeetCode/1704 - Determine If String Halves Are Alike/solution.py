class Solution:
    def count_vowels(self, s: str) -> int:
        return sum([1 for c in s if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']])
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s) // 2
        
        return self.count_vowels(s[:l]) ==  self.count_vowels(s[l:])

