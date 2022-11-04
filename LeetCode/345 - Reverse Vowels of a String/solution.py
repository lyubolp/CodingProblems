class Solution:
    def reverseVowels(self, s: str) -> str:
        all_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        volews_in_s = reversed([c for c in s if c in all_vowels])
        
        return ''.join(next(volews_in_s) if c in all_vowels else c for c in s)

